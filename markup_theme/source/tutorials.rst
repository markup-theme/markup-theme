.. 
.. xxxxx
.. 



==================================================
Tutorials
==================================================

This section contains tutorials and tutorial-like things! They range from examples of customizing and extending |theme| to documentation of what's necessary to keep the them running. We put these here in part because much of customizing and working with Sphinx is some degree of inscrutable or opaque and there just aren't enough examples out there.


.. _tutorials-blockquotes:

Blockquotes
==================================================

|theme| does not support blockquote styles for Markdown by default. This support can be added easily. Blockquotes are added to Markdown like this:

.. code-block:: none

   > This is a blockquote.

but without the supporting CSS the text is presented plainly.

To add support for blockquotes, you'll need to update the CSS for |theme| (for both HTML and PDF).

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


.. _tutorials-change-colors:

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


.. _tutorials-code-block-styles:

Code Block Styles
==================================================

A new color style for code blocks can be easily added. There are three spots in the ``_sphinx.scss`` file that require updates for new code blocks, along with a new entry in ``_config.scss``.

The following example shows how to add code block styles for everybody's favorite statically-typed purely functional programming language: Haskell!

**Add code block styles for Haskell**

#. Identify the shortname for the lexer in Pygments. In this case, it's ``haskell``.
#. Open a command prompt and navigate to the ``_themes/markup/static/`` directory.
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

   .. tip:: For darker background colors use ``$markup-white`` for the text color; for lighter background colors use ``$markup-almost-black``. The text color is defined by ``color`` in the first CSS block.


.. _tutorials-font-awesome-icons:

Font Awesome Icons
==================================================

Font Awesome is an `open source icon library <https://fontawesome.com/license/free>`__ that offers a free standard set of icons. |theme| uses a single unmodified CSS and a single unmodified JavaScript file from the Font Awesome Free for the Web library.

.. note:: Use any `icon in the Free for the Web library <https://fontawesome.com/icons?d=gallery&m=free>`__. You may need to upgrade the CSS and JavaScript files in |theme| to use the same set that is on the Font Awesome website.

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


.. _tutorials-github-pages:

GitHub Pages
==================================================

You can host the output of a Sphinx project on GitHub pages:

#. Create a directory named ``/docs`` as a top-level directory in your documentation project.
#. In the ``/docs`` directory, add a file named ``.nojekyll``. This file should be empty.
#. Build your Sphinx output to the ``/docs`` directory.
#. In GitHub, choose **Settings** and then under **GitHub Pages** select the ``master branch /docs folder`` option. The **Settings** page will refresh with the URL for the published HTML. For example: https://markup-theme.github.io/markup-theme/.
#. Check in your project.
#. A few minutes later you should see the HTML at the URL specified under **GitHub Pages**.

.. note:: You may need to update the linking paths used in the site for the ``nav-docs``, ``layout``, and ``search`` files, as the GitHub path generated by GitHub pages adds a directory to the path that is the same name as the project. For example, the ``/markup-theme/`` part of the ``https://markup-theme.github.io/markup-theme/`` is added and this may affect how URLs are defined across the site.


.. _tutorials-github-pages-404:

404.html
--------------------------------------------------
You can add a 404.html page to the output of a Sphinx project on GitHub pages:

#. Create a file named ``404.rst`` in the docs collection that is used for the root of the documentation website. For example, |theme| uses the ``/markup_theme/`` as its top-level for GitHub pages.

   For the initial creation, make the page like this:

   .. code-block:: rst

      ==================================================
      Page not found ...
      ==================================================

      The page you were looking for is not here.

   You can change this later to be anything you want. It's a reStructuredText page that follows all of the same rules as any other reStructuredText page in |theme|.

#. Add ``404`` to the ``toctree`` list in ``index.html`` file that is located in the same collection.
#. Build your Sphinx output to the ``/docs`` directory.
#. Push the changes to GitHub.
#. Verify the changes by entering a page name you know does not exist. That page should show the contents of ``404.html``.


