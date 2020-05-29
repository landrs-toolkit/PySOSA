from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier
from PySOSA.ActuatableProperty import ActuatableProperty
from PySOSA.Procedure import Procedure
from PySOSA.Actuation import Actuation

# Add Graph obj
obsgraph = cfg.get_graph()

def get_graph():
    return obsgraph

class Actuator(object):
    """
     A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.

    """
    actuations = []

    #constructor parameters- label,comment, list of actuatable properties,list of procedures
    def __init__(self, *args):
        self.actuator_id = BNode()
        self.label = Literal(args[0])
        self.comment = Literal(args[1])
        self.actuatableProperty = (args[2])
        self.procedure = (args[3])

        obsgraph.add((self.actuator_id, RDF.type, cfg.sosa.Actuator))
        obsgraph.add((self.actuator_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuator_id, RDFS.label, self.label))
        # add list of actuatable properties
        for act in self.actuatableProperty:
            if isinstance(act, ActuatableProperty):
                obsgraph.add((self.actuator_id, cfg.sosa.observes, act.label))
        # add list of procedures
        for pro in self.procedure:
            if isinstance(pro, Procedure):
                obsgraph.add((self.sensor_id, cfg.sosa.implements, pro.label))

    def get_uri(self):
        return self.actuator_id

    def set_actuator_id(self, actuator_id):
        self.actuator_id = actuator_id

    #add a single procedure
    def add_procedure(self, pro):
        if isinstance(pro, Procedure):
            obsgraph.add((self.actuator_id, cfg.sosa.observes, pro.label))

    #add a single  actuableProperty
    def add_actuatableProperty(self, actProp):
        if isinstance(actProp, ActuatableProperty):
            obsgraph.add((self.actuator_id, cfg.sosa.observes, actProp.label))

    #add actuation
    def add_actuation(self, actuation):
        a_uri = actuation.get_uri()
        if isinstance(actuation, Actuation):
            obsgraph.add((self.actuator_id, cfg.sosa.madeActuation, a_uri))
            self.actuations.append(a_uri)

