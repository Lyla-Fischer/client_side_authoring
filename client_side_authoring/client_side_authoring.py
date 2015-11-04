"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class ClientSideAuthoringXBlock(XBlock):
    """
    Provides an authoring interface to specify the HTML/CSS/javascript
    that is shown to students using standard XBlock rendering. 
    """

    authored_html = String(
        default=unicode(""), scope=Scope.content,
        help="The author-provided HTML to be displayed to the students",
    )
    authored_css = String(
        default=unicode(""), scope=Scope.content,
        help="The author-provided CSS to be displayed to the students",
    )
    authored_javascript = String(
        default=unicode(""), scope=Scope.content,
        help="The author-provided javascript to be displayed to the students",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        A view which displays the web page that was authored
        """
        frag = Fragment(self.authored_html)
        frag.add_css(self.authored_css)
        frag.add_javascript(self.authored_javascript)
        frag.initialize_js('ClientSideAuthoringXBlock')
        return frag

    def studio_view(self, context=None):
        """
        The authoring view which allows authors to write their web page
        """
        html = self.resource_string("static/html/client_side_authoring.html")
        frag = Fragment(html.format(self=self))
        frag.add_content(self.authored_html)

        #css

        frag.add_css(self.resource_string("static/css/client_side_authoring.css"))


        frag.add_javascript(
            self.resource_string("static/js/src/client_side_authoring.js"))

        #codemirror
        frag.add_javascript(self.resource_string(
            "static/vender/CodeMirror/lib/codemirror.js"))
        frag.add_css(self.resource_string(
            "static/vender/CodeMirror/lib/codemirror.css"))

        #codemirror modes
        frag.add_javascript(self.resource_string(
            "/static/vender/CodeMirror/mode/xml/xml.js"))
        frag.add_javascript(self.resource_string(
            "/static/vender/CodeMirror/mode/css/css.js"))
        frag.add_javascript(self.resource_string(
            "static/vender/CodeMirror/mode/javascript/javascript.js"))

        frag.initialize_js('ClientSideAuthoringXBlock')
        return frag


    @XBlock.json_handler
    def save_authoring(self, data, suffix=''):
        """
        Saves the 'html', 'css', and 'javascript' entries in the json dict
        for display in the student view. 
        """
        self.authored_html = data['html']
        self.authored_css = data['css']
        self.authored_javascript = data['javascript']

        response = {
            'html': self.authored_html, 
            'css':self.authored_css, 
            'javascript': self.authored_javascript
        }

        return response

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ClientSideAuthoringXBlock",
             """<client_side_authoring/>"""),
        ]
