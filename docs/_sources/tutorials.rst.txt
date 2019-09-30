.. 
.. xxxxx
.. 



==================================================
Tutorials
==================================================

This section contains tutorials and tutorial-like things! They range from examples of customizing and extending the MARKUP theme to documentation of what's necessary to keep the them running. We put these here in part because much of customizing and working with Sphinx is some degree of inscrutable or opaque and there just aren't enough examples out there.


Blockquotes
==================================================

The MARKUP theme does not support blockquote styles for Markdown by default. This support can be added easily. Blockquotes are added to Markdown like this:

.. code-block:: none

   > This is a blockquote.

but without the supporting CSS the text is presented plainly.

To add support for blockquotes, you'll need to update the CSS for the MARKUP theme (for both HTML and PDF).

**To add CSS to support blockquotes**

#. Open a command prompt and navigate to the ``_themes/markup/static/`` directory.
#. Run the following command:

   .. code-block:: console

      $ sass --watch scss/markup.scss:markup.css_t

#. Open the ``_themes/markup/static/_sphinx.scss`` file in a text editor.
#. Add CSS similar to:

   .. code-block:: text

      blockquote, q {
        border-left: 5px solid $markup-dark-blue;
        padding: 1em 1em 1em 1em;
      }

#. Save the ``_sphinx.css`` file.
#. Add a blockquote to a Markdown topic:

   .. code-block:: text

      > This is a blockquote.

#. Run the build and review the output.
#. Update the CSS to your preferences. Change the color, margin size, etc.
#. When finished with the ``_themes/markup/static/`` directory, repeat these steps exactly for the ``_themes/markup_pdf/static/`` directory to ensure this style is also available for PDF printing.


Change Colors
==================================================

What, you don't like the colors on this site? Want to use your organization's colors? Fine. Here's how to change them.

#. Open a command prompt and navigate to the ``_themes/markup/static/`` directory.
#. Run the following command:

   .. code-block:: console

      $ sass --watch scss/markup.scss:markup.css_t

#. Open the ``_themes/markup/static/_config.scss`` file in a text editor.
#. This file contains variables similar to:

   .. code-block:: css

      $markup-red: #f06543;
      $markup-dark-blue: #1e2022;
      $markup-blue-grey: #c9d6df;
      $markup-bright-yellow: #f9e784;

   For admonitions and code-blocks, they have specific names:

   .. code-block:: css

      $markup-code-block-console: #216869;
      $markup-note: #52616b;

   Some are related to navigation and others are extension-specific (for tabs and expandos). We'd like to think they are all perfectly named, but they might not be.

#. In the other CSS files, such as ``_sphinx.scss`` you'll see the variables:

   .. code-block:: none
      :emphasize-lines: 2,6,7,8

      div.note {
          border: 2px solid $markup-note;
      }

      div.note p.admonition-title {
          color: $markup-white;
          background-color: $markup-note;
          border-bottom-color: $markup-note;
      }

   You can change these however you want. Do one or two at a time, test as you go. As you save the CSS files, Sass will verify the output is done correctly and will report any errors with the syntax. You'll need to look at the output to make sure you've got the colors you want.




Sass
==================================================

The MARKUP theme is already set up to use `Sass <https://sass-lang.com/>`__. You will need to `download Sass <https://sass-lang.com/install>`__ to make changes to the style sheet. Recommended! You could switch this to be managed by your other favorite CSS manager, like `Less <http://lesscss.org/>`__. But we don't provide any tips on how to do that.


Add Code Block Styles
==================================================

A new color style for code blocks can be easily added. There are three spots in the ``_sphinx.scss`` file that require updates for new code blocks, along with a new entry in ``_config.scss``.

The following example shows how to add code block styles for everybody's favorite statically-typed purely functional programming language.

**Add code block styles for Haskell**

#. Identify the shortname for the lexer in Pygments. In this case, it's ``haskell``.
##. Open a command prompt and navigate to the ``_themes/markup/static/`` directory.
#. Run the following command:

   .. code-block:: console

      $ sass --watch scss/markup.scss:markup.css_t

#. Open the ``_themes/markup/static/_config.scss`` file in a text editor and update the list of code block-specific variables to add the highlighted entry for Haskell, along with choosing a color:

   .. code-block:: none
      :emphasize-lines: 6

      $markup-code-block-none: #93a1aa;
      $markup-code-block-bash: #345995;
      $markup-code-block-console: #216869;
      $markup-code-block-css: #51344d;
      $markup-code-block-django: #8fcb9b;
      $markup-code-block-haskell: #b8c5d6;
      $markup-code-block-html: #eac435;
      /* ... snip ... */

