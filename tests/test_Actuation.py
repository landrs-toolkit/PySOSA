import unittest
from PySOSA import Actuation
from PySOSA import FeatureOfInterest

class MyTestCase(unittest.TestCase):


    def test_add_featureOfInterest(self):
        """
        creates an FOI object and test add feature of interest to Actuation
        """
        a1 = Actuation("Actuation 1", "switch on thermometer")
        feature = FeatureOfInterest("Feature 1", "temperature")
        a1.add_featureOfInterest(feature)

if __name__ == '__main__':
        unittest.main()
