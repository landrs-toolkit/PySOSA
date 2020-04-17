from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Actuator(object):
    """
     A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.

    """
    actuations = []

    def __init__(self,label,comment):
        self.actuator_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.actuatableProperty = Literal

        obsgraph.add((self.actuator_id, RDF.type, cfg.sosa.Actuator))
        obsgraph.add((self.actuator_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuator_id, RDFS.label, self.label))

    def get_uri(self):
        return self.actuator_id

    def set_actuator_id(self, actuator_id):
        self.actuator_id = actuator_id
    #add procedure
    def add_procedure(self, Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.actuator_id, cfg.sosa.implements, p_uri))
    #add actuableProperty
    def add_actuatableProperty(self, ActuatableProperty):
        a_uri = ActuatableProperty.get_uri()
        obsgraph.add((self.actuator_id, cfg.sosa.actsOnProperty, a_uri))
    #add actuation
    def add_actuation(self, Actuation):
        a_uri = Actuation.get_uri()
        obsgraph.add((self.actuator_id, cfg.sosa.madeActuation, a_uri))
        self.actuations.append(a_uri)

