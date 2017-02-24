# -*- coding: utf-8 -*-
"""
Content tabs specs
=================
"""
import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes
from sphinx.util.osutil import copyfile


CSS_FILE = 'contenttabs.css'
JS_FILE = 'contenttabs.js'


class ExampleCodeDirective(Directive):
    """
    It's container directive with content-tabs class
    """

    has_content = True
    optional_arguments = 1

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text)
        node['classes'].append('content-tabs')

        if self.arguments and self.arguments[0]:
            node['classes'].append(self.arguments[0])

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)
        return [node]


class ExampleCodeTabDirective(Directive):
    has_content = True
    option_spec = {'title': directives.unchanged}
    required_arguments = 1

    def run(self):
        self.assert_has_content()
        text = '\n'.join(self.content)
        node = nodes.container(text)
        node['ids'].append('tab-%s' % self.arguments[0])
        node['classes'].append('tab-content')

        par = nodes.paragraph(text=self.options["title"])
        par['classes'].append('tab-title')
        node += par

        self.add_name(node)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


def add_assets(app):
    app.add_stylesheet(CSS_FILE)
    app.add_javascript(JS_FILE)

def copy_assets(app, exception):
    if app.builder.name != 'html' or exception:
        return
    app.info('Copying examplecode stylesheet/javascript... ', nonl=True)
    dest = os.path.join(app.builder.outdir, '_static', CSS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), CSS_FILE)
    copyfile(source, dest)
    dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
    copyfile(source, dest)
    app.info('done')

def setup(app):
    app.add_directive('content-tabs',  ExampleCodeDirective)
    app.add_directive('tab-container', ExampleCodeTabDirective)
    app.connect('builder-inited', add_assets)
    app.connect('build-finished', copy_assets)
