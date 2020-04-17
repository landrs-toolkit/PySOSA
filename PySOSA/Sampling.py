from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Sampling(object):
    """
     An act of Sampling carries out a (Sampling) Procedure to create or transform one or more Samples.
    """

    def __init__(self,label,comment):
        self.sampling_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal(datetime)
        self.simpleResult = Literal

        obsgraph.add((self.sampling_id, RDF.type, cfg.sosa.Sampling))
        obsgraph.add((self.sampling_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampling_id, RDFS.label, self.label))
        obsgraph.add((self.sampling_id, cfg.sosa.datetime, self.dateTime))
        #fix
        #obsgraph.add((self.sampling_id, cfg.sosa.hasresult, self.simpleResult))

    def get_uri(self):
        return self.sampling_id

    #add feature of interest
    def add_featureOfInterest(self, FeatureOfInterest):
        f_uri = FeatureOfInterest.get_uri()
        obsgraph.add((self.sampling_id, cfg.sosa.hasFeatureOfInterest, f_uri))


