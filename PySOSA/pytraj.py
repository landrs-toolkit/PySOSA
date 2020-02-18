# -*- coding: utf-8 -*-
"""Python module for instantiating and serializing Semantic Trajectories using the STEP Ontologies

Information on Semantic Trajectory Episodes Ontology (STEP) https://talespaiva.github.io/step/
Based on Code from https://github.com/klotzbenjamin/vss-ontology
And demo http://automotive.eurecom.fr/trajectory
This module provides utility class objects for maintaining a Trajectory and the ability to serialize them as JSON-LD.

Todo:
    * Add configuration for sensors.
    * Additional Organizational Information

"""

from rdflib import Graph, URIRef, BNode, Literal, Namespace, RDF, RDFS, XSD
from pyld import jsonld
from datetime import datetime
from pytz import timezone
from time import gmtime, strftime
import json
import uuid


# Add Graph obj
trajgraph = Graph()

# Add namespaces

sosa = Namespace("http://www.w3.org/ns/sosa/")
prov = Namespace("http://www.w3.org/ns/prov#")
qudt_1_1 = Namespace("http://qudt.org/1.1/schema/qudt#")
owltime = Namespace("http://www.w3.org/2006/time#")
owl = Namespace("http://www.w3.org/2002/07/owl#")
rdf = Namespace("http://purl.org/dc/terms/")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
qudt_unit_1_1 = Namespace("http://www.qudt.org/1.1/vocab/unit#")
sf  = Namespace("http://www.opengis.net/ont/sf#")
geo = Namespace("http://www.opengis.net/ont/geosparql#")
step=Namespace("http://www.purl.org/net/step#")




class Trajectory(object):
    fixlist = []
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.movingObject = BNode()
        self.trajectory = BNode()
        self.rawTrajectory = BNode()

        trajgraph.add((self.movingObject, RDF.type, geo.Feature))
        trajgraph.add((self.movingObject, RDF.type, step.Agent))
        trajgraph.add((self.movingObject, step.hasTrajectory, self.trajectory))
        trajgraph.add((self.trajectory,step.hasRawTrajectory,self.rawTrajectory))
        trajgraph.add((self.trajectory,RDF.type,step.Trajectory))
        trajgraph.add((self.rawTrajectory,RDF.type,step.RawTrajectory))

    # Add a Fix to a raw semantic trajectory.
    # Designed to create a 2-d or optional 3-d point in wkt
    # Designed to take an optional time argument or generate time point based on current time.
    def addFix(self, lat, long, altitude = None, thisTime = None):
        MyFix=BNode()
        trajgraph.add((self.rawTrajectory,step.hasFix,MyFix))
        if thisTime is None:
            trajgraph.add((MyFix,owltime.Instant,Literal(str(strftime("%Y-%m-%dT%H:%M:%S", gmtime())),datatype=XSD.dateTime)))
        else:
            trajgraph.add((MyFix,owltime.Instant,Literal(str(strftime("%Y-%m-%dT%H:%M:%S", thisTime)),datatype=XSD.dateTime)))

        if altitude is None:
            trajgraph.add((MyFix,sf.Point,Literal("POINT("+str(lat)+" "+str(long)+")",datatype=sf.WktLiteral)))
        else:
            trajgraph.add((MyFix,sf.Point,Literal("POINT Z ("+str(lat)+" "+str(long)+" "+str(altitude)+")",datatype=sf.WktLiteral)))

        trajgraph.add((MyFix,RDF.type,step.Fix))

    # adds STEP <SemanticDescription> to segment
    def addSemanticSegment(self):
        pass