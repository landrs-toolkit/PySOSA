import unittest

import pyobs


class MyTestCase(unittest.TestCase):


    """Test add sensor to platform method"""

    def test_add_sensor(self):
        # platform object
        p1 = pyobs.Platform("platform 1", "p1")
        # sensor objects
        s1 = pyobs.Sensor("Sensor 1", "first sensor")
        s2 = pyobs.Sensor("Sensor 2", "second sensor")
        s3 = pyobs.Sensor("Sensor 3", "third sensor")

        #add sensors to platform 1
        p1.add_sensor(s1)
        p1.add_sensor(s2)
        p1.add_sensor(s3)

        this_graph = pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))


        #Test add actuator to platform method

    def test_add_actuator(self):
        # platform object
        p1 = pyobs.Platform("platform 1", "p1")
        # actuator objects
        act1 = pyobs.Actuator("Actuator 1", "first actuator")
        act2 = pyobs.Actuator("Actuator 2", "second actuator")
        act3 = pyobs.Actuator("Actuator 3", "third actuator")

        # add actuators to platform 1
        p1.add_actuator(act1)
        p1.add_actuator(act2)
        p1.add_actuator(act3)

        # Test add sampler to platform method

    def test_add_sampler(self):
         # platform object
        p1 = pyobs.Platform("platform 1", "p1")
        # sampler objects
        sam1 = pyobs.Sampler("Sampler 1", "first sampler")
        sam2 = pyobs.Sampler("Sampler 2", "second sampler")
        sam3 = pyobs.Sampler("Sampler 3", "third sampler")

        # add actuators to platform 1
        p1.add_sampler(sam1)
        p1.add_sampler(sam2)
        p1.add_sampler(sam3)