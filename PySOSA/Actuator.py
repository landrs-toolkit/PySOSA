from rdflib import BNode, Literal, RDF, RDFS

from PySOSA import config as cfg
from PySOSA.ActuatableProperty import ActuatableProperty
from PySOSA.Actuation import Actuation
from PySOSA.Procedure import Procedure

# Add Graph obj
obsgraph = cfg.get_graph()

def get_graph():
    return obsgraph

class Actuator(object):
    """
     Creates an Actuator object representing a SOSA Actuator
     A device that is used by, or implements, an (Actuation) Procedure that changes the state of the world.
    """
    actuations = []


    def __init__(self, *args):
        """ instantiating Actuator object
           Args:
               *args (str): label, comment, actuatable property, prdocedure
           Returns:
               actuator object: instantiated with actuator  properties
        """
        self.actuator_id = BNode()
        self.platform_id = BNode()
        self.label = Literal(args[0])
        self.comment = Literal(args[1])
        self.actuatableProperty = (args[2])
        self.procedure = Literal(args[3])

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
        """
        returns the actuator id
        """
        return self.actuator_id

    def set_actuator_id(self, actuator_id):
        """ setting actuator id
           Args:
               *actuator_id (str): the actuator id to be set to the actuator object
           Returns:
               actuator object: with the set actuator id
        """
        self.actuator_id = actuator_id


    def add_procedure(self, pro):
        """
        takes a procedure and adds the procedure to the graph
        """
        if isinstance(pro, Procedure):
            obsgraph.add((self.actuator_id, cfg.sosa.observes, pro.label))


    def add_actuatableProperty(self, actProp):
        """
        add a single  actuableProperty
        """
        if isinstance(actProp, ActuatableProperty):
            obsgraph.add((self.actuator_id, cfg.sosa.observes, actProp.label))


    def add_actuation(self, actuation):
        """
        add actuation
        """
        a_uri = actuation.get_uri()
        if isinstance(actuation, Actuation):
            obsgraph.add((self.actuator_id, cfg.sosa.madeActuation, a_uri))
            self.actuations.append(a_uri)

