# Notes regarding implementation
This is a pseudo specification:
- Every class should have a comment and lable parameter
- Many but not all classes have an ID variable
- In the [UML](https://www.lucidchart.com/documents/edit/850a6e19-5757-4882-b6bd-cfff3b791f39/gPu_yc0VCCLi), a closed arrow indicates "has A" and an open arrow indicates "Is A"
- Where attributes are shown as equaling x/y/z etc these are instance variables that should be set by the contructor
- Where attributes are not shown as equaliing anything these are class variables that are not set by the contructor but which should be added to the graph on instantiation as blank nodes.  These class variables should all have associated 'set' functions.
- Both contructors and set functions should both alter variable values and the value in the graph
- Test functions should be written covering all cases
- Documentation should be done per PEP257 style
- Function, Class, and Variable names should all be PEP8 compliant
- In general treat the std as primary authority.  The UML serves primarily to indicate which classes need to support an ID and which variables should be setable/querable within and from which classes
- types are not shown in the UML, use the standard as the reference
- If things are unclear, try looking at the paper, there are some examples of architecture that might make things more clear

Reference standard: https://www.w3.org/TR/vocab-ssn/#SOSASensor
Reference Paper: http://www.semantic-web-journal.net/system/files/swj1878.pdf
