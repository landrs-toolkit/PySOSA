LANDRS PySOSA Documentation
==================================
Version 0.0.1

Last Updated 2020.07.09

Introduction
==================================
PySOSA is a python module for building SOSA based RDF graphs

The LANDRS (Linked And Networked DRoneS) project amongst other things works to create an ontology and building an OpenAPI specification for creating a Restful API for building linked data native drone data applications. LANDRS is a Sloan Foundation funded project to build open source APIs for managing scientific data on drones through the use of web standards and linked data technologies.

PySOSA Guide
==================================
Here is the guide to use PySOSA: https://github.com/landrs-toolkit/PySOSA

SOSA (Sensor, Observation, Sample, and Actuator) is a lightweight but self-contained core ontology for its elementary classes and properties.
You may find useful information on SOSA here https://www.w3.org/TR/vocab-ssn/#SOSAPlatform
PySOSA implementation was guided by the sosa resource shared above. 

For testing PySOSA:  
$ python -m unittest test_Platform.py

PySOSA Modules & Classes
==================================
Class : implementation link

1. Platform : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Platform.py
2. Sensor : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Sensor.py
3. Observation : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Observation.py 
4. Actuator : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Actuator.py
5. ActuatableProperty : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/ActuatableProperty.py
6. Sampler : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Sampler.py
7. FeatureofInterest : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/FeatureofInterest.py
8. Procedure: https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Procedure.py
9. Actuation : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Actuation.py
10. Sampling : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/Sampling.py
11. ObservableProperty : https://github.com/landrs-toolkit/PySOSA/blob/master/PySOSA/ObservableProperty.py

Example of PySOSA Features
==================================

Some functions you can invoke on the PySOSA modules:

    * set_Platform_id()
    * get_URI()
    * add_sensor()
    * remove_sensor()
    * add_Observation()
    * add_Actuator()
    * remove_actuator()
    * set_dateTime()

This is how you would add a sensor to the Platform

Adding a sensor to a Platform algorithm:


""" Add a sensor to the platform """

    Args:

        sensor (str): The sensor object

    Returns:

        str: a list of sensors, platform with sensors added to it
    

Python code snippet 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def add_sensor(self, sensor):

    #check if it is a sensor before adding

    if isinstance(sensor, Sensor):
        #add sensor to list

        self.sensors.append(sensor)

        #add sensor to rdf graph

        obsgraph.add((self.platform_id, cfg.sosa.hosts, sensor.label))

    else:

        raise Exception('Type error: object not of type Sensor')


How to Use PySOSA?
==================================

More details To Be Announced!

PySOSA is A python module for building RDF graphs using the W3C SOSA (Sensors, Observations, Samples, and Actuators) ontology. For more see https://github.com/landrs-toolkit/PySOSA. 
In short PySOSA implements a python-based Linked-Data API for Networked Drones.

1. Discover the SOSA Features
2. check out the PySOSA repo
3. clone the repo into your Pycharm IDE and run the tests



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


How to install from Pypi
==================================

Pre Requisites. Before using, you must have the following:
Installation. Install using pip: pip install pysosa Link to pysosa pypi
Configuration. Configure all connection parameters on the IDE
Downloading the code! Run Your function
Checking your recently installed package.


License
==================================

PySOSA is published openly under Apache 2.0 https://www.apache.org/licenses/LICENSE-2.0

Contacts
==================================

* Get in touch with us on the landrs website https://www.landrs.org/
* Email us at landrs@nd.edu
* Twitter Handle https://twitter.com/DroneData4Good


.. toctree::
   :maxdepth: 2
   :caption: Contents:

   
Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
