#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
from collections import defaultdict
import hashlib
import json
import logging
import socket
import threading
import time
import websocket

from . import exceptions
from .base_classes import BaseRequest
from . import events

LOG = logging.getLogger(__name__)


class Client:
    """
    Core class for using pyobs

    Simple usage:
        >>> from pyobs import Client, requests as obsrequests
        >>> client = Client("localhost", 4444, "secret")
        >>> client.connect()
        >>> client.call(obsrequests.GetVersion()).obs_websocket_version
        u'4.1.0'
        >>> client.disconnect()

    For advanced usage, including events callback, see the 'samples' directory.
    """

    def __init__(self, host='localhost', port=4444, password=''):
        """
        Construct a new Client wrapper

        :param host: Hostname to connect to
        :param port: TCP Port to connect to (Default is 4444)
        :param password: Password for the websocket server (Leave this field
            empty if no auth enabled on the server)
        """
        self.id = 1
        self.thread_recv = None
        self.ws = None
        self.eventmanager = EventManager()
        self.answers = {}

        self.host = host
        self.port = port
        self.password = password

    def connect(self, host=None, port=None):
        """
        Connect to the websocket server

        :return: Nothing
        """
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port

        try:
            self.ws = websocket.WebSocket()
            LOG.info("Connecting...")
            self.ws.connect("ws://{}:{}".format(self.host, self.port))
            LOG.info("Connected!")
            self._auth(self.password)
            self._run_threads()
        except socket.error as e:
            raise exceptions.ConnectionFailure(str(e))

    def reconnect(self):
        """
        Restart the connection to the websocket server

        :return: Nothing
        """
        try:
            self.disconnect()
        except Exception:
            # TODO: Need to catch more precise exception
            pass
        self.connect()

    def disconnect(self):
        """
        Disconnect from websocket server

        :return: Nothing
        """
        LOG.info("Disconnecting...")
        if self.thread_recv is not None:
            self.thread_recv.running = False

        try:
            self.ws.close()
        except socket.error:
            pass

        if self.thread_recv is not None:
            self.thread_recv.join()
            self.thread_recv = None

    def _auth(self, password):
        auth_payload = {
            "request-type": "GetAuthRequired",
            "message-id": str(self.id),
        }
        self.id += 1
        self.ws.send(json.dumps(auth_payload))
        result = json.loads(self.ws.recv())

        if result['status'] != 'ok':
            raise exceptions.ConnectionFailure(result['error'])
            
        if result.get('authRequired'):
            secret = base64.b64encode(
                hashlib.sha256(
                    (password + result['salt']).encode('utf-8')
                ).digest()
            )
            auth = base64.b64encode(
                hashlib.sha256(
                    secret + result['challenge'].encode('utf-8')
                ).digest()
            ).decode('utf-8')

            auth_payload = {
                "request-type": "Authenticate",
                "message-id": str(self.id),
                "auth": auth,
            }
            self.id += 1
            self.ws.send(json.dumps(auth_payload))
            result = json.loads(self.ws.recv())
            if result['status'] != 'ok':
                raise exceptions.ConnectionFailure(result['error'])
        pass

    def _run_threads(self):
        if self.thread_recv is not None:
            self.thread_recv.running = False
        self.thread_recv = RecvThread(self)
        self.thread_recv.daemon = True
        self.thread_recv.start()

    def call(self, obj):
        """
        Make a call to the OBS server through the Websocket.

        :param obj: Request (class from pyobs.requests module) to send to the
            server.
        :return: Request object populated with response data.
        """
        if not isinstance(obj, BaseRequest):
            raise exceptions.ObjectError(
                "Call parameter is not a request object")
        payload = obj.data()
        r = self.send(payload)
        obj.input(r)
        return obj

    def send(self, data):
        """
        Make a raw json call to the OBS server through the Websocket.

        :param data: Request (python dict) to send to the server. Do not
            include field "message-id".
        :return: Response (python dict) from the server.
        """
        message_id = str(self.id)
        self.id += 1
        data["message-id"] = message_id
        LOG.debug("Sending message id {}: {}".format(message_id, data))
        self.ws.send(json.dumps(data))
        return self._wait_message(message_id)

    def _wait_message(self, message_id):
        timeout = time.time() + 60  # Timeout = 60s
        while time.time() < timeout:
            if message_id in self.answers:
                return self.answers.pop(message_id)
            time.sleep(0.1)
        raise exceptions.MessageTimeout("No answer for message {}".format(
            message_id))

    def register(self, func, event=None):
        """
        Register a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from pyobs.events module) to trigger the
            hook on. Default is None, which means trigger on all events.
        :return: Nothing
        """
        self.eventmanager.register(func, event)

    def unregister(self, func, event=None):
        """
        Unregister a new hook in the websocket client

        :param func: Callback function pointer for the hook
        :param event: Event (class from pyobs.events module) which triggered
            the hook on. Default is None, which means unregister this function
            for all events.
        :return: Nothing
        """
        self.eventmanager.unregister(func, event)


