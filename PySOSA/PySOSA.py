
"""Python module for instantiating and serializing W3C/OGC SSN-EXT Observation Collection.
This module provides utility class objects for maintaining a Observation Collection and the ability to serialize the collections as JSON-LD.
Todo:
    * Add configuration for sensors.
    * Additional Organizational Information
"""
from PySOSA import config as cfg
from datetime import datetime
from rdflib import Graph, BNode, Literal, Namespace, RDF, RDFS

# Contexts for SOSA, SSN-EXT, SOSA
#  SOSA https://github.com/opengeospatial/ELFIE/blob/master/docs/json-ld/sosa.jsonld
#  Timeseries ML  https://github.com/opengeospatial/ELFIE/blob/master/docs/json-ld/tsml.jsonld
#  SSN-EXT https://github.com/opengeospatial/SELFIE/blob/master/docs/contexts/ssn-ext.jsonld
#  QUDT https://github.com/opengeospatial/SELFIE/blob/master/docs/contexts/qudt.jsonld
# datetime.datetime.now(pytz.timezone('Europe/Paris')).isoformat()
# UUID str(uuid.uuid4())
# https://github.com/w3c/sdw/blob/gh-pages/proposals/ssn-extensions/rdf/ssn-ext.jsonld 

# For images that are observations IIF 
# https://github.com/zimeon/iiif-ld-demo

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


    def __init__(self, comment, label):
        self.platform_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        obsgraph.add((self.platform_id, RDF.type, sosa.Platform))
        obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        obsgraph.add((self.platform_id, RDFS.label, self.label))

    def add_sensor(self, Sensor):
        if(isinstance(self, Sensor)):
            sen_uri = Sensor.get_uri()
            self.sensors.append(sen_uri)
            obsgraph.add((self.platform_id, sosa.hosts, sen_uri))
            Sensor.add_platform_id(self.platform_id)
        else:
            raise Exception('Object is not of type Sensor')



    def add_actuator(self, Actuator):
        if(isinstance(self,Actuator)):
            a_uri = Actuator.get_uri()
            self.actuators.append(a_uri)
            obsgraph.add((self.platform_id, sosa.hosts, a_uri))
            Actuator.add_platform_id(self.platform_id)
        else:
            raise Exception('Object is not of type Actuator')

    def add_sampler(self, Sampler):
        if(isinstance(self, Sampler)):
            s_uri = Sampler.get_uri()
            self.samplers.append(s_uri)
            obsgraph.add((self.platform_id, sosa.hosts, s_uri))
            Sampler.add_platform_id(self.platform_id)
        else:
            raise Exception('Object is not of type Sampler')

    def remove_sensor(self, Sensor):
        sen_uri = Sensor.get_uri()
        self.sensors.remove(sen_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, sen_uri))
        Sensor.add_platform_id(self.platform_id)

    def remove_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.remove(a_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, a_uri))
        Actuator.add_platform_id(self.platform_id)

    def remove_sampler(self, Sampler):
        s_uri = Sampler.get_uri()
        self.samplers.remove(s_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, s_uri))
        Sampler.add_platform_id(self.platform_id)

class Actuator(object):
    """
     A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.
    """
    actuations = []

    def __init__(self, comment, label, actuatableProperty,procedure ):
        self.actuator_id = BNode()
        self.platform_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.actuatableProperty = Literal
        self.procedure = Literal

        obsgraph.add((self.actuator_id, RDF.type, sosa.Actuator))  # should we use sosa.system or ssn.system?
        obsgraph.add((self.actuator_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuator_id, RDFS.label, self.label))
        obsgraph.add((self.actuator_id, sosa.actsOnProperty, actuatableProperty))
        obsgraph.add((self.actuator_id, sosa.implements, procedure))
        obsgraph.add((self.actuator_id, sosa.isHostedBy, self.platform_id))


    def set_actuator_id(self, actuator_id):
        self.actuator_id = actuator_id


    def set_platform_id(self, platform_id):
        self.platform_id = platform_id



