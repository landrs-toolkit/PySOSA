# -*- coding: utf-8 -*-
"""Python module for instantiating and serializing W3C/OGC SSN-EXT Observation Collection.

This module provides utility class objects for maintaining a Observation Collection and the ability to serialize the collections as JSON-LD.

Todo:
    * Add configuration for sensors.
    * Additional Organizational Information

"""

from rdflib import Graph,URIRef, BNode, Literal, Namespace, RDF
from pyld import jsonld
from datetime import datetime
from pytz import timezone
import json
import uuid


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



context = {
   "rdf" : "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "owl" : "http://www.w3.org/2002/07/owl#",
    "ssn-ext-examples" : "http://example.org/ssn-ext-examples#",
    "xsd" : "http://www.w3.org/2001/XMLSchema#",
    "dcterms" : "http://purl.org/dc/terms/",
    "rdfs" : "http://www.w3.org/2000/01/rdf-schema#",
    "time" : "http://www.w3.org/2006/time#",
    "ssn-ext" : "http://www.w3.org/ns/ssn/ext/",
    "sosa" : "http://www.w3.org/ns/sosa/",
"qudt": "http://qudt.org/1.1/schema/qudt#",
"prov": "http://www.w3.org/ns/prov#",

"hasUltimateFeatureOfInterest" : {
      "@id" : "http://www.w3.org/ns/ssn/ext/hasUltimateFeatureOfInterest",
      "@type" : "@id"
    },
    "usedProcedure" : {
      "@id" : "http://www.w3.org/ns/sosa/usedProcedure",
      "@type" : "@id"
    },
    "phenomenonTime" : {
      "@id" : "http://www.w3.org/ns/sosa/phenomenonTime",
      "@type" : "@id"
    },
    "observedProperty" : {
      "@id" : "http://www.w3.org/ns/sosa/observedProperty",
      "@type" : "@id"
    },
    "madeBySensor" : {
      "@id" : "http://www.w3.org/ns/sosa/madeBySensor",
      "@type" : "@id"
    },
    "hasFeatureOfInterest" : {
      "@id" : "http://www.w3.org/ns/sosa/hasFeatureOfInterest",
      "@type" : "@id"
    },
    "hasMember" : {
      "@id" : "http://www.w3.org/ns/ssn/ext/hasMember",
      "@type" : "@id"
    },
    "inXSDDateTime" : {
      "@id" : "http://www.w3.org/2006/time#inXSDDateTime",
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime"
    },
    "hasBeginning" : {
      "@id" : "http://www.w3.org/2006/time#hasBeginning",
      "@type" : "@id"
    },
    "isSampleOf" : {
      "@id" : "http://www.w3.org/ns/sosa/isSampleOf",
      "@type" : "@id"
    },
    "hasResult" : {
      "@id" : "http://www.w3.org/ns/sosa/hasResult",
      "@type" : "@id"
    },
    "imports" : {
      "@id" : "http://www.w3.org/2002/07/owl#imports",
      "@type" : "@id"
    },
    "comment" : {
      "@id" : "http://www.w3.org/2000/01/rdf-schema#comment"
    },
    "creator" : {
      "@id" : "http://purl.org/dc/terms/creator",
      "@type" : "@id"
    },
    "created" : {
      "@id" : "http://purl.org/dc/terms/created",
      "@type" : "http://www.w3.org/2001/XMLSchema#date"
    },
    "resultTime" : {
      "@id" : "http://www.w3.org/ns/sosa/resultTime",
      "@type" : "http://www.w3.org/2001/XMLSchema#dateTime"
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
rdfs = Namespace ("http://www.w3.org/2000/01/rdf-schema#")

class Base(object):
    def __init__(self, type, **kwargs):
        self.jsonld = {
            "@type": type,
        }
        self.jsonld.update(kwargs)


class ObservationCollection(object):
    """ Create SSN-EXT Observation Collection """
    def __init__(self, ):
        self.jsonld={
            "@type": "ssn-ext:ObservationCollection",
            "hasFeatureOfInterest" : "http://example.org/Sample_2",
            "madeBySensor" : "http://example.org/s4",
            "observedProperty" : "http://example.org/op2",
            "phenomenonTime" : "_:b13",
            "usedProcedure" : "http://example.org/p3",
            "hasMember" : [ "http://example.org/O5", "http://example.org/O4" ]
        }
        self.obscollid = BNode()
        obsgraph.add((self.obscollid, RDF.type, ssnext.ObservationCollection))


    def addObservation(self):
        obsid = BNode()
        obsgraph.add((obsid, RDF.type, ssnext.Observation))
        obsgraph.add((self.obscollid, ssnext.hasMember, obsid))

# str(uuid.uuid4())

class Observation(object):
    def __init__(self):
        pass

class Sensor(object):
    def __init__(self):
        pass

class ObservableProperty:
    def __init__(self):
        pass

class FeatureOfInterest(object):
    def __init__(self):
        self.uri = "_B0"
        pass
class UltimateFeatureOfInterest(FeatureOfInterest):
    def __init__(self):
        super(UltimateFeatureOfInterest, self).__init__()