#. Open ``_sphinx.scss`` and add the highlighted sections. This will add Haskell to the CSS that defines the border of the code block:

   .. code-block:: none
      :emphasize-lines: 6,30

      .highlight-none,
      .highlight-bash,
      .highlight-console,
      .highlight-css,
      .highlight-django,
      .highlight-haskell,
      .highlight-html,
      /* ... snip ... */
      .highlight-yaml,{
          position:relative;
          -webkit-border-top-left-radius: 3px;
          -webkit-border-top-right-radius: 3px;
          -webkit-border-bottom-left-radius: 3px;
          -webkit-border-bottom-right-radius: 3px;
          -moz-border-radius-topleft: 2px;
          -moz-border-radius-topright: 2px;
          -moz-border-radius-bottomleft: 2px;
          -moz-border-radius-bottomright: 2px;
          border-top-left-radius: 3px;
          border-top-right-radius: 3px;
          border-bottom-left-radius: 3px;
          border-bottom-right-radius: 3px;
      }

      .highlight-none:before,
      .highlight-bash:before,
      .highlight-console:before,
      .highlight-css:before,
      .highlight-django:before,
      .highlight-haskell:before,
      .highlight-html:before,
      /* ... snip ... */
      .highlight-yaml:before,{
          z-index:10;
          font-size:9px;
          padding:.2em .6em;
          text-align:center;
          color:$markup-dark-grey;
          display:block;
          position:absolute;
          border-radius:0 3px 0 3px;
          border-top:none;
          border-right:none;
          background-color:$markup-lightest-grey;
          top:0;
          right:0;
          height:12px
      }

#. Add the following block of code. Copy and paste one of the others, and then be sure to get the highlighted names correct for the ``content`` and color variable names:

   .. code-block:: none
      :emphasize-lines: 1,2,3,4,6,7

      .highlight-haskell:before{
          content:'HASKELL';
          background-color:$markup-code-block-haskell;
          color:$markup-white;
      }

      .highlight-haskell pre{
          border-color:$markup-code-block-haskell;
          -webkit-border-top-left-radius: 3px;
          -webkit-border-top-right-radius: 3px;
          -webkit-border-bottom-left-radius: 3px;
          -webkit-border-bottom-right-radius: 3px;
          -moz-border-radius-topleft: 2px;
          -moz-border-radius-topright: 2px;
          -moz-border-radius-bottomleft: 2px;
          -moz-border-radius-bottomright: 2px;
          border-top-left-radius: 3px;
          border-top-right-radius: 3px;
          border-bottom-left-radius: 3px;
          border-bottom-right-radius: 3px;
      }

   .. tip:: For darker colors, choose ``$markup-white`` and or lighter colors consider choosing ``$markup-almost-black`` for the text color, which is defined by ``color`` in the first CSS block.




Local Pygments CSS
==================================================

Pygments is an `open source generic syntax highlighter <http://pygments.org/>`__ that is used by the MARKUP theme to prettify source code. Pygments has the following BSD license:

.. code-block:: none

   Copyright (c) 2006-2017 by the respective authors (see AUTHORS file).
   All rights reserved.

   Redistribution and use in source and binary forms, with or without
   modification, are permitted provided that the following conditions are
   met:

   * Redistributions of source code must retain the above copyright
     notice, this list of conditions and the following disclaimer.

   * Redistributions in binary form must reproduce the above copyright
     notice, this list of conditions and the following disclaimer in the
     documentation and/or other materials provided with the distribution.

   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The MARKUP theme puts a copy of pygments.css into the ``_themes/markup/static/`` directory to provide local control for two CSS settings:

.. code-block:: css

   .highlight .hll { background-color: #f9e784 }
   .highlight  { background: #ffffff; }

They are located at the top of the CSS file. The reason why this is done is to be able to apply a preferred color to code line highlights and to prevent the default grey background for code blocks from appearing in situations where code blocks appear inside admonitions, by changing it to white.

It's a somewhat clumsy workaround, but figuring out how to override two specific CSS settings in Pygments was harder and (at this time) seems impossible. If you don't want to use a local copy of pygments.css, just remove it from the MARKUP theme. The default yellow highlight is probably fine and the instance of code blocks appearing inside admonitions should be uncommon. If you want to keep it, you may need to grab an updated copy of pygments.css and re-do these two changes when Pygments itself is upgraded.


Font Awesome Icon Library
==================================================

Font Awesome is an `open source icon library <https://fontawesome.com/license/free>`__ that offers a free standard set of icons. The MARKUP theme uses a single unmodified CSS and a single unmodified JavaScript file from the Font Awesome Free for the Web library.

**Upgrade the Font Awesome Free for the Web library**

#. Navigate to https://fontawesome.com/start.
#. Click Download.
#. On the next page, click the **Font Awesome Free for the Web** button.
#. When the download is complete, open it. Copy the following files: ``all.css`` and ``all.js``.
#. Paste these files into ``_themes/markup/static/``.

**Use Font Awesome Pro**

#. Navigate to https://fontawesome.com/pro.
#. Purchase a subscription for Font Awesome Pro. 
#. Download the icon library.
#. When the download is complete, open it. Copy the following files: ``all.css`` and ``all.js``.
#. Paste these files into ``_themes/markup/static/``.



PDF Cover Pages
==================================================

PDF generation relies on two images located in the ``markup_pdf/_static`` directory:

* cover-test.png
* markup-logo.png

Both of these images should be replaced with your preferred PDF cover and company logo. Replace ``cover-test.png`` with any PNG image you want, and then update ``markup-logo.png`` with your company's logo.

If you change any of these names, be sure to update these names in the ``_themes/markup_pdf/layout.html`` file also. While you're in there, fix the copyright statement at the bottom to say your company name and your company URL.

You can move around the ``markup-logo.png`` file by adjusting the ``top``, ``left``, ``width``, and ``height`` settings for ``#logo`` in the ``_nav.scss`` file ``markup_pdf`` theme.


Tokens
==================================================

The MARKUP theme has an example of tokens built into the theme. Open the ``/markup_theme/tokens/names.txt`` to see examples of tokens. For example:

.. code-block:: none

   .. |company_name| replace:: YourCompanyName
   .. |theme| replace:: MARKUP
   .. |md| replace:: Markdown
   .. |rst| replace:: reStructuredText

The format for defining a token is:

.. code-block:: none

   .. |token| replace:: some-string

where

* ``|token|`` defines the string (with pipes ``|`` on either side) within your |rst| files
* ``replace::`` tells Sphinx the string that will replace the token
* ``some-string`` defines the string that will be populated by Sphinx at build-time

Tokens are useful for ensuring consistency of naming. They work best with short names, but can be used for complete sentences.

.. tip:: If you create too many tokens, this may slow your build down. In some cases, with lots of tokens, quite a bit. So use them carefully and for things where using a token makes sense.

Another example of using tokens is to create situations where Font Awesome icons can be used inline within reStructuredText topics. For example:

.. code-block:: none

   .. |fa-index-diamond| raw:: html

      <i class="fas fa-diamond fa-xs" data-fa-transform="shrink-5"></i>

which then appears like this:

some string |fa-index-diamond| some string |fa-index-diamond| some string

A location in the docs where something like this is useful is a front page in which all of the topics are listed, sort of line an index. See https://docs.djangoproject.com/en/2.2/ and the ``|`` character they use. Instead, MARKUP theme sets it as a diamond icon from Font Awesome.

.. note:: Markdown topics can use the ``<i class>`` string directly inline and do not require a token.


Navigation Icons
==================================================

The MARKUP theme is configured to use Font Awesome icons in the following locations:

* Throughout the left-side navigation at the first level of headers.
* At the top of the right-side navigation.
* For the hamburger button.
* Inline in paragraphs (via special steps in reStructuredText files or via HTML tags in Markdown).


Left Side
--------------------------------------------------

The site-specific nav-docs.html file uses Font Awesome to apply icons to the left-side of the first-level headers.

**Font Awesome icons**

The standard way the MARKUP theme adds Font Awesome icons to the left-side navigation uses the ``iconClass`` line to specify which icon to use:

.. code-block:: django
   :emphasize-lines: 3

   {
     "title": "Start Here",
     "iconClass": "fas fa-arrow-alt-circle-right fa-fw",
     "subItems": [
       {
         "title": "Start Here",
         "hasSubItems": false,
         "url": "/some_file.html"
       },
       {
         "title": "FAQ",
         "hasSubItems": false,
         "url": "/faq.html"
       },
       {
         "title": "Additional Resources",
         "hasSubItems": false,
         "url": "/resources.html"
       },
     ]
   },

**Custom SVG images**

You can use custom icons--such as a company or product logo--instead, as long as the custom icon is an SVG image and as long as it's in the ``/_static`` directory for that documentation site. Change the ``iconClass`` line to be ``"image": "filename.svg",``:

.. code-block:: django
   :emphasize-lines: 3

   {
     "title": "Start Here",
     "image": "markup.svg",
     "subItems": [
       {
         "title": "Start Here",
         "hasSubItems": false,
         "url": "/some_file.html"
       },
       {
         "title": "FAQ",
         "hasSubItems": false,
         "url": "/faq.html"
       },
       {
         "title": "Additional Resources",
         "hasSubItems": false,
         "url": "/resources.html"
       },
     ]
   },


Right Side
--------------------------------------------------

The right-side navigation is built automatically based on the header structure of the topic. It contains a single icon at the top. This icon is specified in ``_themes/markup/localtoc.html``: 

.. code-block:: jinja
   :emphasize-lines: 3

   {%- if display_toc %}
     <h3>
       <i class="fas fa-newspaper" aria-hidden="true"></i>
       <a href="{{ pathto(master_doc) }}">&nbsp;{{ _('ON THIS PAGE') }}</a>
     </h3>

   {{ toc }}

You may create site-specific right-side navigation icons by adding a copy of ``localtoc.html`` to a site-specific ``_templates`` directory, and then updating the name of the Font Awesome icon.

You may comment it out if you don't want to use the icon:

.. code-block:: jinja
   :emphasize-lines: 3

   {%- if display_toc %}
     <h3>
       <!--<i class="fas fa-newspaper" aria-hidden="true"></i>-->
       <a href="{{ pathto(master_doc) }}">&nbsp;{{ _('ON THIS PAGE') }}</a>
     </h3>

   {{ toc }}


Hamburger Button
--------------------------------------------------

A `hamburger button <https://en.wikipedia.org/wiki/Hamburger_button>`__ appears in the browser when it's at smaller sizes. This enables users to browse the top-level and left-side navigation structures. This icon that renders as the hamburger icon is specified in ``layout.html``:

.. code-block:: html

   <div id="nav-icon"><i class="fas fa-bars"></i></div>

This icon is set globally via ``_themes/markup/layout.html`` and per-site via ``_templates/layout.html``. In general, this icon is probably best left alone.


Inline
--------------------------------------------------

You can create inline Font Awesome icons.

* For reStructuredText topics, this requires using tokens: ``|token-name|``.
* For Markdown, you can use inline HTML: ``<i class="fas fa-heart"></i>``.

See the guides for reStructuredText and Markdown for more information.


Upgrade the MARKUP Theme
==================================================

The following sections are less tutorial and more documentation of changes that were necessary to the extensions included with the MARKUP theme so they may be run with certain versions of Sphinx.

.. admonition:: Sphinx 1.5.1

   Sphinx 1.5.1 is, effectively, the starting point for the MARKUP theme.

.. admonition:: Sphinx 1.8.5

   The following issues were discovered when upgrading to Sphinx 1.8.5:

   #. The expando.py and tabs.py extensions needed to be updated to use the logger module. This was resolved by updating both extensions to import the logger module, and then to use the logger instead of ``app.info('done')``.
   #. The sphinxjp.theme.revealjs theme broke in an automated CI/CD environment because (for whatever reason) it was not installable with Sphinx 1.8.5. We didn't try to debug that specific issue. Instead, this was resolved by moving the ``directives.py`` file from that theme to the ``_ext`` directory, renaming it ``slides.py``, and deprecating the use of a standalone ``compat.py`` file. This was done against Sphinx 1.5.1 prior to upgrading and resolved the problem (for now).

.. admonition:: Sphinx 2.0.1

   The following issues were discovered when upgrading to Sphinx 2.0.1:

   #. TBD. The scope of potential changes for 2.0.1 are unknown. They may be substantial or they may be easy.


expando.py Extension
--------------------------------------------------

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



tabs.py Extension
--------------------------------------------------

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


slides.py Extension
--------------------------------------------------

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