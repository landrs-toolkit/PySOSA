from rdflib import BNode, Literal, RDF, RDFS

from PySOSA import config as cfg
from PySOSA.Actuator import Actuator
from PySOSA.Sampler import Sampler
from PySOSA.Sensor import Sensor

# Add Graph obj
obsgraph = cfg.get_graph()


class Platform(object):

    """
    Creates a Platform object that represents a SOSA Platform
    A Platform is an entity that hosts other entities, particularly Sensors, Actuators, Samplers, and other Platforms.
    """
    # Maybe remove list if makes object too big/not needed, or might want a func that returns this list
    sensors = []
    actuators = []
    samplers = []

    def __init__(self, *args):
        """ constructor for instantiating Platform object
        Args:
            *args (str): label, comment, (list of or a) sensor, actuator, sampler
            platform object can be instantiated with multiple arguments, can have multiple sensors, actuators etc.
        Returns:
            object: an instantiated platform object with assigned attributes to it
        """
        self.platform_id = BNode()
        self.label = Literal(args[0])
        self.comment = Literal(args[1])
        self.sensorList = args[2]  # lists of sensors
        self.actuatorList = args[3]  # lists of actuators
        self.samplerList = args[4]  # lists of samplers
        obsgraph.add((self.platform_id, RDF.type, cfg.sosa.Platform))
        obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        obsgraph.add((self.platform_id, RDFS.label, self.label))
        # add sensors
        for sen in self.sensorList:
            if isinstance(sen, Sensor):
                # check if sensorList is not empty
                # if len(self.get_sensors_list() != 0):
                # add to list of sensors
                self.sensors.append(sen)
                # add to graph
                obsgraph.add((self.platform_id, cfg.sosa.hosts, sen.label))
            # else:
            #     raise Exception("Cannot add empty sensor! ")

        # add actuators
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

    def get_uri(self):
        """
        method to get the platform Uniform Resource Identifier (URI)
        The URI is a reliably unique way of representing an entity (a drone, an object, a relationship, etc)
        """
        return self.platform_id

    def add_sensor(self, sensor):
        """ Add a sensor to the platform
        Args:
            sensor (str): The sensor object
        Returns:
            str: a list of sensors, platform with sensors added to it
        """
        if isinstance(sensor, Sensor):
            # add sensor to list
            self.sensors.append(sensor)
            # add sensor to rdf graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sensor.label))
        else:
            raise Exception('Type error: object not of type Sensor')

    def get_sensors_list(self):
        """ return list of sensors
        get sensors list that was added to the platform
        """
        return self.sensors

    def add_actuator(self, actuator):
        """ Add an actuator to a platform
        Args:
            self, actuator (str): self, actuator to be added
        Returns:
            Platform object: a platform object with actuator added to the obsgraph
        """
        # check if it is an actuator before adding
        if isinstance(actuator, Actuator):
            a_uri = actuator.get_uri()
            # add actuators to list
            self.actuators.append(a_uri)
            # add actuators to graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, actuator.label))
        else:
            raise Exception('Type error: object not of type Actuator')

    def add_sampler(self, sampler):
        """
        Add a single sampler to the platform
        check if it is a sampler before adding, add to the graph
        """
        if isinstance(sampler, Sampler):
            s_uri = sampler.get_uri()
            # add sampler to list
            self.samplers.append(s_uri)
            # add samplers to graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sampler.label))
        else:
            raise Exception('Type error: object not of type Sampler')

    def remove_sensor(self, Sensor):
        """
        Remove sensor from platform
        Args:
            self, sensor
        Returns: Platform with removed sensor
        """
        sen_uri = Sensor.get_uri()
        self.sensors.remove(Sensor.label)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, sen_uri))

    def remove_actuator(self, Actuator):
        """ Remove actuator from  platform
        Args:
            self, actuator (str): platform object, actuator to be removed
        Returns:
            Platform Object: a platform with the removed actuator from the obsgraph
        """
        a_uri = Actuator.get_uri()
        self.actuators.remove(a_uri)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, a_uri))

    def remove_sampler(self, Sampler):
        """ Remove sampler
                Args:
                    self, sampler (str): a sampler object to be removed
                Returns:
                    Platform Object: a platform with the sampler removed from the obsgraph
                """
        s_uri = Sampler.get_uri()
        self.samplers.remove(s_uri)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, s_uri))
