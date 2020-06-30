import unittest
from PySOSA import Actuation
from PySOSA import FeatureOfInterest

class MyTestCase(unittest.TestCase):

#Test add feature of interest to Actuation
    def test_add_featureOfInterest(self):
        a1 = Actuation("Actuation 1", "switch on thermometer")
        feature = FeatureOfInterest("Feature 1", "temperature")
        a1.add_featureOfInterest(feature)

if __name__ == '__main__':
        unittest.main()
