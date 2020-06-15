import unittest
from PySOSA import config as cfg
from PySOSA import PySOSA
from PySOSA.Platform import Platform
from PySOSA.Sensor import Sensor
from PySOSA.Sampler import Sampler
from PySOSA.Actuator import Actuator
from PySOSA.Procedure import Procedure
from PySOSA.ObservableProperty import ObservableProperty
from PySOSA.Observation import Observation

class MyTestCase(unittest.TestCase):

    #Test adding observable property to sensor

    def test_set_procedure_id(self):
        procedure_id = "UND2020"
        proc1 = Procedure("procedure 1", "proc1", "Sensor calibration proc", "procedureInput", "procedureOutput")
        proc2 = Procedure("procedure 2", "proc2", "Sensor calibration proc", "procedureInput", "procedureOutput")
        # list of procedures
        proList = [proc1, proc2]
        # observable property object
        obs1 = ObservableProperty("obs-property1", "obs-property")
        obs2 = ObservableProperty("obs-property2", "obs-property2")
        obs3 = ObservableProperty("obs-property3", "obs-property3")
        # list of observable properties
        obsList = [obs1, obs2]
        s4 = Sensor("Sensor 4", "fourth sensor", obsList, proList)
        obs4 = ObservableProperty("temperature","property 1")
        s4.add_obs_property(obs4)

    #Test adding procedure to sensor

    def test_add_procedure(self):
        proc1 = Procedure("procedure 1", "proc1")
        proc2 = Procedure("procedure 2", "proc2")
        # list of procedures
        proList = [proc1, proc2]
        # observable property object
        obs1 = ObservableProperty("obs-property1", "obs-property")
        obs2 = ObservableProperty("obs-property2", "obs-property2")
        obs3 = ObservableProperty("obs-property3", "obs-property3")
        # list of observable properties
        obsList = [obs1, obs2]

        # sensor object
        s5 = Sensor("Sensor 5", "fifth sensor", obsList, proList)
        proc3 = Procedure("Procedure 1","setting height of temperature sensor")
        #add procedure
        s5.add_procedure(proc3)

    # test to add observation to  sensor
    def test_add_observation(self):
        s6 = Sensor("Sensor 6", "sixth sensor", [], [])
        obs1 = Observation("Observation 1", "measuring temperature")
        s6.add_observation(obs1)


        this_graph = cfg.get_graph()
        # print(this_graph.serialize(format='turtle'))
        print(this_graph.serialize(format="ttl").decode('utf-8'))
