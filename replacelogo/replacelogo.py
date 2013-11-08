# coding: utf-8

# Replace Logo Plugin

from trac.core import *
from trac.web import IRequestFilter
from trac.web.chrome import ITemplateProvider, add_script, add_meta

class ReplaceLogoPlugin(Component):
    implements(IRequestFilter,  ITemplateProvider)

    # ITemplateProvider#get_htdocs_dirs
    def get_htdocs_dirs(self):
        from pkg_resources import resource_filename
        return [('replacelogo', resource_filename(__name__, 'htdocs'))]

    # ITemplateProvider#get_templates_dirs
    def get_templates_dirs(self):
        return []

    # IRequestFilter#pre_process_request
    def pre_process_request(self, req, handler):
        return handler

    # IRequestFilter#post_process_request
    def post_process_request(self, req, template, data, content_type):

        # send trac project name.
        # insert a meta tag to trac site.
        trac_project_name = self.config.get("project", "name")
        add_meta(req, name="TracProjectTitle", content=trac_project_name)

        # add javascript
        add_script(req, 'replacelogo/js/replacelogo.js')

        return template, data, content_type