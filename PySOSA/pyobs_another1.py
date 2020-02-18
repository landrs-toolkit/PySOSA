# -*- coding: utf-8 -*-
"""Python module for instantiating and serializing W3C/OGC SSN-EXT Observation Collection.

This module provides utility class objects for maintaining a Observation Collection and the ability to serialize the collections as JSON-LD.

Todo:
    * Add configuration for sensors.
    * Additional Organizational Information

"""

from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
#from pytz import timezone
#import json
#import uuid

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
from rdflib.term import Identifier

context = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "owl": "http://www.w3.org/2002/07/owl#",
    "ssn-ext-examples": "http://example.org/ssn-ext-examples#",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "dcterms": "http://purl.org/dc/terms/",
    "rdfs": "http://www.w3.org/2000/01/rdf-schema#",
    "time": "http://www.w3.org/2006/time#",
    "ssn-ext": "http://www.w3.org/ns/ssn/ext/",
    "sosa": "http://www.w3.org/ns/sosa/",
    "qudt": "http://qudt.org/1.1/schema/qudt#",
    "prov": "http://www.w3.org/ns/prov#",

    "hasUltimateFeatureOfInterest": {
        "@id": "http://www.w3.org/ns/ssn/ext/hasUltimateFeatureOfInterest",
        "@type": "@id"
    },
    "usedProcedure": {
        "@id": "http://www.w3.org/ns/sosa/usedProcedure",
        "@type": "@id"
    },
    "phenomenonTime": {
        "@id": "http://www.w3.org/ns/sosa/phenomenonTime",
        "@type": "@id"
    },
    "observedProperty": {
        "@id": "http://www.w3.org/ns/sosa/observedProperty",
        "@type": "@id"
    },
    "madeBySensor": {
        "@id": "http://www.w3.org/ns/sosa/madeBySensor",
        "@type": "@id"
    },
    "hasFeatureOfInterest": {
        "@id": "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
        "@type": "@id"
    },
    "hasMember": {
        "@id": "http://www.w3.org/ns/ssn/ext/hasMember",
        "@type": "@id"
    },
    "inXSDDateTime": {
        "@id": "http://www.w3.org/2006/time#inXSDDateTime",
        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "hasBeginning": {
        "@id": "http://www.w3.org/2006/time#hasBeginning",
        "@type": "@id"
    },
    "isSampleOf": {
        "@id": "http://www.w3.org/ns/sosa/isSampleOf",
        "@type": "@id"
    },
    "hasResult": {
        "@id": "http://www.w3.org/ns/sosa/hasResult",
        "@type": "@id"
    },
    "imports": {
        "@id": "http://www.w3.org/2002/07/owl#imports",
        "@type": "@id"
    },
    "comment": {
        "@id": "http://www.w3.org/2000/01/rdf-schema#comment"
    },
    "creator": {
        "@id": "http://purl.org/dc/terms/creator",
        "@type": "@id"
    },
    "created": {
        "@id": "http://purl.org/dc/terms/created",
        "@type": "http://www.w3.org/2001/XMLSchema#date"
    },
    "resultTime": {
        "@id": "http://www.w3.org/ns/sosa/resultTime",
        "@type": "http://www.w3.org/2001/XMLSchema#dateTime"
    },

    "ObservationCollection": "ssn-ext:ObservationCollection",
    "hasMember": "ssn-ext:hasMember",
    "isMemberOf": "ssn-ext:isMemberOf",
    "Observation": "sosa:Observation",
    "Sample": "sosa:Sample",
    "observedProperty": "sosa:observedProperty",
    "hasBeginning": "time:hasBeginning",
    "hasEnd": "time:hasEnd",
    "hasGeometry": "gsp:hasGeometry",
    "isSampleOf": "sosa:isSampleOf",
    "isFeatureOfInterestOf": "sosa:isFeatureOfInterestOf",
    "relatedSample": "sampling:relatedSample",
    "quantityValue": "http://qudt.org/schema/qudt#quantityValue",
    "numericValue": "http://qudt.org/schema/qudt#numericValue",
    "unit": "http://qudt.org/schema/qudt#unit"
}

# Add Graph obj
obsgraph = Graph()

# Add namespaces
ssnext = Namespace("http://www.w3.org/ns/ssn/ext/")
sosa = Namespace("http://www.w3.org/ns/sosa/")
prov = Namespace("http://www.w3.org/ns/prov#")
qudt = Namespace("http://qudt.org/1.1/schema/qudt#")
owltime = Namespace("ttp://www.w3.org/2006/time#")
owl = Namespace("http://www.w3.org/2002/07/owl#")
rdf = Namespace("http://purl.org/dc/terms/")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
ssn = Namespace("http://www.w3.org/ns/ssn/")


