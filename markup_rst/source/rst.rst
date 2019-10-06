.. 
.. this is a commented-out section
.. 

.. role:: red

.. role:: blue



==================================================
Formatting Guide: reStructuredText
==================================================

This is the formatting guide for |rst| as it may be used with |theme|.

* :ref:`format-content-admonitions`
* :ref:`format-content-card-walls`
* :ref:`format-content-code-blocks`
* :ref:`format-content-tabs`
* :ref:`format-content-expandos`
* :ref:`format-content-fontawesome`
* :ref:`Headers (Levels 1-4) <format-content-header-h1>`
* :ref:`format-content-images`
* :ref:`format-content-includes`
* :ref:`format-content-inline-markup`
* :ref:`format-content-links`
* :ref:`format-content-lists`
* :ref:`format-content-tables`
* :ref:`format-content-toctree`
* :ref:`format-content-tokens`
* :ref:`format-content-topic-title`
* :ref:`format-content-additional-resources`

.. _format-content-admonitions:

Admonitions
==================================================

.. format-content-admonitions-start

Admonitions are notes and warnings, and other types of alerts to give to readers. Use notes for a simple callout and warnings for things that will break if not followed correctly. Use the other adminitions sparingly, or at least in a consistent manner.

.. format-content-admonitions-end



.. _format-content-admonition-attention:

Attention
--------------------------------------------------

.. format-content-attention-start

Use ``.. attention::`` as shown here:

.. code-block:: rst

   .. attention:: The words for the attention itself.

to create an admonition like this:

.. attention:: The words for the attention itself.

.. format-content-attention-end



.. _format-content-admonition-caution:

Caution
--------------------------------------------------

.. format-content-caution-start

Use ``.. caution::`` as shown here:

.. code-block:: rst

   .. caution:: The words for the caution itself.

to create an admonition like this:

.. caution:: The words for the caution itself.

.. format-content-caution-end



.. _format-content-admonition-custom:

Custom Admonitions
--------------------------------------------------

.. format-content-custom-start

|theme| uses the default admonition to enable the use of custom admonition titles. The default admonition is styled the same as a note.

For a custom admonition, use ``.. admonition:: some string`` as shown here:

.. code-block:: rst

   .. admonition:: Custom admonition title

      Contents of custom admonition.

Which will appear in the documentation like this:

.. admonition:: Custom admonition title

   Contents of custom admonition.

.. format-content-custom-end



.. _format-content-admonition-danger:

Danger
--------------------------------------------------

.. format-content-danger-start

Use ``.. danger::`` as shown here:

.. code-block:: rst

   .. danger:: The words for the danger itself.

to create an admonition like this:

.. danger:: The words for the danger itself.

.. format-content-danger-end



.. _format-content-admonition-error:

Error
--------------------------------------------------

.. format-content-error-start

Use ``.. error::`` as shown here:

.. code-block:: rst

   .. error:: The words for the error itself.

to create an admonition like this:

.. error:: The words for the error itself.

.. format-content-error-end



.. _format-content-admonition-hint:

Hint
--------------------------------------------------

.. format-content-hint-start

Use ``.. hint::`` as shown here:

.. code-block:: rst

   .. hint:: The words for the hint itself.

to create an admonition like this:

.. hint:: The words for the hint itself.

.. format-content-hint-end



.. _format-content-admonition-important:

Important
--------------------------------------------------

.. format-content-important-start

Use ``.. important::`` as shown here:

.. code-block:: rst

   .. important:: The words for the important itself.

to create an admonition like this:

.. important:: The words for the important itself.

.. format-content-important-end



.. _format-content-admonition-note:

Note
--------------------------------------------------

.. format-content-note-start

Use ``.. note::`` as shown here:

.. code-block:: rst

   .. note:: The words for the note itself.

to create an admonition like this:

.. note:: The words for the note itself.

.. format-content-note-end



.. _format-content-admonition-tip:

Tip
--------------------------------------------------

.. format-content-tip-start

Use ``.. tip::`` as shown here:

.. code-block:: rst

   .. tip:: The words for the tip itself.

to create an admonition like this:

.. tip:: The words for the tip itself.

.. format-content-tip-end



.. _format-content-admonition-warning:

Warning
--------------------------------------------------

.. format-content-warning-start

Use ``.. warning::`` as shown here:

.. code-block:: rst

   .. warning:: The words for the warning itself.

to create an admonition like this:

.. warning:: The words for the warning itself.

.. format-content-warning-end




.. _format-content-card-walls:

Card Walls
==================================================

.. format-content-card-walls-start

A card wall is a series of cards that show content groupings, such as on the main page of a docs site or on a marketing page that's full of links to resources. A card may contain standard inline formatting (plain text, bold, italics, and so on, along with links to topics in other parts of the documentation collection). A card wall may be placed inline on a page. It may also be used as a index page, where the only contents on the index page are cards in the card wall.


.. container:: card-group

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Getting Started

         .. container:: card-wall-description

            The getting started guide is how to get started and learns you how to get started.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Deployment Guide

         .. container:: card-wall-description

            The deployment guide is the deployment guide and learns you how to deploy.

            Links for :ref:`le success <format-content-links>`.

   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            User Guide

         .. container:: card-wall-description

            The user guide is the user guide and learns you how to user.

            Links for :ref:`le success <format-content-links>`.


   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Admin Guide

         .. container:: card-wall-description

            The admin guide is the admin guide and learns you how to admin.

            Links for :ref:`le success <format-content-links>`.



   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Reference

         .. container:: card-wall-description

            The reference guide is the reference guide and learns you how to reference.

            Links for :ref:`le success <format-content-links>`.



   .. container:: card-wall

      .. container:: card-wall-content

         .. container:: card-wall-name

            Diagrams

         .. container:: card-wall-description

            The diagrams guide is just a list of sweet diagrams.

            Links for :ref:`le success <format-content-links>`.

.. format-content-card-walls-end



.. _format-content-code-blocks:

Code Blocks
==================================================

.. format-content-code-blocks-start

For code samples (Python, YAML, JSON, Jinja, config files, and so on) and for commands run via the command line that appear in the documentation we want to set them in code blocks using variations of the ``.. code-block::`` directive.

.. note:: Code block types in the |theme| are generalized. For example: the ``text`` type is used for general text files **including** configuration files and the ``sql`` type is used for general data tables. You may customize this to make them more specific and/or add more types to the code block styling options.

Code blocks are parsed using a tool called Pygments that checks the syntax in the named code block against the lexer in Pygments to help ensure that the structure of the code in the code block, even if it's pseudocode, is formatted correctly.

.. format-content-code-blocks-end

.. format-content-code-blocks-warning-start

.. warning:: Pygments lexers check the code in a code block against a lexer. A lexer checks the structure and syntax of the code in the code block. If this check doesn't pass, a Sphinx build may fail.

   For example, if a code block contains YAML and Jinja and is defined by a ``.. code-block:: yaml`` code block, the build will fail because Jinja templating is not YAML.

   Use a ``none`` code block to (temporarily or permanently) work around any problems you may have with rendering code blocks, as a none block is more forgiving.

