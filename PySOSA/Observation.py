from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Observation(object):


    def __init__(self, label, comment):
        self.comment = Literal(comment)
        self.label = Literal(label)
        self.observation_id = BNode()
        self.dateTime = Literal(datetime)
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
