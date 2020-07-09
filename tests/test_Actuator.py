import unittest
from PySOSA import Actuation
from PySOSA import  Actuator
from PySOSA import ActuatableProperty
from PySOSA import Sampling, Sampler


class MyTestCase(unittest.TestCase):


    def test_add_actuation(self):
        """
        Test add actuation  to actuator
        """
        a1 = Actuation("Actuation 1", "switch on thermometer")
        act1 = Actuator("Actuator 1", "first actuator")
        act1.add_actuation(a1)


    def test_add_actuatableProperty(self):
        """
        Testing to add actuatable property to actuator
        """
        actProp = ActuatableProperty("ActuatableProperty1","temperature")
        act1 = Actuator("Actuator 1", "first actuator")
        act1.add_actuatableProperty(actProp)


    def test_add_sampling(self):
        """
        Test add sampling to sampler
        """
        sampl1 = Sampling("Sampling 1", "first sampling")
        sam1 = Sampler("Sampler 1", "first sampler")
        sam1.add_sampling(sampl1)


if __name__ == '__main__':
    unittest.main()