class RecvThread(threading.Thread):

    def __init__(self, core):
        self.core = core
        self.ws = core.ws
        self.running = True
        threading.Thread.__init__(self)

    def run(self):
        while self.running:
            message = ""
            try:
                message = self.ws.recv()

                # recv() can return an empty string (Issue #6)
                if not message:
                    continue

                result = json.loads(message)
                if 'update-type' in result:
                    LOG.debug("Got message: {}".format(result))
                    obj = self.build_event(result)
                    self.core.eventmanager.trigger(obj)
                elif 'message-id' in result:
                    LOG.debug("Got answer for id {}: {}".format(
                        result['message-id'], result))
                    self.core.answers[result['message-id']] = result
                else:
                    LOG.warning("Unknown message: {}".format(result))
            except websocket.WebSocketConnectionClosedException:
                if self.running:
                    self.core.reconnect()
            except (ValueError, exceptions.ObjectError) as e:
                LOG.warning("Invalid message: {} ({})".format(message, e))
        # end while
        LOG.debug("RecvThread ended.")

    @staticmethod
    def build_event(data):
        name = data["update-type"]
        try:
            obj = getattr(events, name)()
        except AttributeError:
            raise exceptions.ObjectError("Invalid event {}".format(name))
        obj.input(data)
        return obj


class EventManager:
    """
    EventManager holds a mapping that relates classes to a list of callbacks.
    """
    def __init__(self):
        self._callbacks_mapping = defaultdict(list)

    def _add(self, key, item):
        self._callbacks_mapping[key].append(item)

    def _remove(self, key, item):
        try:
            self._callbacks_mapping[key].remove(item)
        except ValueError:
            pass  # Nothing to remove
        else:
            # Keep the mapping clean of zero-length lists
            if len(self._callbacks_mapping[key]) == 0:
                del self._callbacks_mapping[key]

    def register(self, callback, trigger=None):
        """
        Register a new callback for the trigger specified.

        If None is specified as trigger, it registers the callback for every
        trigger.

        :param callback: Function to call when triggered
        :param trigger: Class of event that triggers the callback
        :return: Nothing
        """
        self._add(trigger, callback)

    def unregister(self, callback, trigger=None):
        """
        Unregister a callback for the trigger specified.

        If None is specified as trigger, it unregisters the callback for every
        trigger.

        :param callback: Function to stop calling when triggered
        :param trigger: Class of event that triggered the callback
        :return: Nothing
        """
        # Special case for trigger == None, need to remove from all lists
        if trigger is None:
            for trigger in self._callbacks_mapping:
                self._remove(trigger, callback)
        # Checking if trigger is already in the callbacks mapping prevents
        # creating empty lists with remove
        elif trigger in self._callbacks_mapping:
            self._remove(trigger, callback)

    def trigger(self, data):
        """
        Triggers the callbacks registered to the class of the provided object.

        :param data: Object that triggers the callbacks
        :return: Nothing
        """
        # Checking if type(data) is already in the callbacks mapping prevents
        # creating empty lists with the loop
        if type(data) in self._callbacks_mapping:
            for callback in self._callbacks_mapping[type(data)]:
                callback(data)
        if None in self._callbacks_mapping:
            for callback in self._callbacks_mapping[None]:
                callback(data)
