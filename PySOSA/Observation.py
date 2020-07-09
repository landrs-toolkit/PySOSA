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

    def __init__(self, label, comment):
        """ instantiating Observation object
             Args:
                 label, comment (literal): label and comment for the observation carried out
             Returns:
                 an observation: initialized with observation_id, FOI, dateTime, simple result, label and comment
          """
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
        """
        get observation id
        """
        return self.observation_id

    def set_dateTime(self, dateTime):
        """
        set the date time for the observation
        """
        self.dateTime = dateTime

    def set_simpleResult(self,simpleResult):
        """
        set observation simple result
        """
        self.simpleResult = simpleResult
