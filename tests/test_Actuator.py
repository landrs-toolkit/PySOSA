import unittest

import pyobs


class MyTestCase(unittest.TestCase):

# Test add actuation  to actuator
    def test_add_actuation(self):
        a1 = pyobs.Actuation("Actuation 1", "switch on thermometer")
        act1 = pyobs.Actuator("Actuator 1", "first actuator")
        act1.add_actuation(a1)

#Test add actuatable property to actuator
    def test_add_actuatableProperty(self):
        actProp = pyobs.ActuatableProperty("ActuatableProperty1","temperature")
        act1 = pyobs.Actuator("Actuator 1", "first actuator")
        act1.add_actuatableProperty(actProp)

# Test add sampling to sampler
    def test_add_sampling(self):
        sampl1 = pyobs.Sampling("Sampling 1", "first sampling")
        sam1 = pyobs.Sampler("Sampler 1", "first sampler")
        sam1.add_sampling(sampl1)


if __name__ == '__main__':
    unittest.main()