def get_graph():
    return obsgraph


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
        obsgraph.add((self.obscollid, RDF.type, ssnext.ObservationCollection))
        obsgraph.add((self.obscollid, RDFS.comment, self.comment))

    def addObservation(self, sensorURI, FeatureURI, result):
        obsid = BNode()
        resultTime = datetime.now(tz=None)
        resultTimeLiteral = Literal(resultTime)
        resultLiteral = Literal(result)
        obsgraph.add((obsid, RDF.type, sosa.Observation))
        obsgraph.add((obsid, sosa.madeBySensor, sensorURI))
        obsgraph.add((self.obscollid, ssnext.hasMember, obsid))
        obsgraph.add((obsid, sosa.resultTime, resultTimeLiteral))
        obsgraph.add((obsid, sosa.hasSimpleResult, resultLiteral))


# str(uuid.uuid4())

class Observation(object):


    def __init__(self, label, comment):
        self.comment = Literal(comment)
        self.label = Literal(label)
        self.observation_id = BNode()
        self.dateTime = Literal
        self.simpleResult = Literal


        obsgraph.add((self.observation_id, RDF.type , sosa.Observation))
        obsgraph.add((self.observation_id, RDFS.comment, self.comment))
        obsgraph.add((self.observation_id, RDFS.label, self.label))
        #To be fixed
        #obsgraph.add((self.observation_id, sosa.dateTime, self.dateTime))
        #obsgraph.add((self.observation_id, sosa.hasSimpleResult, self.simpleResult))

    def get_uri(self):
        return self.observation_id

    def set_dateTime(self, dateTime):
        self.dateTime = dateTime

    def set_simpleResult(self,simpleResult):
        self.simpleResult = simpleResult

# Class for managing observableproperties
# Preferably linked to envo, sweet and qudt
class ObservableProperty(object):
    """
    Creates a Observable Property object that represents a SOSA Observable Property

    """

    def __init__(self,label,comment):
        self.property_id = BNode()
        self.label = Literal(label)
        self.comment=Literal(comment)
        obsgraph.add((self.property_id, RDF.type, sosa.ObservableProperty))
        obsgraph.add((self.property_id, RDFS.comment, self.comment))
        obsgraph.add((self.property_id, RDFS.label, self.label))


    def get_uri(self):
        return self.property_id


class FeatureOfInterest(object):
    """   Creates a Feature of Interest object that represents a SOSA Feature of Interest """

    def __init__(self):
        self.uri = "_B0"
        pass


class UltimateFeatureOfInterest(FeatureOfInterest):
    def __init__(self):
        super(UltimateFeatureOfInterest, self).__init__()

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

    def get_uri(self):
        return self.platform_id

    def add_sensor(self, Sensor):
            sen_uri = Sensor.get_uri()
            self.sensors.append(sen_uri)
            obsgraph.add((self.platform_id, sosa.hosts, sen_uri))
            print("sensor list after adding")
            print(self.sensors)

    def add_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.append(a_uri)
        obsgraph.add((self.platform_id, sosa.hosts, a_uri))



    def add_sampler(self, Sampler):
            s_uri = Sampler.get_uri()
            self.samplers.append(s_uri)
            obsgraph.add(self.platform_id, sosa.hosts, s_uri)



    def remove_sensor(self, Sensor):
        sen_uri = Sensor.get_uri()
        self.sensors.remove(Sensor.label)
        obsgraph.remove((self.platform_id, sosa.hosts, sen_uri))

        print("sensor list after removing")
        print(self.sensors)

    def remove_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.remove(a_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, a_uri))


    def remove_sampler(self, Sampler):
        s_uri = Sampler.get_uri()
        self.samplers.remove(s_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, s_uri))


class Sensor(object):

    """
    Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure.
    Sensors respond to a Stimulus, e.g., a change in the environment, or Input data composed
    from the Results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.
    """

    observations = []

    #constructor
    def __init__(self, label,comment):
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.sensor_id = BNode()
        self.obs_property = Literal
        obsgraph.add((self.sensor_id, RDF.type, sosa.Sensor))
        obsgraph.add((self.sensor_id, RDFS.comment, self.comment))
        obsgraph.add((self.sensor_id, RDFS.label, self.label))

    #set sensor id
    def set_sensor_id(self, sensor_id):
        self.sensor_id = sensor_id

    #get sensor id
    def get_uri(self):
        return self.sensor_id

    #add observable property

    def add_obs_property(self, ObservableProperty):
        a_uri = ObservableProperty.get_uri()
        obsgraph.add((self.sensor_id, sosa.observes, a_uri))

    #add procedure
    def add_procedure(self,Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.sensor_id, sosa.implements, p_uri))

    #define platfrom that hosts sensor
    def add_platform(self,Platform):
        pl_uri = Platform.get_uri()
        obsgraph.add((self.sensor_id, sosa.isHostedBy, pl_uri))

    #define observation
    def add_observation(self,Observation):
        o_uri=Observation.get_uri()
        obsgraph.add((self.sensor_id, sosa.madeObservation, o_uri))
        self.observations.append(Observation)




