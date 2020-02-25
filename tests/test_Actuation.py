import unittest

import pyobs


class MyTestCase(unittest.TestCase):


#Test add feature of interest to Actuation
    def test_add_featureOfInterest(self):
        a1 = pyobs.Actuation("Actuation 1", "switch on thermometer")
        feature = pyobs.FeatureOfInterest("Feature 1", "temperature")
        a1.add_featureOfInterest(feature)

if __name__ == '__main__':
        unittest.main()
