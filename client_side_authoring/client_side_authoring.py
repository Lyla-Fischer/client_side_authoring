"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from xblock.core import XBlock
from xblock.fields import Scope, Integer
from xblock.fragment import Fragment


class ClientSideAuthoringXBlock(XBlock):
    """
    TO-DO: document what your XBlock does.
    """

    authored_html = String(
        default=unicode(""), scope=Scope.content,
        help="The author-provided HTML to be displayed to the students",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")

    def student_view(self, context=None):
        """
        The primary view of the CustomHtmlXBlock, shown to students
        when viewing courses.
        """
        # import pdb; pdb.set_trace()
        frag = Fragment(self.authored_html)
        frag.add_css(self.resource_string("static/css/custom_html.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/custom_html.js"))
        frag.initialize_js('CustomHtmlXBlock')
        return frag

    def author_view(self, context=None):
        """
        The authoring view of the CustomHtmlXBlock,
        shown to authors when they are assembling a course
        """
        html = self.resource_string("static/html/custom_html_authoring.html")
        frag = Fragment(html.format(self=self))
        frag.add_content(self.authored_html)

        frag.add_css(self.resource_string("static/css/custom_html.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/custom_html.js"))
        frag.add_javascript(
            self.resource_string("static/js/src/csrf_javascript.js"))
        frag.add_javascript_url("//tinymce.cachefly.net/4.2/tinymce.min.js")
        frag.initialize_js('CustomHtmlXBlock')
        return frag

    @XBlock.handler
    def save_html(self, data, suffix=''):
        """
        Saves the 'content' attribute of a form POST request for display as 
        HTML as part of a webpage
        """
        self.authored_html = data.POST['content']

        response = HTTPTemporaryRedirect()
        response.location = data.referrer
        return response

    @staticmethod
    def workbench_scenarios():
        """A canned scenario for display in the workbench."""
        return [
            ("ClientSideAuthoringXBlock",
             """<client_side_authoring/>"""),
        ]
