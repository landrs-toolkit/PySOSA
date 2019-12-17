from pyobs import pyobs
import rdflib


def test_Observation():
    obs = pyobs.ObservationCollection(comment="mycol")
    this_graph = pyobs.get_graph()
    print(this_graph.serialize(format='turtle'))

if __name__ == '__main__':
    test_Observation()