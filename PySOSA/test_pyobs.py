import pyobs_pyobs

import pyobs_pyobs


import rdflib


def test_Observation():
    obs = pyobs_pyobs.ObservationCollection(comment="mycol")
    this_graph = pyobs_pyobs.get_graph()
    print(this_graph.serialize(format='turtle'))


if __name__ == '__main__':
    test_Observation()
