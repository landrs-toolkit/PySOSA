import unittest
from PySOSA.Platform import Platform
from PySOSA.Sensor import Sensor
from PySOSA.Sampler import Sampler
from PySOSA.Actuator import Actuator
from PySOSA import PySOSA

class MyTestCase(unittest.TestCase):

    """Test add sensor to platform method"""

    def test_add_sensor(self):
        # platform object
        p1 = Platform("platform 1", "p1")
        # sensor objects
        s1 = Sensor("Sensor 1", "first sensor")
        s2 = Sensor("Sensor 2", "second sensor")
        s3 = Sensor("Sensor 3", "third sensor")

        #add sensors to platform 1
        p1.add_sensor(s1)
        p1.add_sensor(s2)
        p1.add_sensor(s3)

        this_graph = PySOSA.get_graph()
        print(this_graph.serialize(format='turtle'))


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