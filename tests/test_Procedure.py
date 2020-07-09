import unittest

from PySOSA.ObservableProperty import ObservableProperty
from PySOSA.Procedure import Procedure
from PySOSA.Sensor import Sensor


class MyTestCase(unittest.TestCase):

    #Test setting procedure_id to sensor

    def test_set_procedure_id(self):
        """
        creates a procedure object and test setting that procedure's id
        """
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



    def test_add_procedure(self):
        """
        Test adding procedure to sensor
        """
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