class Procedure(object):
    """
    Creates a Procedure object
    """

    def __init__(self, comment, label):
        self.procedure_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.input = Literal
        self.output = Literal

        obsgraph.add((self.procedure_id, RDF.type, sosa.Procedure))
        obsgraph.add((self.procedure_id, RDFS.comment, self.comment))
        obsgraph.add((self.procedure_id, RDFS.label, self.label))
        obsgraph.add((self.procedure_id, sosa.hasInput, self.input))
        obsgraph.add((self.procedure_id, sosa.hasOutput, self.output))

    def set_procedure_id(self, procedure_id):
        self.procedure_id = procedure_id


class Actuation(object):
    """
    An Actuation carries out an (Actuation) Procedure to change the state of the world using an Actuator.
    """

    def __init__(self, comment, label,dateTime, featureOfInterest,simpleResult):
        self.actuation_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = datetime
        self.featureOfInterest = Literal
        self.simpleResult = Literal

        obsgraph.add((self.actuation_id, RDF.type, sosa.Actuation))
        obsgraph.add((self.actuation_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuation_id, RDFS.label, self.label))
        obsgraph.add((self.actuation_id, sosa.resultTime, self.dateTime))
        obsgraph.add((self.actuation_id, sosa.hasFeatureOfInterest, self.featureOfInterest))
        obsgraph.add((self.actuation_id, sosa.hasResult, self.simpleResult))


class ActuatableProperty(object):
    """
    An actuatable quality (property, characteristic) of a FeatureOfInterest.
    """

    def __init__(self, comment, label):
        self.actuatable_property_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.actuatable_property_id, RDF.type, sosa.ActuatableProperty))
        obsgraph.add((self.actuatable_property_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuatable_property_id, RDFS.label, self.label))


class FeatureOfInterest(object):
    """
    The thing whose property is being estimated or calculated in the course of an Observation
    to arrive at a Result, or whose property is being manipulated by an Actuator,
    or which is being sampled or transformed in an act of Sampling.
    """

    def __init__(self, comment, label):
        self.feature_of_interest_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.feature_of_interest_id, RDF.type, sosa.FeatureOfInterest))
        obsgraph.add((self.feature_of_interest_id, RDFS.comment, self.comment))
        obsgraph.add((self.feature_of_interest_id, RDFS.label, self.label))


class Sampler(object):
    """
    Feature which is intended to be representative of a FeatureOfInterest on which Observations may be made.
    """
    samplings = []

    def __init__(self, comment, label, sampler_id, platform_id, procedure):
        self.sampler_id = BNode()
        self.platform_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.procedure = Literal


        obsgraph.add((self.sampler_id, RDF.type, sosa.Sampler))
        obsgraph.add((self.sampler_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampler_id, RDFS.label, self.label))
        obsgraph.add((self.sampler_id, sosa.isHostedBy, self.platform_id))
        obsgraph.add((self.sampler_id, sosa.implements, self.procedure))

    def set_sampler_id(self, sampler_id):
        self.sampler_id = sampler_id


    def set_platform_id(self, platform_id):
        self.platform_id = platform_id


class Sampling(object):
    """
    Creates an Actuation object that represents a SOSA System
    """

    def __init__(self, comment, label):
        self.sampling_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = datetime
        self.featureOfInterest = Literal
        self.simpleResult = Literal

        obsgraph.add((self.sampling_id, RDF.type, sosa.Sampling))
        obsgraph.add((self.sampling_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampling_id, RDFS.label, self.label))
        obsgraph.add((self.sampling_id, sosa.hasFeatureOfInterest, self.featureOfInterest))
        obsgraph.add((self.sampling_id, sosa.hasResult, self.simpleResult))