.. format-content-code-blocks-warning-end


.. _format-content-code-block-line-emphasis:

Line Emphasis
--------------------------------------------------

.. format-content-code-block-line-emphasis-start

Individual lines in a code block may be emphasized. The presentation is similar to a yellow highlight in a book. The following example shows how to highlight lines 3 and 5 in a code block:

.. code-block:: rst

   .. code-block:: python
      :emphasize-lines: 3,5
   
      def function(foo):
        if (some_thing):
          return bar
        else:
          return 0

will display as:

.. code-block:: python
   :emphasize-lines: 3,5

   def function(foo):
     if (some_thing):
       return bar
     else:
       return 0

.. format-content-code-block-line-emphasis-end



.. _format-content-code-block-command-shell:

Command Shell
--------------------------------------------------

.. format-content-code-block-command-shell-start

For command shell blocks, assign ``console`` as the name of the code block:

.. code-block:: rst

   .. code-block:: console

      $ service stop

to create a code block like this:

.. code-block:: console

   $ service stop

.. format-content-code-block-command-shell-end



.. _format-content-code-block-config-file:

Config File
--------------------------------------------------

.. format-content-code-block-config-file-start

For generic configuration file blocks, assign ``text`` as the name of the code block:

.. code-block:: rst

   .. code-block:: text

      spark.setting.hours 1h
      spark.setting.option -User.timezone=UTC
      spark.setting.memory 20g

to create a code block like this:

.. code-block:: text

   spark.setting.hours 1h
   spark.setting.option -User.timezone=UTC
   spark.setting.memory 20g

.. note:: We're using ``text`` because there are not specific lexers available for all of the various configuration files. The ``text`` lexer allows us to style the code block similar to all of the others, but will not apply any highlighting to the formatting within the code block.

.. format-content-code-block-config-file-end



.. _format-content-code-block-css:

CSS
--------------------------------------------------

.. format-content-code-block-css-start

For CSS code blocks, assign ``css`` as the name of the code block:

.. code-block:: rst

   .. code-block:: css

      ul.tab-selector {
        display: block;
        list-style-type: none;
        margin: 10 0 10px;
        padding: 0;
        line-height: normal;
        overflow: auto;
      }

to create a code block like this:

.. code-block:: css

   ul.tab-selector {
     display: block;
     list-style-type: none;
     margin: 10 0 10px;
     padding: 0;
     line-height: normal;
     overflow: auto;
   }

.. format-content-code-block-css-end



.. _format-content-code-block-data-table:

Data Table
--------------------------------------------------

.. format-content-code-block-data-table-start

Table blocks are used to show the inputs and outputs of processing data, such as with blocks reference documentation. For table code blocks, assign ``sql`` as the name of the code block:

.. code-block:: rst

   .. code-block:: sql

      --------- ---------
       column1   column2 
      --------- ---------
       value     value   
       value     value   
       value     value  
      --------- ---------

to create a code block like this:

.. code-block:: sql

   --------- ---------
    column1   column2 
   --------- ---------
    value     value   
    value     value   
    value     value  
   --------- ---------

.. format-content-code-block-data-table-end



.. _format-content-code-block-html:

HTML
--------------------------------------------------

.. format-content-code-block-html-start

For HTML code blocks, assign ``html`` as the name of the code block:

.. code-block:: rst

   .. code-block:: html

      <div class="admonition warning">
        <p class="first admonition-title">Warning</p>
        <p class="last">The text for the warning built from raw HTML.</p>
      </div>

to create a code block like this:

.. code-block:: html

   <div class="admonition warning">
     <p class="first admonition-title">Warning</p>
     <p class="last">The text for the warning built from raw HTML.</p>
   </div>

.. format-content-code-block-html-end



.. _format-content-code-block-javascript:

JavaScript
--------------------------------------------------

.. format-content-code-block-javascript-start

For JavaScript code blocks, assign ``javascript`` as the name of the code block:

.. code-block:: rst

   .. code-block:: javascript

      $('div.content-tabs').each(function() {
          var tab_sel = $('<ul />', { class: "tab-selector" });
          var i = 0;

          if ($(this).hasClass('right-col')){
              tab_sel.addClass('in-right-col');
          }

          $('.tab-content', this).each(function() {
              var sel_item = $('<li />', {
                  class: $(this).attr('id'),
                  text: $(this).find('.tab-title').text()
              });
              $(this).find('.tab-title').remove();
              if (i++) {
                  $(this).hide();
              } else {
                  sel_item.addClass('selected');
              }
              tab_sel.append(sel_item);
              $(this).addClass('contenttab');
          });

          $('.tab-content', this).eq(0).before(contenttab_sel);
          contenttab_sel = null;
          i = null;
      });

to create a code block like this:

.. code-block:: javascript
      
   $('div.content-tabs').each(function() {
       var tab_sel = $('<ul />', { class: "tab-selector" });
       var i = 0;

       if ($(this).hasClass('right-col')){
           tab_sel.addClass('in-right-col');
       }

       $('.tab-content', this).each(function() {
           var sel_item = $('<li />', {
               class: $(this).attr('id'),
               text: $(this).find('.tab-title').text()
           });
           $(this).find('.tab-title').remove();
           if (i++) {
               $(this).hide();
           } else {
               sel_item.addClass('selected');
           }
           tab_sel.append(sel_item);
           $(this).addClass('contenttab');
       });

       $('.tab-content', this).eq(0).before(contenttab_sel);
       contenttab_sel = null;
       i = null;
   });

.. format-content-code-block-javascript-end



.. _format-content-code-block-json:

JSON
--------------------------------------------------

.. format-content-code-block-json-start

For JSON code blocks, assign ``json`` as the name of the code block:

.. code-block:: rst

   .. code-block:: json
      
      {
        "foo": [
          {
            "one": "12345",
            "two": "abcde",
            "three": "words"
          },
        ]
      }

to create a code block like this:

.. code-block:: json
      
   {
     "foo": [
       {
         "one": "12345",
         "two": "abcde",
         "three": "words"
       },
     ],
   }

.. format-content-code-block-json-end



.. _format-content-code-block-json-jinja:

JSON w/Jinja
--------------------------------------------------

.. format-content-code-block-json-jinja-start

For JSON code blocks that also embed Jinja templating, such as the nav-docs.html files that are used to build the documentation site's left navigation structures, the standard ``.. code-block:: json`` block will not work because the code block is not parsable as JSON. Instead, for code blocks that require a mix of JSON and Jinja templating, assign ``django`` as the name of the code block:

.. code-block:: rst

   .. code-block:: django

      {% extends "!nav-docs.html" %}
      {% set some_jinja = "12345" %}
      {% set navItems = [
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
      ] -%}

to create a code block like this:

.. code-block:: django

   {% extends "!nav-docs.html" %}
   {% set some_jinja = "12345" %}
   {% set navItems = [
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
   ] -%}

