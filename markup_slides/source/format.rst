.. THIS PAGE IS LOCATED AT THE /slides/ PATH.

==================================================
Slide Title Page
==================================================

This is a slide title page. While this slide title page has a paragraph on it, typically a slide title page is left blank (except for the title). When a short paragraph is here, it's effectively a subtitle.

This slide deck also serves as a sort-of smoke test for the supported formatting options.

.. slide:: Supported Formatting
   :level: 1

   The following slides show the recommended subset of supported formatting options. These are identical to the formatting options available with |theme|.

.. slide:: Paragraphs
   :level: 2

   A simple paragraph.

   You can have more than one.


.. slide:: Ordered Lists
   :level: 2

   Always introduce an ordered list:

   #. one
   #. two
   #. three


.. slide:: Unordered lists
   :level: 2

   Always introduce an unordered list:

   - one
   - two
   - three


.. slide:: Definition Lists
   :level: 2

   A definition list works great for things like terminology:

   **some term**
      Indent three spaces, and then keep typing.

   **another term**
      Indent three spaces, and then type some more!


.. slide:: Incremented List Items
   :level: 2

   .. rst-class:: build

      - The first list item is shown automatically.
      - Press the spacebar to add the next one.
      - Press the spacebar (again) for the next list item.
      - Press the space (again) to add the final list item.


.. slide:: Images with Titles
   :level: 2

   Images work best preceded by a single-line introduction:

   .. image:: ../../images/slides_splash.png
      :width: 600 px
      :align: center

   They may be followed by a short list:

   #. one
   #. two, depending on the image size


.. slide:: Images without Titles
   :level: 2

   Image slides can be shown without titles simply by omitting the slide name, as shown in the next slide example.

.. slide:: 
   :level: 2

   .. image:: ../../images/slides_splash.png
      :width: 700 px
      :align: center


.. slide:: Simple Code Blocks
   :level: 2

   .. code-block:: python

      retrieve_instruction(
        self,
        name,
      )


.. slide:: Notes, warnings, and tips
   :level: 2

   These are notes, warnings, and tips:

   .. note:: Use notes sparingly.

   .. warning:: Use warnings even more sparingly.

   .. tip:: Maybe use a tip once in a while.


.. slide:: Tables, 2x6
   :level: 2

   .. list-table::
      :widths: 200 200
      :header-rows: 1

      * - Column 1
        - Column 2
      * - **Row 1**
        - description
      * - **Row 2**
        - description
      * - **Row 3**
        - description
      * - **Row 4**
        - description
      * - **Row 5**
        - description
      * - **Row 6**
        - description


.. slide:: Tables, 3x6
   :level: 2

   .. list-table::
      :widths: 200 200 200
      :header-rows: 1

      * - Column 1
        - Column 2
        - Column 3
      * - **Row 1**
        - description
        - description
      * - **Row 2**
        - description
        - description
      * - **Row 3**
        - description
        - description
      * - **Row 4**
        - description
        - description
      * - **Row 5**
        - description
        - description
      * - **Row 6**
        - description
        - description


.. slide:: Tables, 4x6
   :level: 2

   .. list-table::
      :widths: 200 200 200 200
      :header-rows: 1

      * - Column 1
        - Column 2
        - Column 3
        - Column 4
      * - **Row 1**
        - description
        - description
        - description
      * - **Row 2**
        - description
        - description
        - description
      * - **Row 3**
        - description
        - description
        - description
      * - **Row 4**
        - description
        - description
        - description
      * - **Row 5**
        - description
        - description
        - description
      * - **Row 6**
        - description
        - description
        - description


.. slide:: Tables, 5x6
   :level: 2

   .. list-table::
      :widths: 150 150 150 150 150
      :header-rows: 1

      * - Column 1
        - Column 2
        - Column 3
        - Column 4
        - Column 5
      * - **Row 1**
        - description
        - description
        - description
        - description
      * - **Row 2**
        - description
        - description
        - description
        - description
      * - **Row 3**
        - description
        - description
        - description
        - description
      * - **Row 4**
        - description
        - description
        - description
        - description
      * - **Row 5**
        - description
        - description
        - description
        - description
      * - **Row 6**
        - description
        - description
        - description
        - description


.. slide:: Tables, 6x6
   :level: 2

   .. list-table::
      :widths: 150 150 150 150 150 150
      :header-rows: 1

      * - Column 1
        - Column 2
        - Column 3
        - Column 4
        - Column 5
        - Column 6
      * - **Row 1**
        - description
        - description
        - description
        - description
        - description
      * - **Row 2**
        - description
        - description
        - description
        - description
        - description
      * - **Row 3**
        - description
        - description
        - description
        - description
        - description
      * - **Row 4**
        - description
        - description
        - description
        - description
        - description
      * - **Row 5**
        - description
        - description
        - description
        - description
        - description
      * - **Row 6**
        - description
        - description
        - description
        - description
        - description




