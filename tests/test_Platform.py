import unittest
from PySOSA import config as cfg
from PySOSA import PySOSA
from PySOSA.Platform import Platform
from PySOSA.Sensor import Sensor
from PySOSA.Sampler import Sampler
from PySOSA.Actuator import Actuator
from PySOSA.Procedure import Procedure
from PySOSA.ObservableProperty import ObservableProperty

class MyTestCase(unittest.TestCase):

    """Test add sensor to platform method"""

    def test_add_sensor(self):
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



        act1 = Actuator("Actuator 1", "first actuator")
        act2 = Actuator("Actuator 2", "second actuator")
        act3 = Actuator("Actuator 3", "third actuator")
        #list of actuators
        actList =[act1,act2,act3]
        #list of sensors
        senList = [s1,s2]
        #list of list
        addOns = []
        addOns.insert(0,senList)
        addOns.insert(1,actList)
        addOns.insert(2,[])

        # platform object
        p1 = Platform("platform 1", "p1",addOns)

        this_graph = cfg.get_graph()
        #print(this_graph.serialize(format='turtle'))
        print(this_graph.serialize(format="ttl").decode('utf-8'))

"""
        #Test add actuator to platform method

    def test_add_actuator(self):
        # platform object
        p1 = Platform("platform 1", "p1")
        # actuator objects
        act1 = Actuator("Actuator 1", "first actuator")
        act2 = Actuator("Actuator 2", "second actuator")
        act3 = Actuator("Actuator 3", "third actuator")

        # add actuators to platform 1
        p1.add_actuator(act1)
        p1.add_actuator(act2)
        p1.add_actuator(act3)

        # Test add sampler to platform method

    def test_add_sampler(self):
         # platform object
        p1 = Platform("platform 1", "p1")
        # sampler objects
        sam1 = Sampler("Sampler 1", "first sampler")
        sam2 = Sampler("Sampler 2", "second sampler")
        sam3 = Sampler("Sampler 3", "third sampler")

        # add actuators to platform 1
        p1.add_sampler(sam1)
        p1.add_sampler(sam2)
        p1.add_sampler(sam3)
"""