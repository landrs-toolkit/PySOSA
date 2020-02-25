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

    #Test adding observable property to sensor

    def test_add_observable_property(self):
        s1 = pyobs.Sensor("Sensor 1", "first sensor")
        obs1 = pyobs.ObservableProperty("temperature","property 1")
        s1.add_obs_property(obs1)

    #Test adding procedure to sensor

    def test_add_procedure(self):
        s1 = pyobs.Sensor("Sensor 1", "first sensor")
        pro1 = pyobs.Procedure("Procedure 1","setting height of temperature sensor")
        s1.add_procedure(pro1)

    # test to define a sensor'platform

    def test_add_platform(self):
        s1 = pyobs.Sensor("Sensor 1", "first sensor")
        p1 = pyobs.Platform("platform 1", "p1")
        s1.add_platform(p1)

    # test to add observation to  sensor

    def test_add_observation(self):
        s1 = pyobs.Sensor("Sensor 1", "first sensor")
        obs1 = pyobs.Observation("Observation 1", "measuring temperature")
        s1.add_observation(obs1)

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

    #Test add feature of interest to Actuation
    def test_add_featureOfInterest(self):
        a1 = pyobs.Actuation("Actuation 1", "switch on thermometer")
        feature = pyobs.FeatureOfInterest("Feature 1", "temperature")
        a1.add_featureOfInterest(feature)

    #Test add actuatable property to actuator
    def test_add_actuatableProperty(self):
        actProp = pyobs.ActuatableProperty("ActuatableProperty1","temperature")
        act1 = pyobs.Actuator("Actuator 1", "first actuator")
        act1.add_actuatableProperty(actProp)

    # Test add actuation  to actuator
    def test_add_actuation(self):
        a1 = pyobs.Actuation("Actuation 1", "switch on thermometer")
        act1 = pyobs.Actuator("Actuator 1", "first actuator")
        act1.add_actuation(a1)

    # Test add sampling to sampler
    def test_add_sampling(self):
        sampl1 = pyobs.Sampling("Sampling 1", "first sampling")
        sam1 = pyobs.Sampler("Sampler 1", "first sampler")
        sam1.add_sampling(sampl1)




"""Test delete sensor from platform method
    def test_delete_sensor(self):
            # platform object
            p1 = pyobs.Platform("platform 1", "p1")
            # observable property object
            obprop1 = pyobs.ObservableProperty("air speeed", " observes the speed of air")
            # procedure object
            pro1 = pyobs.Procedure("procedure 1", "pro 1")
            # sensor object
            s1 = pyobs.Sensor("Sensor1", "S1", p1.platform_id, obprop1.property_id, pro1.procedure_id)
            # add sensor 1 to platform 1
            #p1.add_sensor(s1)
            #p1.remove_sensor(s1)
           # this_graph = pyobs.get_graph()
           # print(this_graph.serialize(format='turtle'))
    Test add actuator to platform method
    def test_add_actuator(self):
        # platform object
        p1 = pyobs.Platform("platform 1", "p1")
        # observable property object
        feature1 = pyobs.FeatureOfInterst("Feature1", "air")
        # procedure object
        pro1 = pyobs.Procedure("procedure 1", "pro 1")
        # Actuation object
        act1 = pyobs.Actuation("Actuation1", "air actuation", "10 Feb 2020", "blow", feature1)
        # add sensor 1 to platform 1
        this_graph = pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))
"""



if __name__ == '__main__':
        unittest.main()