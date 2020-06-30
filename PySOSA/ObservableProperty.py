from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

# Class for managing observableproperties
# Preferably linked to envo, sweet and qudt
class ObservableProperty(object):
    """
    Creates a Observable Property object that represents a SOSA Observable Property
    Observable Property - An observable quality (property, characteristic) of a FeatureOfInterest.

    """

    def __init__(self,label,comment):
        self.property_id = BNode()
        self.label = Literal(label)
        self.comment=Literal(comment)
        obsgraph.add((self.property_id, RDF.type, cfg.sosa.ObservableProperty))
        obsgraph.add((self.property_id, RDFS.comment, self.comment))
        obsgraph.add((self.property_id, RDFS.label, self.label))


    def get_uri(self):
        return self.property_id

