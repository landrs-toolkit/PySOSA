from datetime import datetime

from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Observation(object):
    """
    Creates an Observation object that represents a SOSA observation
    Observation - Act of carrying out an (Observation) Procedure to estimate or calculate a value of a property of a FeatureOfInterest.
    Links to a Sensor to describe what made the Observation and how;
    """

    # def __init__(self, *args):
    #     self.observation_id = BNode()
    #     self.dateTime = Literal(datetime)
    #     self.feature_of_interest = Literal(args[0])
    #     self.comment = Literal(args[1])
    #     self.label = Literal(args[2])
    #     self.simpleResult = Literal(args[3])
    def __init__(self, label, comment):
        self.observation_id = BNode()
        self.dateTime = Literal(datetime)
        self.featureOfInterest = Literal
        self.comment = Literal(comment)
        self.label = Literal(label)
        self.simpleResult = Literal

        obsgraph.add((self.observation_id, RDF.type , cfg.sosa.Observation))
        obsgraph.add((self.observation_id, RDFS.comment, self.comment))
        obsgraph.add((self.observation_id, RDFS.label, self.label))
        obsgraph.add((self.observation_id, cfg.sosa.dateTime, self.dateTime))
        # To be fixed
       # obsgraph.add((self.observation_id, sosa.hasResult, self.simpleResult))

    def get_uri(self):
        return self.observation_id

    def set_dateTime(self, dateTime):
        self.dateTime = dateTime

    def set_simpleResult(self,simpleResult):
        self.simpleResult = simpleResult
