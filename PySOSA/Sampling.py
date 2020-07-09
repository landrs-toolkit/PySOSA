from datetime import datetime

from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Sampling(object):
    """
     Creates a sampling object representing a SOSA sampling
     An act of Sampling carries out a (Sampling) Procedure to create or transform one or more Samples.
    """

    def __init__(self,label,comment):
        """ instantiating Sampling object (procedure)
            Args:
                label, comment (literal): label and comment for the sampling procedure
            Returns:
                sampling object (str): with attributes for carrying out a sampling
        """
        self.sampling_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.dateTime = Literal(datetime)
        self.simpleResult = Literal

        obsgraph.add((self.sampling_id, RDF.type, cfg.sosa.Sampling))
        obsgraph.add((self.sampling_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampling_id, RDFS.label, self.label))
        obsgraph.add((self.sampling_id, cfg.sosa.datetime, self.dateTime))

    def get_uri(self):
        """
        get sampling id
        """
        return self.sampling_id


    def add_featureOfInterest(self, FeatureOfInterest):
        """
        add feature of Interest
        """
        f_uri = FeatureOfInterest.get_uri()
        obsgraph.add((self.sampling_id, cfg.sosa.hasFeatureOfInterest, f_uri))