.. _tutorials-glossary:

Glossary
==================================================

A glossary is super cool! |theme| does not have one. Boo! But you can add one! Here's how.

#. Open the ``nav-docs.html`` file located at ``_themes/markup-theme/``. This is the global template for the left-side navigation.
#. Scroll to the bottom and find the ``<li class="main-item dark-item">`` entries. There's one already there named "Site Map".
#. Copy this:

   .. code-block:: html

      <li class="main-item dark-item">
        <a href="index.html"><i class="fas fa-sitemap fa-fw icon-left"></i>Site Map</a>
      </li>

   and paste it immediately above that ``<li>`` grouping.

#. Then change it to say this:

   .. code-block:: html

      <li class="main-item dark-item">
        <a href="glossary.html"><i class="fas fa-book fa-fw icon-left"></i>Glossary</a>
      </li>

#. In the ``markup_theme`` docs collection, add a file named ``glossary.rst``.
#. Name the title "Glossary" and use the definition list pattern for each term. For example:

   .. code-block:: rst

	  ==================================================
	  Glossary
	  ==================================================

	  This page contains an awesome glossary!

	  **glossary term A**
	     These are the words for glossary term A.

	  **glossary term B**
	     These are the words for glossary term B.

#. ``glossary.rst`` should be a typical reStructuredText topic. You may use headers to group by letter or (if you have tons of terms) you could split the glossary into separate topics by letter. For example: ``glossary_a.rst``, ``glossary_b.rst``, etc.

Once you have a glossary, it's easy to reuse glossary terms via the includes patterns. See the ``/shared/terms.rst`` in |theme| for how to create a single source for reusable terms.

.. tip:: In addition to a glossary, some organizations can benefit from having a topic that contains only a two-column table with abbreviations and/or initialisms in one column and those abbreviations and/or initialisms spelled out in another. Call this topic ``abbreviations.rst``, give it a title similar to "Abbreviations, Initialisms", and then use a list-table with rows for each term. For example:

   .. code-block:: none

      .. list-table::
         :widths: 50 550
         :header-rows: 0

         * - **CSV**
           - Comma-Separated Values
         * - **Mbit**
           - Megabit
         * - **MB**
           - Megabyte
         * - **MiB**
           - Mebibyte

   will look like this:

   .. list-table::
      :widths: 50 550
      :header-rows: 0

      * - **CSV**
        - Comma-Separated Values
      * - **Mbit**
        - Megabit
      * - **MB**
        - Megabyte
      * - **MiB**
        - Mebibyte


.. _tutorials-local-pygments-css:

Local Pygments CSS
==================================================

Pygments is an `open source generic syntax highlighter <http://pygments.org/>`__ that is used by |theme| to prettify source code. Pygments has an `open source license <https://bitbucket.org/birkenfeld/pygments-main/src/default/LICENSE>`__.

|theme| puts a copy of the Pygments CSS into the ``_themes/markup/static/`` directory to provide local control for two CSS settings:

