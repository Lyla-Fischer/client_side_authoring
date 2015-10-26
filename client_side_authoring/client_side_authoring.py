"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer, String
from xblock.fragment import Fragment


class ClientSideAuthoringXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
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
        The primary view of the ClientSideAuthoringXBlock, shown to students
        when viewing courses.
        """
        frag = Fragment(self.authored_html)
        frag.add_css(self.resource_string("static/css/client_side_authoring.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/client_side_authoring.js"))
        frag.initialize_js('ClientSideAuthoringXBlock')
        return frag

    def author_view(self, context=None):
        """
        The authoring view of the ClientSideAuthoringXBlock,
        shown to authors when they are assembling a course
        """
        html = self.resource_string("static/html/client_side_authoring.html")
        frag = Fragment(html.format(self=self))
        frag.add_content(self.authored_html)

        frag.add_css(self.resource_string("static/css/client_side_authoring.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/client_side_authoring.js"))
        # frag.add_javascript(
        #     self.resource_string("static/js/src/csrf_javascript.js"))
        frag.initialize_js('ClientSideAuthoringXBlock')
        return frag


    @XBlock.json_handler
    def save_authoring(self, data, suffix=''):
        """
        Saves the 'content' attribute of a form POST request for display as 
        HTML as part of a webpage
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
