from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
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

class Platform(object):
    """
    Creates a Platform object that represents a SOSA Platform
"""
    # Maybe remove list if makes object too big/not needed, or might want a func that returns this list
    sensors = []
    actuators = []
    samplers = []

    #constructor
    def __init__(self, comment, label):
        self.platform_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        obsgraph.add((self.platform_id, RDF.type, sosa.Platform))
        obsgraph.add((self.platform_id, RDFS.comment, self.comment))
        obsgraph.add((self.platform_id, RDFS.label, self.label))

    #Get platform URI
    def get_uri(self):
        return self.platform_id

    #Add sensor to platform
    def add_sensor(self, Sensor):
            sen_uri = Sensor.get_uri()
            self.sensors.append(sen_uri)
            obsgraph.add((self.platform_id, sosa.hosts, sen_uri))
            print("sensor list after adding")
            print(self.sensors)

    #Add actuator to platform
    def add_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.append(a_uri)
        obsgraph.add((self.platform_id, sosa.hosts, a_uri))


    #Add sampler to platform
    def add_sampler(self, Sampler):
            s_uri = Sampler.get_uri()
            self.samplers.append(s_uri)
            obsgraph.add((self.platform_id, sosa.hosts, s_uri))


    #Remove sensor from platform
    def remove_sensor(self, Sensor):
        sen_uri = Sensor.get_uri()
        self.sensors.remove(Sensor.label)
        obsgraph.remove((self.platform_id, sosa.hosts, sen_uri))

        print("sensor list after removing")
        print(self.sensors)

    #Remove actuator from  platform
    def remove_actuator(self, Actuator):
        a_uri = Actuator.get_uri()
        self.actuators.remove(a_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, a_uri))

    #Remove sampler from platform
    def remove_sampler(self, Sampler):
        s_uri = Sampler.get_uri()
        self.samplers.remove(s_uri)
        obsgraph.remove((self.platform_id, sosa.hosts, s_uri))
