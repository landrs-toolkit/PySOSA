from datetime import datetime

from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Actuation(object):
    """
    An Actuation carries out an (Actuation) Procedure to change the state of the world using an Actuator.
    """

    def __init__(self,label,comment):
        """ instantiating Actuation object representing SOSA actuation
           Args:
               label, comment (literal): label and comment for the actuation
           Returns:
               actuation object: instantiated with actuation  properties
        """
        self.actuation_id = BNode()
        self.featureOfInterest = Literal
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal(datetime)
        self.simpleResult = Literal

        obsgraph.add((self.actuation_id, RDF.type, cfg.sosa.Actuation))
        obsgraph.add((self.actuation_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuation_id, RDFS.label, self.label))
        obsgraph.add((self.actuation_id, cfg.sosa.datetime, self.dateTime))



    def get_uri(self):
        """
        get actuation id
        """
        return self.actuation_id


    def set_date_time(self, dateTime):
        """
        set date time
        """
        self.dateTime = dateTime


    def get_date_time(self):
        """
        get result time
        """
        return self.dateTime


    def set_simple_Result(self, simpleResult):
        """
        set simple result
        """
        self.simpleResult = simpleResult


    def get_simple_Result(self):
        """
        get simple result
        """
        return self.simpleResult


    def add_featureOfInterest(self, FeatureOfInterest):
        """
        add feature of interest
        """
        f_uri = FeatureOfInterest.get_uri()
        obsgraph.add((self.actuation_id, cfg.sosa.hasFeatureOfInterest, f_uri))

