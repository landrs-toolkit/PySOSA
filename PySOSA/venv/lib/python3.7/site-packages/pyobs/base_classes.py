#!/usr/bin/env python
# -*- coding: utf-8 -*-

from copy import copy


class _Base:
    def __init__(self):
        self._name = '?'
        self._returns = {}

    def __getitem__(self, item):
        return self._returns[item]

    @property
    def name(self):
        return self._name

    def input(self, data):
        self._returns = copy(data)


class BaseEvent(_Base):
    def input(self, data):
        _Base.input(self, data)
        del self._returns['update-type']

    def __repr__(self):
        return "<{} event ({})>".format(self._name, self._returns)


class BaseRequest(_Base):
    def __init__(self):
        _Base.__init__(self)
        self._params = {}
        self._status = None

    def data(self):
        payload = copy(self._params)
        payload.update({'request-type': self._name})
        return payload

    def input(self, data):
        _Base.input(self, data)
        self._status = self._returns['status'] == 'ok'
        del self._returns['message-id']
        del self._returns['status']

    def __repr__(self):
        if self._status is None:
            return "<{} request ({}) waiting>".format(self._name, self._params)
        elif self._status:
            return "<{} request ({}) called: success ({})>".format(
                self._name, self._params, self._returns)
        else:
            return "<{} request ({}) called: failed ({})>".format(
                self._name, self._params, self._returns)
