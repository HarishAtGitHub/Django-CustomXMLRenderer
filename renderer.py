from rest_framework.renderers import XMLRenderer
from six import StringIO
from django.utils.xmlutils import SimplerXMLGenerator

class CustomXMLRenderer(XMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        """
        Renders `data` into serialized XML without the root tag. The root tag was added in the default
        XMLRenderer. So this CustomXMLRenderer removes it by overriding XMLRenderer class.
        """
        if data is None:
            return ''
        stream = StringIO()
        xml = SimplerXMLGenerator(stream, self.charset)
        xml.startDocument()
        self._to_xml(xml, data)
        xml.endDocument()
        return stream.getvalue()

