from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

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
        obsgraph.add((self.platform_id, RDF.type, cfg.sosa.Platform))
        obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        obsgraph.add((self.platform_id, RDFS.label, self.label))

    #Get platform URI
    def get_uri(self):
        return self.platform_id

    #Add sensor to platform
    def add_sensor(self, Sensor):
            sen_uri = Sensor.get_uri()
            self.sensors.append(sen_uri)
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sen_uri))
            print("sensor list after adding")
            print(self.sensors)

    #Add actuator to platform
    def add_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.append(a_uri)
        obsgraph.add((self.platform_id, cfg.sosa.hosts, a_uri))


    #Add sampler to platform
    def add_sampler(self, Sampler):
            s_uri = Sampler.get_uri()
            self.samplers.append(s_uri)
            obsgraph.add((self.platform_id, cfg.sosa.hosts, s_uri))


    #Remove sensor from platform
    def remove_sensor(self, Sensor):
        sen_uri = Sensor.get_uri()
        self.sensors.remove(Sensor.label)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, sen_uri))

        print("sensor list after removing")
        print(self.sensors)

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
