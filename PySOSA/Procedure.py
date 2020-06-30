from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Procedure(object):
    """
    Creates a Procedure object representing a SOSA procedure
    Procedure - A workflow, protocol, plan, algorithm, or computational method specifying how to make an Observation,
    create a Sample, or make a change to the state of the world (via an Actuator).
    """

    def __init__(self, comment, label):
        self.procedure_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.input = BNode()
        self.output = BNode()

        obsgraph.add((self.procedure_id, RDF.type, cfg.sosa.Procedure))
        obsgraph.add((self.procedure_id, RDFS.comment, self.comment))
        obsgraph.add((self.procedure_id, RDFS.label, self.label))
        obsgraph.add((self.procedure_id, cfg.sosa.hasInput, self.input))
        obsgraph.add((self.procedure_id, cfg.sosa.hasOutput, self.output))

    #set procedure id
    def set_procedure_id(self, procedure_id):
        self.procedure_id = procedure_id

    #get procedure id
    def get_uri(self):
        return self.procedure_id

    # set procedure input
    def set_procedure_input(self, input):
        self.input = input

    # get procedure input
    def get_input(self):
        return self.input

        # set procedure output
    def set_procedure_output(self, output):
        self.output = output

        # get procedure output
    def get_output(self):
        return self.output
