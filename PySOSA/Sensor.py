from PySOSA import config as cfg
from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS
from datetime import datetime
from rdflib.term import Identifier
from PySOSA.ObservableProperty import ObservableProperty
from PySOSA.Procedure import Procedure
from PySOSA.Observation import Observation

# Add Graph obj
obsgraph = cfg.get_graph()

class Sensor(object):

    """
    Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure.
    Sensors respond to a Stimulus, e.g., a change in the environment, or Input data composed
    from the Results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.
    """

    observations = []
    observableProps =[]

    #constructor parameters- label,comment, list of observable properties and list of procedures
    def __init__(self, *args):
        self.sensor_id = BNode()
        self.label = Literal(args[0])
        self.comment = Literal(args[1])
        self.observableProperty = (args[2])
        self.procedure = (args[3])
        obsgraph.add((self.sensor_id, RDF.type,  cfg.sosa.Sensor))
        obsgraph.add((self.sensor_id, RDFS.comment, self.comment))
        obsgraph.add((self.sensor_id, RDFS.label, self.label))
        # add list of observable properties
        for obs in self.observableProperty:
            if isinstance(obs, ObservableProperty):
                obsgraph.add((self.sensor_id,  cfg.sosa.observes, obs.label))
        for pro in self.procedure:
            if isinstance(pro, Procedure):
                obsgraph.add((self.sensor_id,  cfg.sosa.implements, pro.label))

    #set sensor id
    def set_sensor_id(self, sensor_id):
        self.sensor_id = sensor_id

    #get sensor id
    def get_uri(self):
        return self.sensor_id

    #add  a single observable property

    def add_obs_property(self, obsProp):
        if isinstance(obsProp, ObservableProperty):
            a_uri = obsProp.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.observes,obsProp.label ))

    #add  a single procedure
    def add_procedure(self,proc):
        if isinstance(proc, Procedure):
            p_uri = proc.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.implements, proc.label))

    #add observation

    def add_observation(self, obs):
        if isinstance(obs, Observation):
            o_uri = obs.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.madeObservation, obs.label))
            self.observations.append(Observation)

        # return list of observations

    def get_observation_list(self):
        return self.observations

