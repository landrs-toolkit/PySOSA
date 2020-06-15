from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

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


