from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier

# Add Graph obj
obsgraph = Graph()

def get_graph():
    return obsgraph

class Sensor(object):

    """
    Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure.
    Sensors respond to a Stimulus, e.g., a change in the environment, or Input data composed
    from the Results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.
    """

    observations = []

    #constructor
    def __init__(self, label,comment):
        self.label = Literal(label)
        self.comment = Literal(comment)
        self.sensor_id = BNode()
        self.obs_property = Literal
        obsgraph.add((self.sensor_id, RDF.type, cfg.sosa.Sensor))
        obsgraph.add((self.sensor_id, RDFS.comment, self.comment))
        obsgraph.add((self.sensor_id, RDFS.label, self.label))

    #set sensor id
    def set_sensor_id(self, sensor_id):
        self.sensor_id = sensor_id

    #get sensor id
    def get_uri(self):
        return self.sensor_id

    #add observable property

    def add_obs_property(self, ObservableProperty):
        a_uri = ObservableProperty.get_uri()
        obsgraph.add((self.sensor_id, cfg.sosa.observes, a_uri))

    #add procedure
    def add_procedure(self,Procedure):
        p_uri = Procedure.get_uri()
        obsgraph.add((self.sensor_id, cfg.sosa.implements, p_uri))

    #define platfrom that hosts sensor
    def add_platform(self,Platform):
        pl_uri = Platform.get_uri()
        obsgraph.add((self.sensor_id, cfg.sosa.isHostedBy, pl_uri))

    #define observation
    def add_observation(self,Observation):
        o_uri=Observation.get_uri()
        obsgraph.add((self.sensor_id, cfg.sosa.madeObservation, o_uri))
        self.observations.append(Observation)

