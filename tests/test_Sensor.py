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
