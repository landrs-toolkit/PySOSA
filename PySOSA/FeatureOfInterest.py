from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

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