.. admonition:: Why django?

   Using ``django`` seems like an odd way to specify a code block that contains both Jinja and JSON.

   Django is a site templating language that is part of the Python world. The Sphinx themes are actually built using a combination of Django, Jinja, JSON, and other stuff. The left-side navigation, in particular, is a mix of JSON structure and Jinja variables.

   ``django`` identifies the Pygments lexer that parses a code block that contains both Jinja and JSON.

.. format-content-code-block-json-jinja-end



.. _format-content-code-block-lua:

Lua
--------------------------------------------------

.. format-content-code-block-lua-start

For Lua code blocks, assign ``lua`` as the name of the code block:

.. code-block:: rst

   .. code-block:: lua

      A = class()
      function A:init(x)
        self.x = x
      end
      function A:test()
        print(self.x)
      end

to create a code block like this:

.. code-block:: lua

   A = class()
   function A:init(x)
     self.x = x
   end
   function A:test()
     print(self.x)
   end

.. format-content-code-block-lua-end



.. 
.. .. _format-content-code-block-markdown:
.. 
.. Markdown
.. --------------------------------------------------
.. 
.. .. format-content-code-block-markdown-start
.. 
.. For Markdown code blocks, assign ``md`` as the name of the code block:
.. 
.. .. code-block:: rst
.. 
..    .. code-block:: md
.. 
..       ~~~
..       ```eval_rst
..       .. note:: This is the text for the note built from a directive.
..       ```
..       ~~~
.. 
..       builds as:
.. 
..       ```eval_rst
..       .. note:: This is the text for the note built from a directive.
..       ```
.. 
.. .. note:: The Markdown lexer requires Pygments 2.2, but is configured to display the same as the reStructuredText code-block, but with MD in the upper right corner.
.. 
.. 
.. to create a code block like this:
.. 
.. .. code-block:: md
.. 
..    ~~~
..    ```eval_rst
..    .. note:: This is the text for the note built from a directive.
..    ```
..    ~~~
.. 
..    builds as:
.. 
..    ```eval_rst
..    .. note:: This is the text for the note built from a directive.
..    ```
.. 
.. .. format-content-code-block-markdown-end




.. _format-content-code-block-none:

None
--------------------------------------------------

.. format-content-code-block-none-start

For text that needs to be formatted as if it were a code block, but isn't actually code, assign ``none`` as the name of the code block:

.. code-block:: rst

   .. code-block:: none

      This is a none block. It's formatted as if it were code, but isn't actually code.

      Can include code-like things:

      function_foo()
        does: something
      end

to create a code block like this:

.. code-block:: none

   This is a none block. It's formatted as if it were code, but isn't actually code.

   Can include code-like things:

   function_foo()
     does: something
   end

.. format-content-code-block-none-end



.. _format-content-code-block-python:

Python
--------------------------------------------------

.. format-content-code-block-python-start

For Python code blocks, assign ``python`` as the name of the code block:

.. code-block:: rst

   .. code-block:: python

      def function(foo):
        if (some_thing):
          return bar
        else:
          return 0

to create a code block like this:

.. code-block:: python

   def function(foo):
     if (some_thing):
       return bar
     else:
       return 0

.. format-content-code-block-python-end



.. _format-content-code-block-rest-api:

REST API
--------------------------------------------------

.. format-content-code-block-rest-api-start

For REST API code blocks that show how to use an endpoint, assign ``rest`` as the name of the code block:

.. code-block:: rst

   .. code-block:: rest
      
      https://www.yoursite.com/endpoint/{some_endpoint}

to create a code block like this:

.. code-block:: rest
      
   https://www.yoursite.com/endpoint/{some_endpoint}


.. note:: Use the :ref:`format-content-code-block-json` code block style for the JSON request/response part of the REST API.

.. format-content-code-block-rest-api-end



.. _format-content-code-block-rst:

reStructuredText
--------------------------------------------------

.. format-content-code-block-rst-start

For reStructured Text code blocks, assign ``rst`` as the name of the code block:

.. code-block:: rst

   .. code-block:: rst

      This is some *reStructured* **Text** formatting.

      .. code-block:: none

         that has some(code);

to create a code block like this:

.. code-block:: rst

   This is some *reStructured* **Text** formatting.

   .. code-block:: none

      that has some(code);

.. format-content-code-block-rst-end



.. _format-content-code-block-ruby:

Ruby
--------------------------------------------------

.. format-content-code-block-ruby-start

For Ruby code blocks, assign ``ruby`` as the name of the code block:

.. code-block:: rst

   .. code-block:: ruby

      items = [ 'one', 1, 'two', 2.0 ]
      for it in items
        print it, " "
      end

      print "\n"

to create a code block like this:

.. code-block:: ruby

   items = [ 'one', 1, 'two', 2.0 ]
   for it in items
     print it, " "
   end

   print "\n"

.. format-content-code-block-ruby-end



.. _format-content-code-block-scala:

Scala
--------------------------------------------------

.. format-content-code-block-scala-start

For Scala code blocks, assign ``scala`` as the name of the code block:

.. code-block:: rst

   .. code-block:: scala

      object HelloWorld {
        def main(args: Array[String]) {
          println("Hello, world!")
        }
      }

to create a code block like this:

.. code-block:: scala

   object HelloWorld {
     def main(args: Array[String]) {
       println("Hello, world!")
     }
   }

.. format-content-code-block-scala-end




.. _format-content-code-block-script:

Shell Script
--------------------------------------------------

.. format-content-code-block-script-start

For shell script blocks, assign ``bash`` as the name of the code block:

.. code-block:: rst

   .. code-block:: bash

      # The product and version information.
      readonly MARKUP_PRODUCT="markup-app"
      readonly MARKUP_VERSION="1.23.45-6"
      readonly MARKUP_RELEASE_DATE="2019-04-01"

to create a code block like this:

.. code-block:: bash

   # The product and version information.
   readonly MARKUP_PRODUCT="markup-app"
   readonly MARKUP_VERSION="1.23.45-6"
   readonly MARKUP_RELEASE_DATE="2019-04-01"

.. format-content-code-block-script-end



.. _format-content-code-block-yaml:

YAML
--------------------------------------------------

.. format-content-code-block-yaml-start

For YAML code blocks, assign ``yaml`` as the name of the code block:

.. code-block:: rst

   .. code-block:: yaml

      config:
        - some_setting: 'value'
        - some_other_setting: 12345

to create a code block like this:

.. code-block:: yaml

   config:
     - some_setting: 'value'
     - some_other_setting: 12345

.. format-content-code-block-yaml-end



.. _format-content-code-block-yaml-jinja:

YAML w/Jinja
--------------------------------------------------

.. format-content-code-block-yaml-jinja-start

For YAML code blocks that also embed Jinja templating, the standard ``yaml`` block will not work because the code block is not parsable as YAML. Instead, these code blocks must be able to parse a mix of YAML and Jinja templating. Assign ``salt`` as the name of the code block:

