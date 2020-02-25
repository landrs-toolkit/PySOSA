import unittest

import pyobs_pyobs
import rdflib
from rdflib import Graph, URIRef, Literal

import pyobs_pyobs
import rdflib



class MyTestCase(unittest.TestCase):

    def test_add_sensor(self):

        obs = pyobs_pyobs.ObservationCollection(comment="mycol")

        obs = pyobs_pyobs.Platform(comment="mycol")

        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_remove_sensor(self):
        obs = pyobs_pyobs.ObservationCollection(comment='mycol2')
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))

    def test_Observation(self):
        obs = pyobs_pyobs.ObservationCollection(comment="mycol")
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))


    def test_Sensor(self):
        obs = pyobs_pyobs.ObservationCollection(comment='mycol3')
        this_graph = pyobs_pyobs.get_graph()
        print(this_graph.serialize(format='turtle'))


if __name__ == '__main__':
    unittest.main()


