.. 
.. xxxxx
.. 



==================================================
Upgrade the Theme
==================================================

The following sections are less tutorial and more documentation of changes that were necessary to the extensions included with |theme| so they may be run with certain versions of Sphinx.

.. admonition:: Sphinx 1.5.1

   Sphinx 1.5.1 is, effectively, the starting point for |theme|.

.. admonition:: Sphinx 1.8.5

   The following issues were discovered when upgrading to Sphinx 1.8.5:

   #. The expando.py and tabs.py extensions needed to be updated to use the logger module. This was resolved by updating both extensions to import the logger module, and then to use the logger instead of ``app.info('done')``.
   #. The sphinxjp.theme.revealjs theme broke in an automated CI/CD environment because (for whatever reason) it was not installable with Sphinx 1.8.5. We didn't try to debug that specific issue. Instead, this was resolved by moving the ``directives.py`` file from that theme to the ``_ext`` directory, renaming it ``slides.py``, and deprecating the use of a standalone ``compat.py`` file. This was done against Sphinx 1.5.1 prior to upgrading and resolved the problem (for now).

.. admonition:: Sphinx 2.0.1

   The following issues were discovered when upgrading to Sphinx 2.0.1:

   #. TBD. The scope of potential changes for 2.0.1 are unknown. They may be substantial or they may be easy.


.. _upgrade-expando:

expando.py Extension
==================================================

The following tabs highlight changes made to the expando extension as part of Sphinx upgrades. The highlighted changes show the difference between the selected version and the previous version.

.. note:: This extension was repurposed from the `contentui theme <https://github.com/ulrobix/sphinxcontrib-contentui>`__, a BSD-licensed open source project available on GitHub.

.. content-tabs:: expando-upgrades-by-version

   .. tab-container:: sphinx151
      :title: Sphinx 1.5.1

      .. code-block:: python

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

   .. tab-container:: sphinx185
      :title: Sphinx 1.8.5

      .. code-block:: python
         :emphasize-lines: 36,70,71,75

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
         from sphinx.util import logging

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
             logger = logging.getLogger(__name__)
             logger.info('Copying expando JavaScript... ', nonl=True)
             dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
             source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
             copyfile(source, dest)
             logger.info('done')


         def setup(app):
             app.add_directive('expando', ToggleDirective)

             app.connect('builder-inited', add_assets)
             app.connect('build-finished', copy_assets)


.. 
..    .. tab-container:: sphinx201
..       :title: Sphinx 2.0.1
.. 
..       TBD.
.. 


.. _upgrade-tabs:

tabs.py Extension
==================================================

The following tabs highlight changes made to the tabs extension as part of Sphinx upgrades. The highlighted changes show the difference between the selected version and the previous version.

.. note:: This extension was repurposed from the `contentui theme <https://github.com/ulrobix/sphinxcontrib-contentui>`__, a BSD-licensed open source project available on GitHub.

.. content-tabs:: tabs-upgrades-by-version

   .. tab-container:: sphinx151
      :title: Sphinx 1.5.1

      .. code-block:: python

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


         JS_FILE = 'tabs.js'


         class ContentTabsDirective(Directive):
             """
             Group content with horizontal tabs.
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


         class ContentTabsContainerDirective(Directive):
             """
             Allow content to exist within tabs.
             """

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
             app.add_javascript(JS_FILE)


         def copy_assets(app, exception):
             dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
             source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
             copyfile(source, dest)
             app.info('done')


         def setup(app):
             app.add_directive('content-tabs',  ContentTabsDirective)
             app.add_directive('tab-container', ContentTabsContainerDirective)
    
             app.connect('builder-inited', add_assets)
             app.connect('build-finished', copy_assets)

   .. tab-container:: sphinx185
      :title: Sphinx 1.8.5

      .. code-block:: python
         :emphasize-lines: 36,94,95,99

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
         from sphinx.util import logging

         JS_FILE = 'tabs.js'


         class ContentTabsDirective(Directive):
             """
             Group content with horizontal tabs.
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


         class ContentTabsContainerDirective(Directive):
             """
             Allow content to exist within tabs.
             """

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
             app.add_javascript(JS_FILE)


         def copy_assets(app, exception):
             logger = logging.getLogger(__name__)
             logger.info('Copying tabs JavaScript... ', nonl=True)
             dest = os.path.join(app.builder.outdir, '_static', JS_FILE)
             source = os.path.join(os.path.abspath(os.path.dirname(__file__)), JS_FILE)
             copyfile(source, dest)
             logger.info('done')


         def setup(app):
             app.add_directive('content-tabs',  ContentTabsDirective)
             app.add_directive('tab-container', ContentTabsContainerDirective)
    
             app.connect('builder-inited', add_assets)
             app.connect('build-finished', copy_assets)

.. 
..    .. tab-container:: sphinx201
..       :title: Sphinx 2.0.1
.. 
..       TBD.
.. 


.. _upgrade-slides:

slides.py Extension
==================================================

The following tabs highlight changes made to the slides extension as part of Sphinx upgrades. The highlighted changes show the difference between the selected version and the previous version.