.. slide:: More Formatting Options
   :level: 1

   The following slides show all supported formatting options. It is recommended to stick with the smaller subset of recommended formatting options.
   

.. slide:: Admonition: Attention
   :level: 2

   .. attention:: The words for the attention itself.


.. slide:: Admonition: Caution
   :level: 2

   .. caution:: The words for the caution itself.


.. slide:: Admonition: Danger
   :level: 2

   .. danger:: The words for the danger itself.


.. slide:: Admonition: Error
   :level: 2

   .. error:: The words for the error itself.


.. slide:: Admonition: Hint
   :level: 2

   .. hint:: The words for the hint itself.


.. slide:: Admonition: Important
   :level: 2

   .. important:: The words for the important itself.


.. slide:: Admonition: Note
   :level: 2

   .. note:: The words for the note itself.


.. slide:: Admonition: Tip
   :level: 2

   .. tip:: The words for the tip itself.


.. slide:: Admonition: Warning
   :level: 2

   .. warning:: The words for the warning itself.


.. slide:: Code Block: Line Emphasis
   :level: 2

   .. code-block:: python
      :emphasize-lines: 2

      def function(foo):
        if (some_thing):
          return bar


.. slide:: Code Block: Command Shell
   :level: 2

   .. code-block:: console

      $ cr service stop


.. slide:: Code Block: Config File
   :level: 2

   .. code-block:: text

      spark.setting.hours 1h
      spark.setting.option -Duser.timezone=UTC
      spark.setting.memory 20g


.. slide:: Code Block: CSS
   :level: 2

   .. code-block:: css

      ul.tab-selector {
        display: block;
        list-style-type: none;
        margin: 10 0 10px;
        padding: 0;
        line-height: normal;
        overflow: auto;
      }


.. slide:: Code Block: Data Table
   :level: 2

   .. code-block:: sql

      --------- ---------
       column1   column2 
      --------- ---------
       value     value   
       value     value   
       value     value  
      --------- ---------


.. slide:: Code Block: JavaScript
   :level: 2

   .. code-block:: javascript
      
      $('div.content-tabs').each(function() {
          var tab_sel = $('<ul />', { class: "tab-selector" });
          var i = 0;

          $('.tab-content', this).eq(0).before(contenttab_sel);
          contenttab_sel = null;
          i = null;
      });


.. slide:: Code Block: JSON
   :level: 2

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


.. slide:: Code Block: JSON w/Jinja
   :level: 2

   .. code-block:: django

      {% extends "!nav-docs.html" %}
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
          ]
        },
      ] -%}


.. slide:: Code Block: None
   :level: 2

   .. code-block:: none

      This is a none block. It's formatted as if it were code,
      but isn't actually code.

      Can include code-like things:

      function_foo()
        does: something
      end


.. slide:: Code Block: Python
   :level: 2

   .. code-block:: python

      def function(foo):
        if (some_thing):
          return bar
        else:
          return 0



.. slide:: Code Block: REST API
   :level: 2

   .. code-block:: rest
      
      https://www.yoursite.com/endpoint/{some_endpoint}



.. slide:: Code Block: ReStructured Text
   :level: 2

   .. code-block:: rst

      This is some *ReStructured* **Text** formatting.

      .. code-block:: none

         that has some(code);


.. slide:: Code Block: Scala
   :level: 2

   .. code-block:: scala

      object HelloWorld {
        def main(args: Array[String]) {
          println("Hello, world!")
        }
      }


.. slide:: Code Block: Shell Script
   :level: 2

   .. code-block:: bash

      # The product and version information.
      readonly MARKUP_PRODUCT="markup-app"
      readonly MARKUP_VERSION="1.23.45-6"
      readonly MARKUP_RELEASE_DATE="2019-04-01"


.. slide:: Code Block: YAML
   :level: 2

   .. code-block:: yaml

      config:
        - some_setting: 'value'
        - some_other_setting: 12345


.. slide:: Code Block: YAML w/Jinja
   :level: 2

   .. code-block:: salt

      {%- set some_jinja = "12345" %}

      config:
        - some_setting: 'value'
        - some_other_setting: {{ some_jinja }}


.. slide:: Images
   :level: 2

   .. image:: ../../images/tableflip.svg
      :width: 600 px
      :align: center


.. slide:: Inline Paragraph Formatting
   :level: 2

   * Use two asterisks around the word to apply **bold formatting**.
   * Use a single asterisk around the word to apply *italics formatting*.
   * Use two backticks around the code string to apply ``code block formatting``.


.. slide:: Links
   :level: 2

   These types of links should work the same way as anywhere else:
   
   * External
   * Internal (rerference)
   * Topic


.. slide:: Tables: CSV
   :level: 2

   .. csv-table::
      :file: ../../misc/test.csv
      :widths: 30, 70
      :header-rows: 1

