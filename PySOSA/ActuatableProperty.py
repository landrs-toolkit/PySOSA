from rdflib import Graph, BNode, Literal, RDF, RDFS

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class ActuatableProperty(object):
    """
    Creating an Actuatable Property object that represents a SOSA Actuable Property
    An actuatable quality (property, characteristic) of a FeatureOfInterest.
    """

    def __init__(self,label,comment):
        self.actuatable_property_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.actuatable_property_id, RDF.type, sosa.ActuatableProperty))
        obsgraph.add((self.actuatable_property_id, RDFS.comment, self.comment))
        obsgraph.add((self.actuatable_property_id, RDFS.label, self.label))

    def get_uri(self):
            return self.actuatable_property_id