.. code-block:: rst

   .. code-block:: salt

      {%- set some_jinja = "12345" %}

      config:
        - some_setting: 'value'
        - some_other_setting: {{ some_jinja }}

to create a code block like this:

.. code-block:: salt

   {%- set some_jinja = "12345" %}

   config:
     - some_setting: 'value'
     - some_other_setting: {{ some_jinja }}

.. admonition:: Why salt?

   Using ``salt`` seems like an odd way to specify a code block that contains both Jinja and YAML.

   SaltStack is a configuration management tool similar to Ansible, Chef, and Puppet. SaltStack uses a mix of Jinja and YAML to define system states that are to be configured and maintained. The ``salt`` lexer exists in Pygments originally because of how SaltStack defines system states, their use of Python and documentation built via Sphinx, and the need for a lexer that could parse a file with code samples that contain both Jinja and YAML.

   ``salt`` identifies the Pygments lexer that parses a code block that contains both Jinja and YAML.

.. format-content-code-block-yaml-jinja-end



.. _format-content-tabs:

Content Tabs
==================================================

.. format-content-tabs-start

Content tabs enable a way to group topics together in a compact way. Each topic is associated with a tab and, when clicked, shows that content in a content box below. The content box has a shadow applied to it to distinguish tabbed content from normal content. Use content tabs to group related topics, code styles, information sets, or concise workflows.

.. warning:: Content tabs may only be used in HTML outputs. For content that is output to PDF format, the content tabs will "fail gracefully" by presenting the tab title similar to an H5 header.

.. format-content-tabs-end


.. _format-content-tabs-usage:

Usage
--------------------------------------------------

.. format-content-tabs-usage-start

A set of content tabs is defined inside the ``.. content-tabs::`` directive. This directive should be given a filename-based naming pattern, e.g. ``style-guide-content-tab-usage``:

.. code-block:: rst

   .. content-tabs:: style-guide-content-tab-usage

Each tab is then defined inside ``.. content-tabs::`` using the ``.. tab-container:: name`` directive, where ``name`` is a short string that will appear in the tab and ``:title: title-name`` define the string that will appear in the tab itself:

.. code-block:: rst

   .. tab-container:: name1
      :title: name1

      content for tab

   .. tab-container:: name2
      :title: name2

      content for tab

   ... etc.

When it's all together, it should be similar to:

.. content-tabs:: style-guide-content-tab-usage

   .. tab-container:: name1
      :title: name1

      content for tab1

   .. tab-container:: name2
      :title: name2

      content for tab2

.. format-content-tabs-usage-end

.. format-content-tabs-usage-tip-start

.. tip:: Keep the number of tabs in a content tab group to a small number. If a grouping requires more than 5-6 tabs, consider re-grouping the content. Keeping this to a small number also helps prevent wrapping of content tabs.

.. format-content-tabs-usage-tip-end



.. _format-content-tabs-example-tasks:

Example: UI Tasks
--------------------------------------------------

.. format-content-tabs-example-tasks-start

The following example shows use cases for a very sophisticated user interface supported by a few exceptionally well-written task-based topics organized as a series of content tabs.

**Example**

This user interface is just amazing. Users can do stuff:

.. content-tabs:: style-guide-content-tab-evidence

   .. tab-container:: button
      :title: Click Button

      **To click a button**

      #. Open the application.
      #. In the top navigation bar, click **BUTTON**.
      #. From the list, select a list item.
      #. In the **ITEM** pane, scroll to the bottom, and then click **BUTTON**.

   .. tab-container:: box
      :title: Check Box

      **To check a box**

      #. Open the application.
      #. In the top navigation bar, click **BUTTON**.
      #. From the list, select a list item.
      #. In the **ITEM** pane, scroll to the bottom, and then select the **CHECKBOX**.

   .. tab-container:: field
      :title: Type Something

      **To type something**

      #. Open the application.
      #. In the top navigation bar, click **BUTTON**.
      #. From the list, select a list item.
      #. In the **ITEM** pane, scroll to text box, select it, and then start typing.

.. format-content-tabs-example-tasks-end


.. _format-content-tabs-example-terms:

Example: Terms
--------------------------------------------------

.. format-content-tabs-example-terms-start

This example represents an intro near the start of a longer conceptual topic that needs to introduce some important terminology. You'd use a short paragraph (like this one!), and then put each of the terms in a tab below the paragraph. This example also shows how to use the ``.. includes::`` directive to pull in paragraphs from the source glossary file.

**Example**

Blah blah, the following terms are important for this topic:

.. content-tabs:: style-guide-content-tab-terms

   .. tab-container:: term-a
      :title: Aaaaa

      .. include:: ../../shared/terms.rst
         :start-after: .. term-test-start
         :end-before: .. term-test-end

   .. tab-container:: term-b
      :title: Bbbbb

      .. include:: ../../shared/terms.rst
         :start-after: .. term-test-start
         :end-before: .. term-test-end

   .. tab-container:: term-c
      :title: Ccccc

      .. include:: ../../shared/terms.rst
         :start-after: .. term-test-start
         :end-before: .. term-test-end

   .. tab-container:: term-d
      :title: Ddddd

      .. include:: ../../shared/terms.rst
         :start-after: .. term-test-start
         :end-before: .. term-test-end

.. format-content-tabs-example-terms-end



.. _format-content-expandos:

Expandos
==================================================

.. format-content-expandos-start

Expandos enable content to be grouped under a title bar. When the title bar is clicked, the content expands under the title bar and is visible to the reader. When a title bar with expanded content is clicked, the content collapses under the title bar and is no longer visible.

The content appears inside a box to distinguish expanded content from normal content. Use expandos for things like FAQ pages, support and troubleshooting topics, certain tutorials, and to hide certain types of content from the reader until the reader chooses to view it.

.. format-content-expandos-end

.. format-content-expandos-usage-start

An expando is defined inside the ``.. expando::`` directive. Each expando must be assigned a ``:title:``, which is the string that appears in the expandable title bar on the page:

.. code-block:: rst

   .. expando::
      :title: **This is the title**

      Content goes here, indented correctly, as anywhere else in a rST document.

will appear similar to:

.. expando::
   :title: **This is the title**

   Content goes here, indented correctly, as anywhere else in a rST document.

The ``:title:`` may contain **bold** text, *italics* text, plain text, or a **combination** of *styles*:

.. expando::
   :title: **BOLD**

   The title for this expando is **BOLD**.

.. expando::
   :title: *italics*

   The title for this expando is *italics*.

.. expando::
   :title: **combination** of *styles*

   The title for this expando has a **combination** of *styles*.

The ``:title:`` may even contain a :ref:`Font Awesome icon <format-content-fontawesome>` that has been set up as a token. For example:

.. code-block:: rst

   .. expando::
      :title: We like the Font Awesome |fa-expando-checkbox|!

      This title uses the ``|fa-expando-checkbox|`` token: |fa-expando-checkbox|
      |fa-expando-checkbox| |fa-expando-checkbox|!

will appear similar to:

