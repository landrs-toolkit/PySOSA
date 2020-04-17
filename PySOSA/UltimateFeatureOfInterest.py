from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class UltimateFeatureOfInterest(FeatureOfInterest):
    def __init__(self):
        super(UltimateFeatureOfInterest, self).__init__()
