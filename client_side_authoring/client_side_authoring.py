"""TO-DO: Write a description of what this XBlock is."""

import pkg_resources

from webob.exc import HTTPTemporaryRedirect

from mako.template import Template

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

    student_data = String(
        default=unicode(""), scope=Scope.user_state,
        help="Student data stored server-side as a service for authors",
    )

    def resource_string(self, path):
        """Handy helper for getting resources from our kit."""
        data = pkg_resources.resource_string(__name__, path)
        return data.decode("utf8")


    def student_view(self, context=None):
        """
        A view which renders an authored web page
        """
        frag = Fragment(self.authored_html)
        frag.add_css(self.authored_css)
        frag.add_javascript(self.resource_string("/static/js/src/provide_services.js"))
        #TODO: This puts a variable in the global namespace, but hopefully future versions of XBlock will have better security around that. 
        frag.add_javascript("var authored_javascript = '" + self.authored_javascript + "';") 
        frag.initialize_js('ProvideServices')
        return frag


    def raw_authoring_view(self, context=None):
        """
        A raw authoring view allowing web page writers to edit HTML, CSS, and Javascript
        """
        html = self.resource_string("static/html/client_side_authoring.mako")
        frag = Fragment(Template(html).render(
                            authored_html=self.authored_html,
                            authored_css=self.authored_css, 
                            authored_javascript = self.authored_javascript))
        
        #adding basic files
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


    def wysiwyg_authoring_view(self, context=None):
        """
        Provides a WYSIWYG authoring view for web pages.
        """

        html = self.resource_string("static/html/WYSIWYG_authoring.mako")
        student_frag = self.student_view()
        student_html = student_frag.head_html() + student_frag.body_html()
        frag = Fragment(Template(html).render(
                            authored_content = student_html))


        frag.add_css(self.resource_string("static/css/client_side_authoring.css"))
        frag.add_javascript(
            self.resource_string("static/js/src/WYSIWYG_authoring.js"))
        frag.add_javascript(
            self.resource_string("static/js/src/csrf_javascript.js"))
        local_resource_url=self.runtime.local_resource_url(self, 'public/tinymce/js/tinymce/tinymce.min.js')
        frag.add_javascript_url(local_resource_url)
        frag.initialize_js('WysiwygAuthoring')
        return frag

    def studio_view(self, context=None):
        """
        Provides a studio_view by returning the flexible raw_view as a resonable default.

        (OpenCraft likes having a studio_view around, but this implementation 
        has two studio views - raw and wysiwyg.)
        """
        return self.raw_authoring_view(context)

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


    @XBlock.json_handler
    def save_student_data(self, data, suffix=''):
        """
        Saves arbitrary student data, as a server-side service to authors
        """
        self.student_data = data

        response = {
            'student_data' : self.student_data
        }

        return response


    @XBlock.json_handler
    def get_student_data(self, data, suffix=''):
        """
        Gets the student data that was stored as a server-side service to authors

        data is currently an unused parameter
        """

        response = {
            'student_data' : self.student_data
        }

        return response


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
