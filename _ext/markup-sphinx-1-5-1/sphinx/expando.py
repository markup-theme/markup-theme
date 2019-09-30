# -*- coding: utf-8 -*-
"""
    Copyright (c) <year>, <copyright holder>
    All rights reserved.

    Redistribution and use in source and binary forms, with or without
    modification, are permitted provided that the following conditions are met:
    1. Redistributions of source code must retain the above copyright
       notice, this list of conditions and the following disclaimer.
    2. Redistributions in binary form must reproduce the above copyright
       notice, this list of conditions and the following disclaimer in the
       documentation and/or other materials provided with the distribution.
    3. All advertising materials mentioning features or use of this software
       must display the following acknowledgement:
       This product includes software developed by the <organization>.
    4. Neither the name of the <organization> nor the
       names of its contributors may be used to endorse or promote products
       derived from this software without specific prior written permission.

    THIS SOFTWARE IS PROVIDED BY <COPYRIGHT HOLDER> ''AS IS'' AND ANY
    EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
    WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
    DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
    (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
    LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
    ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
    SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import os
from docutils.parsers.rst import Directive, directives
from docutils import nodes
from docutils.statemachine import StringList
from sphinx.util.osutil import copyfile


JS_FILE = 'expando.js'


class ToggleDirective(Directive):
    """
    Locate content within vertical expandable sections.
    """

    has_content = True
    option_spec = {'title': directives.unchanged}
    optional_arguments = 1

    def run(self):
        node = nodes.container()
        node['classes'].append('toggle-content')

        header = self.options["title"]
        par = nodes.paragraph(header)
        par['classes'].append('toggle-header')
        if self.arguments and self.arguments[0]:
            par['classes'].append(self.arguments[0])

        self.state.nested_parse(StringList([header]), self.content_offset, par)
        self.state.nested_parse(self.content, self.content_offset, node)

        return [par, node]


def add_assets(app):
    app.add_javascript(JS_FILE)


def copy_assets(app, exception):
    dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
    source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
    copyfile(source, dest)
    app.info('done')


def setup(app):
    app.add_directive('expando', ToggleDirective)
    
    app.connect('builder-inited', add_assets)
    app.connect('build-finished', copy_assets)
