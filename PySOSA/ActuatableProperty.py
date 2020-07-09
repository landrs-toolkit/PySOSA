# imports

from rdflib import Graph, BNode, Literal, RDF, RDFS
from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class ActuatableProperty(object):
    """
    Creating an Actuatable Property object that represents a SOSA Actuable Property
    An actuatable quality (property, characteristic) of a FeatureOfInterest.
    """

    def __init__(self,label,comment):
        """ instantiating Actuatable Property, an actuable quality of a FOI
           Args:
               label, comment (literal): label and comment for the actuatable property
           Returns:
               ActuatableProperty object: instantiated with characteristics of a FOI
        """
        self.actuatable_property_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.actuatable_property_id, RDF.type, cfg.sosa.ActuatableProperty))
        obsgraph.add((self.actuatable_property_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuatable_property_id, RDFS.label, self.label))

    def get_uri(self):
        """
        get actuatable property id
        """
        return self.actuatable_property_id
