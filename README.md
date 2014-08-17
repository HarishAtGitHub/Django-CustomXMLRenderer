Django-Rest-framework-XMLRender-without-root-tag
================================================

This python CustomXMLRenderer will render XML without the root tag .


**What was the problem ?**

The root tag was added in the default XMLRenderer. 

**How I solved it ?**

CustomXMLRenderer removes it by overriding render method in XMLRenderer class .
