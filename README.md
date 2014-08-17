Django-Rest-framework-XMLRender-without-root-tag
================================================

This python CustomXMLRenderer will render XML without the root tag .


**What was the problem ?**

The root tag was added in the default XMLRenderer class in Django Rest Framework . The root tag will not be necessary in many cases or even turn out to be a burden when this xml need to be processed by other systems which do not know about the unusual root tag .

**How I solved it ?**

CustomXMLRenderer removes it by overriding render method in XMLRenderer class .
