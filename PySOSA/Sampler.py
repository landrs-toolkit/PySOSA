from rdflib import Graph, BNode, Literal, RDF, RDFS

from PySOSA import config as cfg

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Sampler(object):
    """
     A sampler object representing a SOSA sampler
     A device that is used by, or implements, a (Sampling) Procedure to create or transform one or more samples.
    """
    samplings = []

    def __init__(self,label,comment):
        self.sampler_id = BNode()
        self.platform_id = BNode()
        self.detects = Literal
        self.implements_procedure = Literal
        self.label = Literal(label)
        self.comment = Literal(comment)

        obsgraph.add((self.sampler_id, RDF.type, cfg.sosa.Sampler))
        obsgraph.add((self.sampler_id, RDFS.comment, self.comment))
        obsgraph.add((self.sampler_id, RDFS.label, self.label))

    def set_sampler_id(self, sampler_id):
        self.sampler_id = sampler_id

    def set_platform_id(self, platform_id):
        self.platform_id = platform_id

    def remove_platform_id(self, Sampler):
        sampler_uri = Sampler.get_uri()
        self.samplings.remove(Sampler.platform_id)
        obsgraph.remove((self.platform_id, cfg.sosa.hosts, sampler_uri))

    def set_sensor_id(self, sensor_id):
        self.sensor_id = sensor_id

    def get_uri(self):
        return self.sampler_id

    #add procedure
    def add_procedure(self, Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.sampler_id, cfg.sosa.implements, p_uri))
    #add sampling
    def add_sampling(self, Sampling):
        a_uri = Sampling.get_uri()
        obsgraph.add((self.sampler_id, cfg.sosa.madeSampling, a_uri))
        self.samplings.append(a_uri)

    def get_uri(self):
        return self.sampler_id
