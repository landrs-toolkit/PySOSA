from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Actuation(object):
    """
    An Actuation carries out an (Actuation) Procedure to change the state of the world using an Actuator.
    """

    def __init__(self,label,comment):
        self.actuation_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal(datetime)
        self.simpleResult = Literal

        obsgraph.add((self.actuation_id, RDF.type, cfg.sosa.Actuation))
        obsgraph.add((self.actuation_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuation_id, RDFS.label, self.label))
        obsgraph.add((self.actuation_id, cfg.sosa.datetime, self.dateTime))
        #obsgraph.add((self.actuation_id, cfg.sosa.hasSimpleResult, self.simpleResult))

    #get actuation id
    def get_uri(self):
        return self.actuation_id

    #set result time
    def set_date_time(self, dateTime):
        self.dateTime = dateTime

    # get result time
    def get_date_time(self):
        return self.dateTime

    #set simple result
    def set_simple_Result(self, simpleResult):
        self.simpleResult = simpleResult

    # get simple result
    def get_simple_Result(self):
        return self.simpleResult

    #add feature of interest
    def add_featureOfInterest(self, FeatureOfInterest):
        f_uri = FeatureOfInterest.get_uri()
        obsgraph.add((self.actuation_id, cfg.sosa.hasFeatureOfInterest, f_uri))

