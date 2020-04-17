from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

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