.. expando::
   :title: We like the Font Awesome |fa-expando-checkbox|!

   This title uses the ``|fa-expando-checkbox|`` token: |fa-expando-checkbox| |fa-expando-checkbox| |fa-expando-checkbox|!


.. warning:: Expando titles may not contain tokens.

.. format-content-expandos-usage-end

.. format-content-expandos-usage-tip-start

.. tip:: Don't use expandos within large reference topics. One of the primary use cases for a large reference topic is to enable the reader to CMD+F, and then search for a string on the page. Content that is inside a hidden expando may not be searchable in this scenario.

.. format-content-expandos-usage-tip-end


.. _format-content-expando-example-faq:

Example: FAQ
--------------------------------------------------

.. format-content-expando-example-faq-start

FAQs are typically lists of questions. People read the questions before they read the answers. Use expandos to show people the questions, and then the answers.

.. expando::
   :title: **How do I set up a Sphinx documentation environment?**

   The following setup instructions assume the following:

   * You are installing on Mac OS
   * You are able to run the `pip` command (for non-Sass applications)
   * You are able to install Rubygems (for Sass)

   For all other installation scenarios, the steps are similarly easy. Please refer to the linked setup docs for each application for the correct information.

   **To set up a theme environment**

   #. `Install Sphinx <http://www.sphinx-doc.org/en/stable/install.html>`__:

      .. code-block:: console

         $ pip install sphinx

   #. `Install Sass <https://sass-lang.com/install>`__:

      .. code-block:: console

         $ sudo gem install sass

   #. `Install the RevealJS docutils plugin <https://github.com/tell-k/sphinxjp.themes.revealjs#set-up>`__:

      .. code-block:: console

         $ pip install sphinxjp.themes.revealjs 

   #. `Install the Recommonmark docutils-compatibility bridge <http://recommonmark.readthedocs.io>`__:

      .. code-block:: console

         $ pip install recommonmark

      A documentation project that supports Markdown authoring must add the following elements to the `conf.py` file:

      Under ``import sys, os`` add:

      .. code-block:: python

         from recommonmark.parser import CommonMarkParser
         from recommonmark.transform import AutoStructify

         source_parsers = {
           '.md': CommonMarkParser,
         }

      Change ``source_suffix = '.rst'`` to ``source_suffix = ['.rst', '.md']``.

      At the bottom of the `Options for HTML output` configuration section, add:

      .. code-block:: python

         def setup(app):
         app.add_config_value('recommonmark_config', {
           'enable_eval_rst': True,
         }, True)
         app.add_transform(AutoStructify)

   #. `Install WeasyPrint <http://weasyprint.readthedocs.io/en/latest/install.html>`__:

      .. code-block:: console

         $ pip install weasyprint

      and then run ``$ weasyprint --version`` to verify.

      .. note:: In some cases, you will need to make sure that the user running the WeasyPrint installation command can write to the install directory. By default, that requires a command similar to: ``$ sudo chown -R $USER:admin /usr/local``.


.. expando::
   :title: **How do I submit a pull request via GitHub Desktop?**

   The following steps describe how to create a pull request when using GitHub Desktop:

   **To create a pull request via GitHub desktop**

   #. Open GitHub Desktop and select a repository.
   #. From the master branch, ensure that the repository is up to date. Click **Fetch Origin** and then click **Pull Origin**.
   #. Select the dropdown next to **Current Branch**, and then choose **New Branch**.
   #. In the **Create a Branch** dialog box, assign the branch a unique name, such as ``user-060718-feedback``, and then click **Create Branch**.
   #. Using your favorite text editor--such as TextMate on a Mac or EditPad Pro on a Windows PC--open the file you want to edit and make your changes.
   #. In GitHub Desktop, under **Current Repository** choose the **Changes** tab. This will show the changes you just made.
   #. Add short description to the **Summary** box, and optionally add a description. Select all of the files to be commited with this branch.
   #. Click **Commit to [name of branch]**.
   #. Select the dropdown next to **Current Branch**, choose **Pull Requests**, and then click the **Create a pull request** link.
   #. In the **Publish Branch** dialog box, click **Publish Branch**. This will open the GitHub web user interface.
   #. On the **Open a pull request** page, add reviewers if necessary. When finished, click **Create pull request**.

      You're done!


.. expando::
   :title: **How do I set up Localhost on a Mac?**

   The ``markup`` theme must be run as an actual website to ensure certain behaviors, especially for top-level navigation linking, left-side navigation linking, correct highlighting in the left-side navigation. This is true even for local development. You can view any HTML page in any browser to read and verify rendering of formatting elements on the pages themselves---notes, warnings, code blocks, tables, etc.---but linking to other pages and/or using the navigation will not behave correctly. Use localhost to enable correct website behaviors on your local machine.

   Mac OS machines have built-in localhost abilities that can be enabled.

   #. Run the following command:

      .. code-block:: console

         $ sudo apachectl restart

   #. Open the configuration file:

      .. code-block:: console

         $ sudo nano /etc/apache2/httpd.conf

      Enable PHP 7.1 by removing the ``#`` from this line:

      .. code-block:: text

         #LoadModule php7_module libexec/apache2/libphp7.so

   #. Restart Apache.

      .. code-block:: console

         $ sudo apachectl restart

   #. Open the configuration file:

      .. code-block:: console

         $ sudo nano /etc/apache2/httpd.conf

      and then update ``DocumentRoot`` and ``<Directory`` to have the path to the ``/output`` directory for the project:

      .. code-block:: text

         $ DocumentRoot "/path/to/project/output/"
           <Directory "/path/to/project/output/">

   #. Restart Apache.

      .. code-block:: console

         $ sudo apachectl restart

.. format-content-expando-example-faq-end


.. _format-content-expando-example-content-party:

Example: Content Patterns
--------------------------------------------------

.. format-content-expando-example-content-party-start

This example shows various standard content elements--paragraphs, bold, italic, tables, content tabs, code blocks, images, includes, glossary terms--included under expandos:

.. expando::
   :title: Glossary terms!

   This is a test. Can expandos have content tabs?

   .. content-tabs:: style-guide-content-tab-terms

      .. tab-container:: term-a-record
         :title: A record

         .. include:: ../../shared/terms.rst
            :start-after: .. term-test-start
            :end-before: .. term-test-end

      .. tab-container:: term-aaaa-record
         :title: AAAA record

         .. include:: ../../shared/terms.rst
            :start-after: .. term-test-start
            :end-before: .. term-test-end

      .. tab-container:: term-axfr-record
         :title: AXFR record

         .. include:: ../../shared/terms.rst
            :start-after: .. term-test-start
            :end-before: .. term-test-end

      .. tab-container:: term-ptr-record
         :title: PTR record

         .. include:: ../../shared/terms.rst
            :start-after: .. term-test-start
            :end-before: .. term-test-end

   Looks like the answer is: YES.

.. expando::
   :title: Simple procedures

   This is text. And

   #. This
   #. Is
   #. An
   #. Ordered
   #. List

      .. code-block:: python

         with_a = 'code sample'