.. note:: The changes made for 1.5.1 are in comparison to the ``compat.py`` and ``directives.py`` files in the `open source project <https://github.com/tell-k/sphinxjp.themes.revealjs>`__. The open source license statement was added to the top of slides.py, along with the highlighted changes.

.. content-tabs:: expando-upgrades-by-version

   .. tab-container:: sphinx151
      :title: Sphinx 1.5.1

      .. code-block:: python
         :emphasize-lines: 31,32,33,36,38,40,246,261,277

         # -*- coding: utf-8 -*-
         """
             sphinxjp.themes.revealjs.directives
             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

             :author: tell-k <ffk2005@gmail.com>
             :copyright: tell-k. All Rights Reserved.

             Permission is hereby granted, free of charge, to any person
             obtaining a copy of this software and associated documentation
             files (the "Software"), to deal in the Software without
             restriction, including without limitation the rights to use,
             copy, modify, merge, publish, distribute, sublicense, and/or sell
             copies of the Software, and to permit persons to whom the
             Software is furnished to do so, subject to the following
             conditions:

             The above copyright notice and this permission notice shall be
             included in all copies or substantial portions of the Software.

             THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
             EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
             OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
             NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
             HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
             WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
             FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
             OTHER DEALINGS IN THE SOFTWARE.
         """

         #added from compat.py
         import sys
         text = str if sys.version_info >= (3, 0) else unicode  # NOQA

         from docutils import nodes
         from docutils.parsers.rst import Directive, directives
         from docutils.parsers.rst.roles import set_classes
         #removed from sphinxjp.themes.revealjs import compat

         __docformat__ = 'reStructuredText'


         class revealjs(nodes.General, nodes.Element):
             """ node for revealjs """


         class rv_code(nodes.General, nodes.Element):
             """ node for revealjs code section """


         class rv_small(nodes.General, nodes.Element):
             """ node for revealjs small text section """


         class rv_note(nodes.General, nodes.Element):
             """ node for revealjs presentation note """


         def heading(argument):
             """ directives choices for heading tag """
             return directives.choice(argument, ('h1', 'h2', 'h3', 'h4', 'h5', 'h6'))


         class RevealjsDirective(Directive):
             """ Reveal.JS slide entry  """

             has_content = True
             required_arguments = 0
             optional_arguments = 100
             final_argument_whitespace = False

             option_spec = {
                 'id': directives.unchanged,
                 'class': directives.class_option,
                 'noheading': directives.flag,
                 'title-heading': heading,
                 'subtitle': directives.unchanged,
                 'subtitle-heading': directives.unchanged,
                 'data-autoslide': directives.unchanged,
                 'data-markdown': directives.unchanged,
                 'data-transition': directives.unchanged,
                 'data-transition-speed': directives.unchanged,
                 'data-background': directives.unchanged,
                 'data-background-repeat': directives.unchanged,
                 'data-background-size': directives.unchanged,
                 'data-background-transition': directives.unchanged,
                 'data-state': directives.unchanged,
                 'data-separator': directives.unchanged,
                 'data-separator-vertical': directives.unchanged,
                 'data-separator-notes': directives.unchanged,
                 'data-charset': directives.unchanged,
             }

             node_class = revealjs

             def run(self):
                 """ build revealjs node """

                 set_classes(self.options)

                 text = '\n'.join(self.content)
                 node = self.node_class(text, **self.options)

                 self.add_name(node)

                 if "data-markdown" not in self.options:
                     self.state.nested_parse(self.content, self.content_offset, node)

                 if self.arguments:
                     node['title'] = " ".join(self.arguments)

                 node['noheading'] = ('noheading' in self.options)

                 options_list = (
                     'id',
                     'title-heading',
                     'subtitle-heading',
                     'data-autoslide',
                     'data-transition',
                     'data-transition-speed',
                     'data-background',
                     'data-background-repeat',
                     'data-background-size',
                     'data-background-transition',
                     'data-state',
                     'data-markdown',
                     'data-separator',
                     'data-separator-vertical',
                     'data-separator-notes',
                     'data-charset',
                 )
                 for option in options_list:
                     if option in self.options:
                         node[option] = self.options.get(option)
                 return [node]


         class RvSmallDirective(Directive):
             """
             Create small text tag.
             """
             has_content = True
             required_arguments = 0
             optional_arguments = 0
             final_argument_whitespace = False

             option_spec = {
                 'class': directives.class_option,
             }
             node_class = rv_small

             def run(self):
                 """ build rv_small node """

                 set_classes(self.options)
                 self.assert_has_content()
                 text = '\n'.join(self.content)
                 node = self.node_class(text, **self.options)
                 self.add_name(node)
                 self.state.nested_parse(self.content, self.content_offset, node)
                 return [node]


         class RvNoteDirective(Directive):
             """
             Directive for a notes tag.
             """
             has_content = True
             required_arguments = 0
             optional_arguments = 0
             final_argument_whitespace = False

             option_spec = {
                 'class': directives.class_option,
             }
             node_class = rv_note

             def run(self):
                 """ build rv_note node """
                 set_classes(self.options)
                 self.assert_has_content()
                 text = '\n'.join(self.content)
                 node = self.node_class(text, **self.options)
                 self.add_name(node)
                 self.state.nested_parse(self.content, self.content_offset, node)
                 return [node]


         class RvCodeDirective(Directive):
             """
             Directive for a code block with highlight.js
             """

             has_content = True
             required_arguments = 0
             optional_arguments = 0
             final_argument_whitespace = False
             option_spec = {}
             node_class = rv_code

             def run(self):
                 """ build rv_code node """
                 set_classes(self.options)
                 self.assert_has_content()
                 node = self.node_class('\n'.join(self.content), **self.options)
                 return [node]


         def visit_revealjs(self, node):
             """ build start tag for revealjs """
             section_attr = {}
             markdown_headings = {"h1": "#", "h2": "##", "h3": "###",
                                  "h4": "####", "h5": "#####", "h6": "######"}

             if node.get("id"):
                 section_attr.update({"ids": [node.get("id")]})

             attr_list = (
                 'data-autoslide',
                 'data-transition',
                 'data-transition-speed',
                 'data-background',
                 'data-background-repeat',
                 'data-background-size',
                 'data-background-transition',
                 'data-state',
                 'data-markdown',
                 'data-separator',
                 'data-separator-vertical',
                 'data-separator-notes',
                 'data-charset',
             )
             for attr in attr_list:
                 if node.get(attr) is not None:
                     section_attr.update({attr: node.get(attr)})

             title = None
             if node.get("title") and not node.get('noheading'):
                 title = node.get("title")

             title_heading = node.get('title-heading', 'h2')
             subtitle = node.get("subtitle")
             subtitle_heading = node.get('subtitle-heading', 'h3')
             if node.get("data-markdown") is not None:

                 title_base = text("%(heading)s %(title)s \n")
                 title_text = None
                 if title:
                     title_text = title_base % dict(
                         heading=markdown_headings.get(title_heading),
                         title=title
                     )

                 subtitle_text = None
                 if subtitle:
                     subtitle_text = title_base % dict(
                         heading=markdown_headings.get(subtitle_heading),
                         title=subtitle
                     )
             else:
                 title_base = text("<%(heading)s>%(title)s</%(heading)s>\n")
                 title_text = None
                 if title:
                     title_text = title_base % dict(
                         title=title,
                         heading=title_heading)

                 subtitle_text = None
                 if subtitle:
                     subtitle_text = title_base % dict(
                         title=subtitle,
                         heading=subtitle_heading)

             if node.get("data-markdown") is not None:
                 self.body.append(self.starttag(node, 'section', **section_attr))
                 if node.get("data-markdown") == text(""):
                     self.body.append("<script type='text/template'>\n")
                     if title_text:
                         self.body.append(title_text)
                     if subtitle_text:
                         self.body.append(subtitle_text)
                     self.body.append(node.rawsource)
                     self.body.append("</script>\n")
             else:
                 self.body.append(self.starttag(node, 'section', **section_attr))
                 if title_text:
                     self.body.append(title_text)
                 if subtitle_text:
                     self.body.append(subtitle_text)
                 self.set_first_last(node)


         def depart_revealjs(self, node=None):
             """ build end tag for revealjs """
             self.body.append('</section>\n')


         def visit_rv_code(self, node):
             """ build start tag for rv_code """

             self.body.append(self.starttag(node, 'pre'))
             self.body.append("<code data-trim contenteditable>")
             self.body.append(node.rawsource)


         def depart_rv_code(self, node=None):
             """ build end tag for rv_code """

             self.body.append("</code>")
             self.body.append("</pre>\n")


         def visit_rv_small(self, node):
             """ build start tag for rv_small """
             self.body.append(self.starttag(node, 'small'))
             self.set_first_last(node)


         def depart_rv_small(self, node=None):
             """ build end tag for rv_small"""
             self.body.append("</small>\n")


         def visit_rv_note(self, node):
             """ build start tag for rv_note """
             self.body.append(self.starttag(node, 'aside', **{'class': 'notes'}))
             self.set_first_last(node)


         def depart_rv_note(self, node=None):
             """ build end tag for rv_note """
             self.body.append("</aside>\n")


         def setup(app):
             """Initialize """
             app.info('Initializing RevealJS theme directives')
             app.add_node(revealjs, html=(visit_revealjs, depart_revealjs))
             app.add_node(rv_code, html=(visit_rv_code, depart_rv_code))
             app.add_node(rv_note, html=(visit_rv_note, depart_rv_note))
             app.add_node(rv_small, html=(visit_rv_small, depart_rv_small))
             app.add_directive('revealjs', RevealjsDirective)
             app.add_directive('rv_code', RvCodeDirective)
             app.add_directive('rv_note', RvNoteDirective)
             app.add_directive('rv_small', RvSmallDirective)
             return

   .. tab-container:: sphinx185
      :title: Sphinx 1.8.5

      No additional changes were necessary for this extension to run in Sphinx 1.8.5.

.. 
..    .. tab-container:: sphinx201
..       :title: Sphinx 2.0.1
.. 
..       TBD.
.. 