class Sensor(object):

    """
    Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure.
    Sensors respond to a Stimulus, e.g., a change in the environment, or Input data composed
    from the Results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.
    """

    observations = []

    def __init__(self, comment, label, sensor_id, platform_id, observable_property, procedure):
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.sensor_id = BNode()
        self.platform_id = BNode()
        self.observable_property = Literal
        self.procedure = Literal

        obsgraph.add((self.sensor_id, RDF.type, sosa.Sensor))
        obsgraph.add((self.sensor_id, RDFS.comment, self.comment))
        obsgraph.add((self.sensor_id, RDFS.label, self.label))
        obsgraph.add((self.sensor_id, sosa.observes, observable_property))
        obsgraph.add((self.sensor_id, sosa.implements, procedure))
        obsgraph.add((self.sensor_id, sosa.isHostedBy, platform_id))

    def set_platform_id(self, platform_id):
        self.platform_id = platform_id


    def set_sensor_id(self, sensor_id):
        self.sensor_id = sensor_id


    def add_platform_id(self, platform_id):
        obsgraph.add((self.sensor_id, sosa.isHostedBy, platform_id))

    def get_uri(self):
        return self.sensorid

    def add_obs_property(self, observable_property):
        obsgraph.add(self.sensorid, sosa.observes, observable_property)


class ObservationCollection(object):
    """ Create SSN-EXT Observation Collection """

    def __init__(self, comment):
        self.jsonld = {
            "@type": "ssn-ext:ObservationCollection",
            "hasFeatureOfInterest": "http://example.org/Sample_2",
            "madeBySensor": "http://example.org/s4",
            "observedProperty": "http://example.org/op2",
            "phenomenonTime": "_:b13",
            "usedProcedure": "http://example.org/p3",
            "hasMember": ["http://example.org/O5", "http://example.org/O4"]
        }
        self.obscollid = BNode()
        self.comment = Literal(comment)
        obsgraph.add((self.obscollid, RDF.type, cfg.ssnext.ObservationCollection))
        obsgraph.add((self.obscollid, RDFS.comment, self.comment))

    def addObservation(self, sensorURI, FeatureURI, result):
        obsid = BNode()
        resultTime = datetime.now(tz=None)
        resultTimeLiteral = Literal(resultTime)
        resultLiteral = Literal(result)
        obsgraph.add((obsid, RDF.type, cfg.sosa.Observation))
        obsgraph.add((obsid, cfg.sosa.madeBySensor, sensorURI))
        obsgraph.add((self.obscollid, cfg.ssnext.hasMember, obsid))
        obsgraph.add((obsid, cfg.sosa.resultTime, resultTimeLiteral))
        obsgraph.add((obsid, cfg.sosa.hasSimpleResult, resultLiteral))


# str(uuid.uuid4())

class Observation(object):
    def __init__(self, comment, label):
        self.comment = Literal(comment)
        self.observation_id = BNode()
        # Fix Tomorrow
        # obsgraph.add((self.observation_id, cfg.sosa.madeBySensor, sensor_id))
        # obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        # obsgraph.add((self.platform_id, RDFS.label, self.label))


# Class for managing observableproperties
# Preferably linked to envo, sweet and qudt
class ObservableProperty(object):
    """
    Creates a Observable Property object that represents a SOSA Observable Property
    """

    def __init__(self, property_uri):
        if property_uri:
            self.observable_property_uri = property_uri
        else:
            self.observable_property_uri = BNode()
        obsgraph.add((self.observable_property_uri, cfg.rdf.type, cfg.sosa.Observable_property))

    def get_uri(self):
        return self.observable_property_uri


class FeatureOfInterest(object):
    """   Creates a Feature of Interest object that represents a SOSA Feature of Interest """

    def __init__(self):
        self.uri = "_B0"
        pass


class UltimateFeatureOfInterest(FeatureOfInterest):
    def __init__(self):
        super(UltimateFeatureOfInterest, self).__init__()