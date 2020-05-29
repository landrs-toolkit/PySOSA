from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier
from PySOSA.Sensor import Sensor
from PySOSA.Actuator import Actuator
from PySOSA.Sampler import Sampler

# Add Graph obj
obsgraph = cfg.get_graph()

class Platform(object):
    """
    Creates a Platform object that represents a SOSA Platform
"""
    # Maybe remove list if makes object too big/not needed, or might want a func that returns this list
    sensors = []
    actuators = []
    samplers = []

    #constructor
    # def __init__(self, comment, label):
    def __init__(self, *args):
        self.platform_id = BNode()
        self.label = Literal(args[1])
        self.comment = Literal(args[0])
        self.sensorList = args[2]#lists of sensors
        self.actuatorList = args[3]#lists of actuators
        self.samplerList = args[4]#lists of samplers
        obsgraph.add((self.platform_id, RDF.type, cfg.sosa.Platform))
        obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        obsgraph.add((self.platform_id, RDFS.label, self.label))
        #add sensors
        for sen in self.sensorList:

            if isinstance(sen, Sensor):
                # add to list of sensors
                self.sensors.append(sen)
                #add to graph
                obsgraph.add((self.platform_id, cfg.sosa.hosts, sen.label))

        #add actuators
        for act in self.actuatorList:
            if isinstance(act, Actuator):
                # add to list of sensors
                self.actuators.append(act)
                # add to graph
                obsgraph.add((self.platform_id, cfg.sosa.hosts, act.label))

            # add samplers
        for sam in self.samplerList:
            if isinstance(sam, Sampler):
                # add to list of sensors
                self.samplers.append(sam)
                # add to graph
                obsgraph.add((self.platform_id, cfg.sosa.hosts, sam.label))


    #Get platform URI
    def get_uri(self):
        return self.platform_id

        # Add a single sensor to platform
    def add_sensor(self, sensor):

        # check if it is a sensor before adding
        if isinstance(sensor, Sensor):
            # add sensor to list
            self.sensors.append(sensor)
            # add sensor to rdf graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sensor.label))

        else:
            raise Exception('Type error: object not of type Sensor')

    # return list of sensors
    def get_sensors_list(self):
        return self.sensors

    # Add a single actuator to platform
    def add_actuator(self, actuator):
        # check if it is an actuator before adding
        if isinstance(actuator, Actuator):
            a_uri = actuator.get_uri()
            # add actuators to list
            self.actuators.append(a_uri)
            # add actuators to graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, actuator.label))
        else:
            raise Exception('Type error: object not of type Actuator')

    # Add a single sampler to platform
    def add_sampler(self, sampler):
        # check if it is an sampler before adding
        if isinstance(sampler, Sampler):
            s_uri = sampler.get_uri()
            # add sampler to list
            self.samplers.append(s_uri)
            # add samplers to graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sampler.label))
        else:
            raise Exception('Type error: object not of type Sampler')

    #Remove sensor from platform
    def remove_sensor(self, Sensor):
        sen_uri = Sensor.get_uri()
        self.sensors.remove(Sensor.label)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, sen_uri))

    #Remove actuator from  platform
    def remove_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.remove(a_uri)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, a_uri))

    #Remove sampler from platform
    def remove_sampler(self, Sampler):
        s_uri = Sampler.get_uri()
        self.samplers.remove(s_uri)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, s_uri))
