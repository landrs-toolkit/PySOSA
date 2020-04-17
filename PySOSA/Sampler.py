from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Sampler(object):
    """
     A device that is used by, or implements, a (Sampling) Procedure to create or transform one or more samples.
    """
    samplings = []

    def __init__(self,label,comment):
        self.sampler_id = BNode()
        self.label = Literal(label)
        self.comment = Literal(comment)


        obsgraph.add((self.sampler_id, RDF.type, cfg.sosa.Sampler))
        obsgraph.add((self.sampler_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampler_id, RDFS.label, self.label))

    def get_uri(self):
        return self.sampler_id

    def set_sampler_id(self, sampler_id):
        self.sampler_id = sampler_id
    #add procedure
    def add_procedure(self, Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.sampler_id, cfg.sosa.implements, p_uri))
    #add sampling
    def add_sampling(self, Sampling):
        a_uri = Sampling.get_uri()
        obsgraph.add((self.sampler_id, cfg.sosa.madeSampling, a_uri))
        self.samplings.append(a_uri)
