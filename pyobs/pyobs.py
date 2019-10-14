# -*- coding: utf-8 -*-
"""Python module for instantiating and serializing W3C/OGC SSN-EXT Observation Collection.

This module provides utility class objects for maintaining a Observation Collection and the ability to serialize the collections as JSON-LD.

Todo:
    * Add configuration for sensors.
    * Additional Organizational Information

"""

from pyld import jsonld
import json


class ObsCollection(object):
    """ Create SOSA Observation Collection """
    def __init__(self, ):
        """Initialize Configuration for a default Observation Collection.
        FOAF:Person, schema:Person and Prov:Person
        Note that because a proper family name suffix is not supported,
        FRAPO is imported.
        https://github.com/SPAROntologies/frapo
        http://www.sparontologies.net/ontologies/frapo
        @prefix frapo: <http://purl.org/cerif/frapo/> .

        Parameters
        ----------
        :param none

        Returns
        -------
        :returns: ObsCollection object
        """
        self.filename = "sc.yaml"
        self.givenName  = ""
        self.familyName = ""
        # "honorificPrefix": "http://schema.org/honorificPrefix",
        self.honorificPrefix = ""
        # honorificSuffix": "http://schema.org/honorificSuffix",
        self.honorificSuffix = ""
        # @prefix frapo: <http://purl.org/cerif/frapo/> .
        self.hasFamilialSuffix = ""
        self.ORCID = ""
        self.W3ID = ""

# str(uuid.uuid4())

class Observation(object):
    def __init__(self):
        pass

class Sensor(object):
    def __init__(self):
        pass

class ObservableProperty:
    def __init__(self):
        pass