import unittest
from PySOSA import config as cfg
from PySOSA.Platform import Platform
from PySOSA import ObservationCollection

class MyTestCase(unittest.TestCase):

    def test_add_sensor(self):
        """
        test add sensor to the graph
        """
        obs = ObservationCollection(comment="mycol")
        obs = Platform(comment="mycol")
        this_graph = cfg.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_remove_sensor(self):
        """
        test remove sensor from the global graph
        """
        obs = ObservationCollection(comment='mycol2')
        this_graph = cfg.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_Observation(self):
        """
        creates an observation object and tests this observation on the graph
        """
        obs = ObservationCollection(comment="mycol")
        this_graph = cfg.get_graph()
        print(this_graph.serialize(format='turtle'))


    def test_Sensor(self):
        """
        creates a sensor object and test that sensor object
        """
        obs = ObservationCollection(comment='mycol3')
        this_graph = cfg.get_graph()
        print(this_graph.serialize(format='turtle'))


if __name__ == '__main__':
    unittest.main()