.. expando::
   :title: Grouped procedures

   This section groups a series of procedures as tabbed content.

   .. content-tabs:: style-guide-content-tab-terms

      .. tab-container:: term-a-record
         :title: This is

         **To do the first step**

         #. Do.
         #. Doing.
         #. Done.

      .. tab-container:: term-aaaa-record
         :title: a procedure

         **To do the second step**

         #. Do.
         #. Doing.
         #. Done.

      .. tab-container:: term-axfr-record
         :title: with a series

         **To do the third step**

         #. Do.
         #. Doing.
         #. Done.

      .. tab-container:: term-ptr-record
         :title: of steps

         **To do the fourth step**

         #. Do.
         #. Doing.
         #. Done.

.. format-content-expando-example-content-party-end


.. _format-content-fontawesome:

Font Awesome
==================================================

.. format-content-fontawesome-start

The docs themes use the `free-for-web Font Awesome library <https://fontawesome.com/download>`__ as a local font library, primarily to add some flair to the left-side navigation. It's possible (though should be done sparingly) to place Font Awesome icons inline within paragraphs, like this: |fa-meh|.

This requires the tokens file to have an entry similar to:

.. code-block:: text

   .. |fa-meh| raw:: html

       &nbsp; <i class="fas fa-meh"></i> &nbsp;

after which ``|fa-meh|`` used inline in a paragraph results in |fa-meh|.

.. format-content-fontawesome-end


.. _format-content-header-h1:

Header (Level 1)
==================================================

.. note:: The CSS for |theme| understands headers below H4; however it's recommended to not use headers below that level for some (aesthetic) reasons:

   #. The left-side navigation supports 3 levels.
   #. The right-side navigation, while built automatically from the headers that exist on that page, indents each header level, and then wraps the text when the header is longer than the width of the right-side columm.

   As such, H4 headers are as much formatting as they are organization. Anything below H4 is recommended to be formatted as **Bold** so that it doesn't appear in the right-side navigation, but still looks on the page as if it were an H5 header. Headers formatted via **Bold** cannot be linked from the left-side navigation because only headers generate an anchor reference. Consider also reformatting the structure of your page to minimize the depth of the header levels. Or use H5 headers: it's up to you!

.. format-content-header-h1-start

An H1 header appears in the documentation like this:

.. code-block:: rst

   H1 Headers
   ==================================================
   An H1 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h1-end


.. _format-content-header-h2:

Header (Level 2)
--------------------------------------------------

.. format-content-header-h2-start

An H2 header appears in the documentation like this:

.. code-block:: rst

   H2 Headers
   --------------------------------------------------
   An H2 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h2-end


.. _format-content-header-h3:

Header (Level 3)
++++++++++++++++++++++++++++++++++++++++++++++++++

.. format-content-header-h3-start

An H3 header appears in the documentation like this:

.. code-block:: rst

   H3 Headers
   ++++++++++++++++++++++++++++++++++++++++++++++++++
   An H3 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h3-end


.. _format-content-header-h4:

