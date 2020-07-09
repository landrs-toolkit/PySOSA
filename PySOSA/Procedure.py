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
        """ instantiating Procedure object
              Args:
                  label, comment (literal): label and comment for the procedure
              Returns:
                  procedure (str): representing a workflow to carry out
        """
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
        """
        setting procedure id
        """
        self.procedure_id = procedure_id


    def get_uri(self):
        """
        get procedure id
        """
        return self.procedure_id


    def set_procedure_input(self, input):
        """
        set procedure input
        """
        self.input = input


    def get_input(self):
        """
        get procedure input of a procedure
        """
        return self.input


    def set_procedure_output(self, output):
        """
        set the output of the procedure
        """
        self.output = output


    def get_output(self):
        """
        get the output of the procedure
        """
        return self.output
