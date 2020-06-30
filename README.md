
# LANDRS_PySOSA


A python module for building SOSA  based RDF graphs


LANDRS (Linked And Networked DRoneS) project amongst other things we’re working
on creating an ontology and building an OpenAPI specification for creating a Restful API
for building linked data native drone data applications. LANDRS is a Sloan Foundation
funded project to build open source APIs for managing scientific data on drones through the
use of web standards and linked data technologies.



The project endeavors to implement PySOSA: A python module for building SOSA  based RDF graphs.
Sensor, Observation, Sample, and Actuator (SOSA) ontology, provides a lightweight core for Semantic Sensor Network (SSN).
SOSA aims at broadening the target audience and application areas that can make use of Semantic Web ontologies.
To find out more about SOSA and SSN check out https://www.w3.org/TR/vocab-ssn/#SOSAPlatform  and https://www.w3.org/TR/vocab-ssn/ 

# Getting started
PySOSA is A python module for building RDF graphs using the W3C SOSA (Sensors, Observations, Samples,
and Actuators) ontology. For more see https://github.com/landrs-toolkit/PySOSA. In short pySOSA implements
a python-based Linked-Data API for Networked Drones.

Visit www.landrs.org or www.ld.landrs.org

# PySOSA

A python module for use in annotating data using the [SOSA (Sensors, Observations, Samples, and Actuators)](https://www.w3.org/TR/vocab-ssn/#SOSASensor) ontology through the creation of RDF graphs.

Hack Design diagram is [here](./PySOSADesign.png)


# Requirements

Prerequisites for running this project See requirements.txt
https://github.com/BadisaMosesane/Drones-PySOSA/blob/master/requirements.txt

# Installing

Install pylint3 from Install. If you have anaconda already installed use pip -U install pylint to update the pylint
so that pyreverse is added to the scripts folder.

Install Pyreverse

You need to install graphViz as the pyreverse generates the UML diagrams in dot format and needs the dot.exe
provided by Graphviz. Once GraphViz is installed make sure the bin folder is added to the PATH variable so that
pyreverse can find it at run time.

Install sphinx

Install IDE: Pycharm recommended


# Running the Tests

The instructions for getting the project up and running on your local machine and testing purposes

To  run the tests for this module:

$ python -m unittest test_landrs.py

How to generate the UML

cd into the directory of where the project resides
Make sure pylint3 and graphviz are installed
Run the command: $ pyreverse -S <modulename> to generate the dot files in the current folder
Once the dot files are generated use the following command to generate the output in one of the formats available
$ dot -Tpdf <dotfilename> -o output
$ dot -Txxx shows all the available output formats


## Contributing

PRs and issue submissions are highly welcomed. This is an open project, published openly under Apache 2.0. We are
excited to have you contribute to this project!
See link https://github.com/landrs-toolkit/PySOSA

# Issues
The following known issues remain:
- AttributeError: module 'pyobs_pyobs' has no attribute 'Platform'
- The output of the graph needs to be formatted
- More tests needs to be done to cover all test cases
- Need to check if the function for adding objects to the graph does add and check duplicate
- Need a function that queries unit testing and code coverage
more unit testing needed

# License
This project is and always will be published openly under Apache 2.0



## About the LANDRS project under which this module is being developed
This is a project under development by the Sloan Foundation supported Linked And Networked DRoneS (LANDRS) project which is working to build foundational infrastructure for the support of Unmanned Vehicles.  Specifically this project is aimed at building ontologies and supporting code APIs to facilitate communities building applications that leverage the power of linked data and the semantic web to facilitate researchers capturing and publishing Findable Accessible Interoperable and Reusable data using UxVs (colloquially known as 'drones').  While focuses on small scale unmanned aerial vehicles the project intends to build infrastructure that is both scientific and usecase domain agnostic and which might serve a range of unmanned vehicles potentially including ground rovers, and watercraft.

