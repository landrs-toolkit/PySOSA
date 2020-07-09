from rdflib import Graph, BNode, Literal, RDF, RDFS

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class FeatureOfInterest(object):
    """
    Creates a feature of interest object representing SOSA FOI
    The thing whose property is being estimated or calculated in the course of an Observation
    to arrive at a Result, or whose property is being manipulated by an Actuator,
    or which is being sampled or transformed in an act of Sampling.
    """

    def __init__(self,label,comment):
        """ constructor for Feature of Interest
           Args:
               label, comment (literal): label and comment for the feature of interest
           Returns:
               FOI object: instantiated with feature_of_interest_id, label and comment
        """
        self.feature_of_interest_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

    def get_uri(self):
        """
        get uri of a feature of interest
        """
        return self.feature_of_interest_id
        obsgraph.add((self.feature_of_interest_id, RDF.type, sosa.FeatureOfInterest))
        obsgraph.add((self.feature_of_interest_id, RDFS.comment, self.comment))
        obsgraph.add((self.feature_of_interest_id, RDFS.label, self.label))

