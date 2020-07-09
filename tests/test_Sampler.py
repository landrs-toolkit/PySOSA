import unittest

from PySOSA import config as cfg
from PySOSA.Actuator import Actuator
from PySOSA.ObservableProperty import ObservableProperty
from PySOSA.Platform import Platform
from PySOSA.Procedure import Procedure
from PySOSA.Sensor import Sensor


class MyTestCase(unittest.TestCase):



    def test_create_platfrom(self):
        """
        creates platform, procedure, sensor, Acturator , observable property objects
        tests adding these to the platform and printing the graph
        shows actuators and sensors attached to the platform on the rdf graph
        """
        # procedure object
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
        obsList2 =[obs1,obs2]
        # sensor object
        s1 = Sensor("Sensor 1", "first sensor", obsList, proList)
        s2 = Sensor("Sensor 2", "second sensor", obsList2, proList)
        s3 = Sensor("Sensor 3", "second sensor", obsList2, proList)
        act1 = Actuator("Actuator 1", "first actuator",[],[])
        act2 = Actuator("Actuator 2", "second actuator",[],[])
        act3 = Actuator("Actuator 3", "third actuator",[],[])
        #list of actuators
        actList =[act1,act2,act3]
        #list of sensors
        senList = [s1,s2]
        # platform object
        p1 = Platform("platform 1", "p1", senList, actList,[])
        p1.add_sensor(s3)

        this_graph = cfg.get_graph()
        #print(this_graph.serialize(format='turtle'))
        print(this_graph.serialize(format="ttl").decode('utf-8'))



    def test_add_sensor(self):
        """Test add a single sensor to platform method"""
        #empty platform
        p2 = Platform("platform 2", "p2", [], [], [])

        # procedure object
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
        s1 = Sensor("Sensor 1", "first sensor", obsList, proList)

        p2.add_sensor(s1)