Header (Level 4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. format-content-header-h4-start

An H4 header appears in the documentation like this:

.. code-block:: rst

   H4 Headers
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
   An H4 header appears in the documentation like this.

Which will appear in the documentation like the actual header for this section.

.. format-content-header-h4-end


.. _format-content-header-markup-length:

Header Markup Length
==================================================

.. format-content-header-markup-length-start

Sphinx requires the length of the header to be at least the same length as the content string that defines the header.

Short headers, short title markup. Makes sense!

That said, in large files, it's easier to scan the structure of the content when you can actually see where the headers are. That's why the header markup strings are recommended to be 50 characters long:

::

   Short title
   ==================================================

This makes it easier to see the structure of the file when scrolling up and down a long topic page. This is pretty much the only reason to use consistent header markup length. Copy, paste, done.

.. format-content-header-markup-length-end


.. _format-content-images:

Images
==================================================

.. format-content-images-start

Images may be embedded in the documentation using the ``.. image::`` directive. For example:

.. code-block:: rst

   .. image:: ../../images/busycorp.svg
      :width: 600 px
      :align: left

with the ``:width:`` and ``:align:`` attributes being aligned underneath ``image`` in the block.

This image will appear in the documentation like this:

.. image:: ../../images/busycorp.svg
   :width: 600 px
   :align: left

Images should be SVG when only HTML output is desired. Printing to PDF from HTML pages requires PNG images.

.. format-content-images-end


.. _format-content-includes:

Includes
==================================================

.. format-content-includes-start

Inclusions are a great way to single-source content. Write it in one place, publish it in many. There are two ways to handle inclusions, though both require using the ``.. includes::`` directive.

#. :ref:`format-content-include-via-file`
#. :ref:`format-content-include-via-snippet`

.. format-content-includes-end



.. _format-content-include-via-file:

via File
--------------------------------------------------

.. format-content-include-via-files-start

Inclusions may be done from standalone files. These standalone files are typically kept as a standalone file located in a dedicated directory within the docs repository, such as ``/shared/some_file.rst``.

The ``.. includes::`` is used to declare the path to that file. At build time, the contents of the included file are built into the location specified by the ``.. includes::`` directive.

For example:

.. code-block:: rst

   .. includes:: ../../includes/terms.rst

will pull in the contents of that file right into the location of the directive.

.. format-content-include-via-files-end



.. _format-content-include-via-snippet:

via Snippet
--------------------------------------------------

.. format-content-include-via-snippet-start

Inclusions may be done from within existing files as long as the target for that snippet is located in another file in the repository.

.. warning:: Snippets may not be used within the same file. What this means is the source of the snippet may not also be the target for that snippet. This will cause a rendering issue in the output or an error in the build.

These types of inclusions require two steps:

#. Declare a start and an end for the snippet; this declaration must be unique across the entire documentation repository.

   .. tip:: To help ensure unique snippet identifiers are built in the output, ensure that the snippet identifiers are directly assocaited with the name of the source directory and source file. These identifiers don't have to be long (though they can be), but they must be unique within a doc set.

      For example, a file locatated at ``internal_docs/source/tips.rst`` should have snippet identifiers like ``.. internal-docs-tips-some-identifier-start`` or ``.. internal-docs-tips-some-identifier-end``.
#. Specify the ``.. includes::`` directive, along with the ``:start-after:`` and ``:end-before:`` attributes.

   The ``:start-after:`` and ``:end-before:`` attributes effectively use a unique code comment located in the file defined by the ``.. includes::`` directive to know the start and end of the snippet to be included.

For example, a snippet is defined in ``docs/source/snippet.rst``:

.. code-block:: rst

   This is the file named snippet.rst. It has a few paragraphs and a
   reusable snippet.

   Paragraph one.

   .. docs-snippet-p2-start

   Paragraph two.

   .. docs-snippet-p2-end

   Paragraph three.

This snippet can be included in other files like this:

.. code-block:: rst

   Some content.

   .. include:: ../../docs/source/snippet.rst
      :start-after: .. docs-snippet-p2-start
      :end-before: .. docs-snippet-p2-end

   Some more content.

This should result in a file that looks similar to:

.. code-block:: rst

   Some content.

   Paragraph two.

   Some more content.

.. format-content-include-via-snippet-end

.. format-content-include-via-snippet-hint-start

.. hint:: Snippets may be sourced from large files that contain lists. For example, let's say the docs site has multiple docs collections (by application, by role, by internal vs. external, etc.) and you want each docs collection to have its own dedicated glossary to both enable consistency across doc sets for the same terms, but to also allow specific glossary terms for each doc set.

   In this case, all glossary terms can be created and managed from a single file like ``shared/terms.rst`` in which the snippet start-end pairs are defined and the glossary terms are managed. Then each ``glossary.rst`` file across the docs set can use the ``.. includes::`` directive to pull in the terms it needs.

.. format-content-include-via-snippet-hint-end



.. _format-content-inline-markup:

Inline Markup
==================================================

.. format-content-inline-markup-start

Paragraphs, lists, and other strings of text behave here like they do in any text editor, with line breaks before and after, the usual. Use any of these formatting options within paragraphs, lists, tables, and so on:

* :ref:`format-content-inline-markup-bold`
* :ref:`format-content-inline-markup-italics`
* :ref:`format-content-inline-markup-code`

.. format-content-inline-markup-end



.. _format-content-inline-markup-bold:

Bold
--------------------------------------------------

.. format-content-inline-markup-bold-start

Use two asterisks (``**``) around the word to apply bold formatting: ``**bold**``. For example: **this is bold content**.

.. format-content-inline-markup-bold-end



.. _format-content-inline-markup-italics:

Italics
--------------------------------------------------

.. format-content-inline-markup-italics-start

Use a single asterisk (``*``) around the word to apply italics formatting: ``*italics*``. For example: *this is italicized content*.

.. format-content-inline-markup-italics-end



.. _format-content-inline-markup-code:

Code Strings
--------------------------------------------------

.. format-content-inline-markup-code-start

Use two backticks around the code string to apply code block formatting. For example:

.. code-block:: rst

   ``inline code string``

renders like this: ``inline code string``.

.. note:: An inline code string should only be used within lists and paragraphs for function names, commands for command-line tools, and so on, and only in a way where the contents of that code string reads normally in a sentence. Use the code-block directive for anything else.

.. format-content-inline-markup-code-end





.. _format-content-links:

Links
==================================================

.. format-content-links-start

There are three types of links:

#. :ref:`External <format-content-links-external>`
#. :ref:`Reference <format-content-links-reference>`
#. :ref:`Topic <format-content-links-topic>`

.. format-content-links-end



.. _format-content-links-external:

External
--------------------------------------------------

.. format-content-links-external-start

Ideally, external links should just be the full URL: http://www.yoursite.com.

In some cases the external URL is too big and/or you want to embed the external link naturally within a sentence:

.. code-block:: rst

   `some link text here <http://www.yoursite.com>`_

For example: `some link text here <http://www.yoursite.com>`_

In some cases, Sphinx will throw warnings and errors if there are too many external links in the docs to the same places, so use a double underscore (``__``) at the end of the external link to stop those warnings/errors.

Linking topics together:

The ``:ref:`` links to an anchor on a page in the doc set, as long as the anchor is specified correctly immediately above the header for the section to which you want to link. For example:

.. code-block:: rst

   :ref:`format-content-code-block-yaml`

will link to the header tagged with:

.. code-block:: rst

   .. `_format-content-code-block-yaml`

There can be only one header with that name in the entire collection. The link itself resolves to the header string, which is why we want to limit use of this type of linking to only things that resolve exactly, such as function names, commands, settings groups, and so on. 

.. format-content-links-external-end



.. _format-content-links-reference:

Reference
--------------------------------------------------

.. format-content-links-reference-start

There are two ways to link to internal headers across the doc set.

First, a pre-requisite: the header to which the link is targeted must have an anchor. For example:

.. code-block:: rst

   .. _anchor-name:

   Internal Reference
   --------------------------------------------------
   There are two ways to link to internal headers across the doc set.
   First, a pre-requisite: the header that is the target of the link
   must be tagged:

where the internal reference is the ``.. _anchor-name:``. The string "anchor-name" must be unique across the entire doc set, so the required pattern for these is <file-name-header-name>, like this:

.. code-block:: rst

   .. _format-content-code-block-yaml:

and then there are two ways to link to that anchor. The first will pull in the header name as the link:

.. code-block:: rst

   :ref:`format-content-code-block-yaml`

and the second will use the string you put there and will not pull in the header name as the link:

.. code-block:: rst

   This links to some information about using
   :ref:`YAML code blocks <format-content-code-block-yaml>`
   in your documentation.

These first example renders like this: :ref:`format-content-code-block-yaml`. The second example is preferred and looks like the next sentence. This links to some information about using :ref:`YAML code blocks <format-content-code-block-yaml>` in your documentation.

.. format-content-links-reference-end



.. _format-content-links-topic:

Topic
--------------------------------------------------

.. format-content-links-topic-start

There are two ways to link to internal topics. The first pulls in the topic name as a link:

.. code-block:: rst

   :doc:`blocks`

and the second uses a string to replace (and override) the header name as the link:

.. code-block:: rst

   This links to some information about using :doc:`blocks </blocks>`
   to build a pipeline.

.. format-content-links-topic-end




.. _format-content-lists:

Lists
==================================================

.. format-content-lists-start

Three types of lists are available:

* :ref:`format-content-list-definition`
* :ref:`format-content-list-ordered`
* :ref:`format-content-list-unordered`

.. format-content-lists-end



.. _format-content-list-definition:

Definition List
--------------------------------------------------

.. format-content-list-definition-start

A definition list is a specially formatted list that uses whitespace to indent the descriptive text underneath a word or a short phrase. This type of list should be used to describe settings, such as command line parameters, API arguments, glossary terms, and so on.

For example:

.. code-block:: rst

   **list_item_one**
      The description must be indented three spaces.

   **list_item_two**
      The description must be indented three spaces.

Which will appear in the documentation like this:

**list_item_one**
   The description must be indented three spaces.

**list_item_two**
   The description must be indented three spaces.

.. format-content-list-definition-end

.. format-content-list-definition-complex-start

.. note:: A definition list may contain a definition list. For example, some configuration settings (already in a definition list) have specific additional settings that must also be in a definition lists. These must be indented and must use the correct amount of white space.

.. format-content-list-definition-complex-start

.. format-content-list-definition-warning-start

.. warning:: A definition list title may not contain :ref:`inline markup <format-content-inline-markup>`.

.. format-content-list-definition-warning-start


.. _format-content-list-ordered:

Ordered List
--------------------------------------------------

.. format-content-list-ordered-start

An ordered list has each list item preceded by ``#.`` followed by a space. For example:

.. code-block:: rst

   #. one
   #. two
   #. three

Which will appear in the documentation like this:

#. one
#. two
#. three

.. format-content-list-ordered-end



.. _format-content-list-unordered:

Unordered List
--------------------------------------------------

.. format-content-list-unordered-start

An unordered list has each list item preceded by a single asterisk (``*``) followed by a space. For example:

.. code-block:: rst

   * one
   * two
   * three

Which will appear in the documentation like this:

* one
* two
* three

.. format-content-list-unordered-end



.. _format-content-tables:

Tables
==================================================

.. format-content-tables-start

Tables are always fun! This theme supports the following table types:

* :ref:`CSV tables <format-content-table-csv>`
* :ref:`Grid tables <format-content-table-grid>`
* :ref:`List tables <format-content-table-list>`
* :ref:`Simple tables <format-content-table-simple>`

You can see from the examples below that there are slight differences between how you can set up the tables to get various table structures. Some table types are more fun than others.

.. format-content-tables-end


.. _format-content-table-csv:

CSV Table
--------------------------------------------------

.. format-content-table-csv-start

Tables may be built from a CSV file as long as the CSV file is available to Sphinx at build time. For example:

.. code-block:: rst

   .. csv-table::
      :file: ../../misc/test.csv
      :widths: 30, 70
      :header-rows: 1

with the ``:widths:`` and ``:header-rows:`` attributes being aligned underneath ``csv-table`` in the block. The ``:file:`` must be the path to a CSV file that is available to Sphinx at build time.

.. note:: |theme| has an example of a CSV file in the ``/misc`` directory. In fact, it's the same one for the ``:file`` parameter used in this example!

A CSV file is similar to:

.. code-block:: rst

   Header1,Header2
   12345,67890
   abcdefghijklmnopqrstuvwxyz,abcdefghijklmnopqrstuvwxyz

where the first line in the CSV file is the header row.

This type of table will appear in the documentation like this:

.. csv-table::
   :file: ../../misc/test.csv
   :widths: 30, 70
   :header-rows: 1

.. format-content-table-csv-end


.. _format-content-table-grid:

Grid Table
--------------------------------------------------

.. format-content-table-grid-start

Grid tables are built by physically spacing out the table in the text file, similar to how it will appear on the page. These are easy when they are small.

.. code-block:: none

   +------------+------------+-----------+ 
   | Header 1   | Header 2   | Header 3  | 
   +============+============+===========+ 
   | body row 1 | column 2   | column 3  | 
   +------------+------------+-----------+ 
   | body row 2 | Cells may span columns.| 
   +------------+------------+-----------+ 
   | body row 3 | Cells may  | - Cells   | 
   +------------+ span rows. | - contain | 
   | body row 4 |            | - blocks. | 
   +------------+------------+-----------+

builds as:

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

.. format-content-table-grid-end





.. _format-content-table-list:

List Table
--------------------------------------------------

.. format-content-table-list-start

A list-table is built using the ``.. list-table::`` directive.

.. code-block:: rst

   .. list-table::
      :widths: 200 400
      :header-rows: 1

      * - columnName
        - columnName
      * - **item1**
        - description
      * - **item2**
        - description

with the ``:widths:`` and ``:header-rows:`` attributes being aligned underneath ``list-table`` in the block. The number of rows (identified by the dashes (``-``) must equal the number of integers specified by ``:widths:``. The integers specified by ``:widths:`` also specifies each column's width, from left to right.

.. list-table::
   :widths: 200 400
   :header-rows: 1

   * - columnName
     - columnName
   * - **item1**
     - description
   * - **item2**
     - description

.. format-content-table-list-end


.. _format-content-table-simple:

Simple Table
--------------------------------------------------

.. format-content-table-simple-start

Simple tables are simple. The markup is focused mostly on the vertical layout. Like grid tables, they are easy when they are small.

.. code-block:: none

   =====  =====  ====== 
      Inputs     Output 
   ------------  ------ 
     A      B    A or B 
   =====  =====  ====== 
   False  False  False 
   True   False  True 
   False  True   True 
   True   True   True 
   =====  =====  ======

builds as:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======

.. format-content-table-simple-end





.. _format-content-toctree:

Toctree
==================================================

.. format-content-toctree-start

A Sphinx project must declare all of the topics that are part of it within a directive named ``toctree``.

.. note:: Because |theme| doesn't build its left navigation automatically from the header structures in topics and because there's no previous/next linking, there's no reason to put a ``toctree`` on more than one page. Instead, just put the ``toctree`` on the root page for the project (default root page name is ``index.rst``), and then add to that ``toctree`` an alphabetical list of every other topic in the collection.

A toctree is similar to:

.. code-block:: none

   .. Hide the TOC from this file.

   .. toctree::
      :hidden:

      test

which defines the list of files--in this case just ``test.rst``--in the documentation collection. Be sure to keep ``:hidden:`` as a property of ``toctree``.

View the ``index.rst`` file in the ``/markup_theme`` directory to see a full and complete example of a toctree.

.. format-content-toctree-end




.. _format-content-tokens:

Tokens
==================================================

.. format-content-tokens-start

Tokens are defined in the file ``names.txt`` located in the ``/tokens`` directory. Each token is defined similar to:

.. code-block:: rst

   .. |company_name| replace:: YourCompanyName

When used in a sentence, use the ``|company_name|`` token to replace that with the string that follows ``replace::``. For example: use ``|theme|`` to add |theme|.

.. warning:: Tokens may not be used in the left-side navigation template (``nav-docs.html``).

The following example tokens exist at ``/tokens/names.txt``:

* ``|company_name|`` => |company_name|
* ``|theme|`` => |theme|
* ``|md|`` => |md|
* ``|rst|`` => |rst|

Use tokens in headers or topic titles carefully. Sphinx will build them correctly in the topic, but anchor references from the left-side navigation will not work unless the anchor reference specifies the token. For example, a token named ``|abc|`` used for a title must be specified in the left navigation as ``"url": "/path/to/file.html#abc"``. Tokens cannot be used within :ref:`inline markup <format-content-inline-markup>`.

.. note:: Too many tokens can really slow builds down. Sphinx will check each file for the presence of tokens, and then check the tokens file to up each token for matching strings. The point at which tokens can slow builds down depends on a) the number of tokens and b) the number of files in each documentation collection. It should be stated that slower builds don't start to become noticeable until there are a couplefew hundred tokens and documentation collections with 60+ topics, some of which are very long reference topics. For small doc sets you may never notice any performance issues and the points at which you may notice performance issues, the benefits of using tokens and reusable strings may outweigh slower build times.

.. format-content-tokens-end



.. _format-content-topic-title:

Topic Titles
==================================================

.. format-content-tokens-start

An topic title header appears in the documentation like this:

.. code-block:: rst

   ==================================================
   Topic Title
   ==================================================

Which will appear in the documentation like the actual topic title for this topic.

.. format-content-tokens-end



.. _format-content-additional-resources:

Additional Resources
==================================================

The following resources may be useful:

* `Google Developer Documentation Style Guide <https://developers.google.com/style/>`_



.. Hide the TOC from this file.

.. toctree::
   :hidden:

   test
