from rdflib import BNode, Literal, RDF, RDFS
from PySOSA import config as cfg
from PySOSA.ObservableProperty import ObservableProperty
from PySOSA.Observation import Observation
from PySOSA.Procedure import Procedure

# Add Graph obj
obsgraph = cfg.get_graph()

class Sensor(object):

    """
    Creates a Sensor object representing a SOSA sensor
    Device, agent (including humans), or software (simulation) involved in, or implementing, a Procedure.
    Sensors respond to a Stimulus, e.g., a change in the environment, or Input data composed
    from the Results of prior Observations, and generate a Result. Sensors can be hosted by Platforms.
    """

    observations = []
    observableProps = []

    def __init__(self, *args):
        """ instantiating Sensor object
           Args:
               *args (str): label, comment, observable property, implementsPrdocedure
               sensor object can be instantiated with multiple arguments
           Returns:
               sensor object: an instantiated sensor object with sensor id, label,comment and other properties
        """
        self.sensor_id = BNode()
        self.platform_id = BNode()
        self.label = Literal(args[0])
        self.comment = Literal(args[1])
        self.observableProperty = args[2]
        self.implements_procedure = (args[3])
        obsgraph.add((self.sensor_id, RDF.type,  cfg.sosa.Sensor))
        obsgraph.add((self.sensor_id, RDFS.comment, self.comment))
        obsgraph.add((self.sensor_id, RDFS.label, self.label))
        # add list of observable properties
        for obs in self.observableProperty:
            if isinstance(obs, ObservableProperty):
                obsgraph.add((self.sensor_id,  cfg.sosa.observes, obs.label))
        for pro in self.implements_procedure:
            if isinstance(pro, Procedure):
                obsgraph.add((self.sensor_id,  cfg.sosa.implements, pro.label))


    def set_sensor_id(self, sensor_id):
        """ setting a sensor id
           Args:
               sensor_id (str): the id to uniquely identify the sensor
           Returns:
               sensor object: with a set sensor id
        """
        self.sensor_id = sensor_id


    def get_uri(self):
        """
        get sensor id
        """
        return self.sensor_id

    def add_obs_property(self, obsProp):
        """ add sensor's observable property
           Args:
               obsProp (str): the observable property to be added
           Returns:
               sensor object: with an observable property
        """
        if isinstance(obsProp, ObservableProperty):
            a_uri = obsProp.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.observes,obsProp.label ))

    def add_procedure(self,proc):
        """ add procedure
           Args:
               *proc (str): the procedure to be added
           Returns:
               sensor object: adds the procdure to the sensor and to the obsgraph
        """
        if isinstance(proc, Procedure):
            p_uri = proc.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.implements, proc.label))


    def add_observation(self, obs):
        """ add an observation to the sensor object
               Args:
                   *obs (str): the observation to be performed and added to the obsgraph
               Returns:
                   sensor object: with an observation or list of observations
        """
        if isinstance(obs, Observation):
            o_uri = obs.get_uri()
            obsgraph.add((self.sensor_id, cfg.sosa.madeObservation, obs.label))
            self.observations.append(Observation)

        # return list of observations

    def get_observation_list(self):
        """ get observations list
        returns a list of observations
        """
        return self.observations