class Procedure(object):
    """
    Creates a Procedure object
    """

    def __init__(self, comment, label):
        self.procedure_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.input = BNode()
        self.output = BNode()

        obsgraph.add((self.procedure_id, RDF.type, sosa.Procedure))
        obsgraph.add((self.procedure_id, RDFS.comment, self.comment))
        obsgraph.add((self.procedure_id, RDFS.label, self.label))
        obsgraph.add((self.procedure_id, sosa.hasInput, self.input))
        obsgraph.add((self.procedure_id, sosa.hasOutput, self.output))

    def set_procedure_id(self, procedure_id):
        self.procedure_id = procedure_id

    def get_uri(self):
        return self.procedure_id



class Actuation(object):
    """
    An Actuation carries out an (Actuation) Procedure to change the state of the world using an Actuator.
    """

    def __init__(self,label,comment):
        self.actuation_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal
        self.simpleResult = Literal

        obsgraph.add((self.actuation_id, RDF.type, sosa.Actuation))
        obsgraph.add((self.actuation_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuation_id, RDFS.label, self.label))
        obsgraph.add((self.actuation_id, sosa.resultTime, self.dateTime))
        obsgraph.add((self.actuation_id, sosa.hasResult, self.simpleResult))

        def get_uri(self):
            return self.actuation_id

        #add feature of interest
        def add_featureOfInterest(self, FeatureOfInterest):
            f_uri = FeatureOfInterest.get_uri()
            obsgraph.add((self.actuation_id, sosa.hasFeatureOfInterest, f_uri))


class ActuatableProperty(object):
    """
    An actuatable quality (property, characteristic) of a FeatureOfInterest.
    """

    def __init__(self,label,comment):
        self.actuatable_property_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.actuatable_property_id, RDF.type, sosa.ActuatableProperty))
        obsgraph.add((self.actuatable_property_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuatable_property_id, RDFS.label, self.label))

    def get_uri(self):
            return self.actuatable_property_id

class FeatureOfInterest(object):
    """
    The thing whose property is being estimated or calculated in the course of an Observation
    to arrive at a Result, or whose property is being manipulated by an Actuator,
    or which is being sampled or transformed in an act of Sampling.
    """

    def __init__(self,label,comment):
        self.feature_of_interest_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        def get_uri(self):
            return self.feature_of_interest_id

        obsgraph.add((self.feature_of_interest_id, RDF.type, sosa.FeatureOfInterest))
        obsgraph.add((self.feature_of_interest_id, RDFS.comment, self.comment))
        obsgraph.add((self.feature_of_interest_id, RDFS.label, self.label))

class Actuator(object):
    """
     A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.

    """
    actuations = []

    def __init__(self,label,comment):
        self.actuator_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.actuatableProperty = Literal

        obsgraph.add((self.actuator_id, RDF.type, sosa.Actuator))
        obsgraph.add((self.actuator_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuator_id, RDFS.label, self.label))

    def get_uri(self):
        return self.actuator_id

    def set_actuator_id(self, actuator_id):
        self.actuator_id = actuator_id
    #add procedure
    def add_procedure(self, Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.actuator_id, sosa.implements, p_uri))
    #add actuableProperty
    def add_actuatableProperty(self, ActuatableProperty):
        a_uri = ActuatableProperty.get_uri()
        obsgraph.add((self.actuator_id, sosa.actsOnProperty, a_uri))
    #add actuation
    def add_actuation(self, Actuation):
        a_uri = Actuation.get_uri()
        obsgraph.add((self.actuator_id, sosa.madeActuation, a_uri))
        self.actuations.append(a_uri)

class Sampler(object):
    """
     A device that is used by, or implements, a (Sampling) Procedure to create or transform one or more samples.
    """
    samplings = []

    def __init__(self,label,comment):
        self.sampler_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)


        obsgraph.add((self.sampler_id, RDF.type, sosa.Sampler))
        obsgraph.add((self.sampler_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampler_id, RDFS.label, self.label))

    def get_uri(self):
        return self.sampler_id

    def set_sampler_id(self, sampler_id):
        self.sampler_id = sampler_id
    #add procedure
    def add_procedure(self, Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.sampler_id, sosa.implements, p_uri))
    #add actuation
    def add_sampling(self, Sampling):
        a_uri = Sampling.get_uri()
        obsgraph.add((self.sampler_id, sosa.madeSampling, a_uri))
        self.samplings.append(a_uri)

class Sampling(object):
    """
     An act of Sampling carries out a (Sampling) Procedure to create or transform one or more Samples.
    """

    def __init__(self,label,comment):
        self.sampling_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal
        self.simpleResult = Literal

        obsgraph.add((self.sampling_id, RDF.type, sosa.Sampling))
        obsgraph.add((self.sampling_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampling_id, RDFS.label, self.label))
        obsgraph.add((self.sampling_id, sosa.resultTime, self.dateTime))
        obsgraph.add((self.sampling_id, sosa.hasResult, self.simpleResult))

        def get_uri(self):
            return self.sampling_id

        #add feature of interest
        def add_featureOfInterest(self, FeatureOfInterest):
            f_uri = FeatureOfInterest.get_uri()
            obsgraph.add((self.sampling_id, sosa.hasFeatureOfInterest, f_uri))

