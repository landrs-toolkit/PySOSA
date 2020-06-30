import unittest
from PySOSA import Actuation
from PySOSA import  Actuator
from PySOSA import ActuatableProperty
from PySOSA import Sampling, Sampler


class MyTestCase(unittest.TestCase):

# Test add actuation  to actuator
    def test_add_actuation(self):
        a1 = Actuation("Actuation 1", "switch on thermometer")
        act1 = Actuator("Actuator 1", "first actuator")
        act1.add_actuation(a1)

#Test add actuatable property to actuator
    def test_add_actuatableProperty(self):
        actProp = ActuatableProperty("ActuatableProperty1","temperature")
        act1 = Actuator("Actuator 1", "first actuator")
        act1.add_actuatableProperty(actProp)

# Test add sampling to sampler
    def test_add_sampling(self):
        sampl1 = Sampling("Sampling 1", "first sampling")
        sam1 = Sampler("Sampler 1", "first sampler")
        sam1.add_sampling(sampl1)


if __name__ == '__main__':
    unittest.main()