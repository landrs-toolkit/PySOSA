LANDRS PySOSA Documentation!
==================================

Introduction
==================================
PySOSA is a python module for building SOSA based RDF graphs

The LANDRS (Linked And Networked DRoneS) project amongst other things works to create an ontology and building an OpenAPI specification for creating a Restful API for building linked data native drone data applications. LANDRS is a Sloan Foundation funded project to build open source APIs for managing scientific data on drones through the use of web standards and linked data technologies.

PySOSA Guide
==================================
 Here is the guide to use PySOSA: https://github.com/landrs-toolkit/PySOSA

For testing PySOSA:  
$ python -m unittest test_Platform.py

PySOSA Modules & Classes
==================================
1. Platform: descr
2. Sensor: description
3. Observation:
4. ObservableProperty
5. Actuator
6. ActuatableProperty
7. Sampler
8. FeatureofInterest


Example of PySOSA Features
==================================

Some functions you can invoke on the Platform class->
This is how you would add a sensor to the Platform
 adding a sensor to a Platform:
   takes self and a sensor object, adds to the graph

    def add_sensor(self, sensor):
        # check if it is a sensor before adding
        if isinstance(sensor, Sensor):
            # add sensor to list
            self.sensors.append(sensor)
            # add sensor to rdf graph
            obsgraph.add((self.platform_id, cfg.sosa.hosts, sensor.label))
        else:
            raise Exception('Type error: object not of type Sensor')

Contributing
==================================

When contributing to this repository, please first discuss the change you wish to make via an issue, email, or any other method with the maintainers of this repository before making a change.

See a summary of instructions to guide how you can contribute.

1. Fork the Project repo 
2. Create your Feature Branch (git checkout -b feature/AmazingFeature)
3. Commit your Changes (git commit -m 'Add some AmazingFeature')
4. Push to the Branch (git push origin feature/AmazingFeature)
5. Open a Pull Request
6. You can also get in touch via email landrs@nd.edu or visit https://www.landrs.org/



Usage | How to install from Pypi
==================================
    Pre Requisites. Before using, you must have the following:
    Installation. Install using pip: pip install pysosa Link to pysosa pypi
    Configuration. Configure all connection parameters on the IDE
    Downloading the code! Run Your function
    Checking your recently installed package.


License
Apache 2.0

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   License
   README.md
   


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