.. code-block:: css

   .highlight .hll { background-color: #f9e784 }
   .highlight  { background: #ffffff; }

They are located at the top of the CSS file. The reason why this is done is to be able to apply a preferred color to code line highlights and to prevent the default grey background for code blocks from appearing in situations where code blocks appear inside admonitions, by changing it to white.

It's a somewhat clumsy workaround, but figuring out how to override two specific CSS settings in Pygments was harder and (at this time) seems impossible. If you don't want to use a local copy of pygments.css, just remove it from |theme|. The default yellow highlight is probably fine and the instance of code blocks appearing inside admonitions should be uncommon. If you want to keep it, you may need to grab an updated copy of pygments.css and re-do these two changes when Pygments itself is upgraded.


.. _tutorials-large-topics-single-source:

Large Topics, Single Source
==================================================

You can build entire sections of content by copying in paragraphs from other topics using the ``includes`` directive (via file or via snippet). 

This can be quite useful, such as for building reference topics for a collection of API entities, but also building a single topic for *all* API entities. Another example is building PDF topics that reuse most (but not all) of another topic.

It's also possible that output format differences, such as those between the HTML and PDF outputs in |theme|, even when subtle, may not be fully compatible. This approach allows you to use single sourcing as much as possible, while also addressing output-specific requirements for certain sections that cannot be single sourced.

Look in ``/markup_pdf/rst.rst`` to see a topic that is built almost entirely by copying in paragraphs from ``/markup_rst/rst.rst``. There are some carefully crafted bespoke paragraphs wrapped in there, but most of it is pulled in via the ``includes`` directive.

Due to the nature of how the ``includes`` directive works, any path that is accessible to the Sphinx build command can be a valid inclusion target. This could be other topics in other directories within the same repo (as |theme| demonstrates) or it could be other topics in other repos.


.. _tutorials-navigation-icons:

Navigation Icons
==================================================

|theme| is configured to use Font Awesome icons in the following locations:

* Throughout the left-side navigation at the first level of headers.
* At the top of the right-side navigation.
* For the hamburger button.
* Inline in paragraphs (via special steps in reStructuredText files or via HTML tags in Markdown).


.. _tutorials-navigation-icons-left-side:

Left Side
--------------------------------------------------

The site-specific nav-docs.html file uses Font Awesome to apply icons to the left-side of the first-level headers.

**Font Awesome icons**

The standard way |theme| adds Font Awesome icons to the left-side navigation uses the ``iconClass`` line to specify which icon to use:

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


.. _tutorials-navigation-icons-right-side:

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


.. _tutorials-navigation-icons-hamburger:

Hamburger Button
--------------------------------------------------

A `hamburger button <https://en.wikipedia.org/wiki/Hamburger_button>`__ appears in the browser when it's at smaller sizes. This enables users to browse the top-level and left-side navigation structures. This icon that renders as the hamburger icon is specified in ``layout.html``:

.. code-block:: html

   <div id="nav-icon"><i class="fas fa-bars"></i></div>

This icon is set globally via ``_themes/markup/layout.html`` and per-site via ``_templates/layout.html``. In general, this icon is probably best left alone.


.. _tutorials-navigation-icons-inline:

Inline
--------------------------------------------------

You can create inline Font Awesome icons.

* For reStructuredText topics, this requires using tokens: ``|token-name|``.
* For Markdown, you can use inline HTML: ``<i class="fas fa-heart"></i>``.

See the guides for reStructuredText and Markdown for more information.



.. _tutorials-pdf-cover-pages:

PDF Cover Pages
==================================================

PDF generation relies on two images located in the ``markup_pdf/_static`` directory:

* cover-test.png
* markup-logo.png

Both of these images should be replaced with your preferred PDF cover and company logo. Replace ``cover-test.png`` with any PNG image you want, and then update ``markup-logo.png`` with your company's logo.

If you change any of these names, be sure to update these names in the ``_themes/markup_pdf/layout.html`` file also. While you're in there, fix the copyright statement at the bottom to say your company name and your company URL.

You can move around the ``markup-logo.png`` file by adjusting the ``top``, ``left``, ``width``, and ``height`` settings for ``#logo`` in the ``_nav.scss`` file ``markup_pdf`` theme.



.. _tutorials-tokens:

Tokens
==================================================

|theme| has an example of tokens built into the theme. Open the ``/markup_theme/tokens/names.txt`` to see examples of tokens. For example:

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

   .. |fa-index-circle| raw:: html

      <i class="fas fa-circle fa-xs" data-fa-transform="shrink-5"></i>

which then appears like this:

some string |fa-index-circle| some string |fa-index-circle| some string

A location in the docs where something like this is useful is a front page in which all of the topics are listed, sort of line an index. See https://docs.djangoproject.com/en/2.2/ and the ``|`` character they use. Instead, |theme| sets it as a circle icon from Font Awesome.

.. note:: Markdown topics can use the ``<i class>`` string directly inline and do not require a token.
