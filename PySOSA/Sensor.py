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

