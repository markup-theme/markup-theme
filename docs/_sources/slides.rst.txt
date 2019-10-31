.. 
.. xxxxx
.. 


==================================================
Slide Decks
==================================================

.. slides-intro-start

Slide decks are built using Hieroglyph, a plugin for Sphinx. Slide pages are built using reStructuredText and are styled to support a useful subset of the standard |theme| formatting guidelines.

Slides provide a simple and easy way to leverage technical content into a presentation-like format and should be used to support and enhance the technical documentation.

.. slides-intro-end


.. _slides-setup:

Slides Setup
==================================================

.. slides-setup-start

Slide decks require Hieroglyph, a slide deck generator that uses Sphinx and reStructuredText and a dedicated topic collection with a ``conf.py`` file configured to support the ``slides`` builder.

#. Install `Hieroglyph <http://docs.hieroglyph.io/en/latest/index.html>`__:

   .. code-block:: console

      $ pip install hieroglyph

#. Update ``conf.py`` in a project that will be used to generate slide decks:

   Add Hieroglyph to ``extensions``:

   .. code-block:: python

      extensions = ['hieroglyph']

   and then add slides-dedicated configuration settings:

   .. code-block:: python

      # -- Options for HTML Slide output ---------------------------------------------------

      autoslides = True
      slide_theme = 'slides-hieroglyph'
      slide_levels = 3
      slide_numbers = True
      #slide_footer = "Welcome to Slides!"
      #slide_theme_options = {'custom_css':'slides.css'}
      slide_theme_path = ['../../_themes/']
      slide_link_to_html = True
      slide_link_html_to_slides = False
      slide_link_html_sections_to_slides = False
      slide_relative_path = "./slides/"
      slide_html_relative_path = "../"

   .. note:: See the `Hieroglyph documentation <http://docs.hieroglyph.io/en/latest/config.html>`__ for more information about these configuration settings.

#. Run a slide decks Sphinx build using the ``slides`` builder that is installed with Hieroglyph:

   .. code-block:: console

      $ sphinx-build -b slides path/to/source path/to/slides/output

.. slides-setup-end




.. _slides-how-to:

How to Use Slides
==================================================

.. slides-how-to-start

Slides are an HTML page output to a directory as part of the static website structure. Because slides are generated using a specific theme (named ``slides-heiroglyph``) they are output to a dedicated directory.

Slides open in a web browser (Chrome, Firefox, Safari).

To navigate between pages in a slide deck:

#. Press the left/right keyboard arrows to move to previous/next slides
#. Press the spacebar to move to the next slide
#. Click the top left/right corners of the slide area to move to previous/next slides

.. slides-how-to-end


.. _slides-supported-formatting:

Supported Formatting
==================================================

.. slides-supported-formatting-start

Sphinx slides built via Heiroglyph support most of the formatting options built into |theme| and have CSS style and output parity with the standard theme.

.. slides-supported-formatting-end


.. _slides-supported-formats-what-works:

What Works
--------------------------------------------------

.. slides-supported-formats-what-works-start

Keep content to its most simple elements:

* Simple paragraphs, along with **bold**, *italics*, and ``inline code``
* Short ordered, unordered, and definition lists
* Small tables, as long as the contents fit within the visible slide area
* Standalone images; large images should be centered
* Small code blocks
* The occasional admonition (note, warning, tip, etc.).
* Making sure the contents fit within the slide
* Links, though most of the links will be formatted as external links
* Inclusions
* Tokens (verify them!)

.. slides-supported-formats-what-works-end


.. _slides-supported-formats-what-does-not:

What Does Not
--------------------------------------------------

.. slides-supported-formats-what-does-not-start

What works, but may not work well:

* Larger code blocks
* Tables with more than ~6 columns and/or ~6 rows, but ideally 2-3 columns and up to 6 rows
* Admonitions that appear more often than "occasionally" or more than once per slide
* The built-in Heiroglyph ``figure`` class stretches images every which way and generally looks bad

.. slides-supported-formats-what-does-not-end


.. _slides-supported-formats-do-not-use:

Do Not Use
--------------------------------------------------

.. slides-supported-formats-do-not-use-start

The following items are unsupported for various reasons: wrong type of deliverable, Sphinx directive doesn't work in Heiroglyph, CSS issues, etc. Please don't use any of the following formatting options:

* Content tabs
* Expandos
* Custom admonitions
* The ``note`` admonition for the purpose of adding presenter notes. (For some reason, they ... don't work!)

.. slides-supported-formats-do-not-use-end


.. _slides-directive:

slides Directive
==================================================

.. slides-directive-start

The ``slides`` directive defines each slide in the slide deck. It is a normal Sphinx directive and requires all content in that slide to be formatted correctly and be aligned with the ``s`` in the directive.

.. slides-directive-end


.. _slides-directive-title:

Title Slides
--------------------------------------------------

Title slides are used at the beginning of a slide deck.

To define a title slide, use the ``slide`` directive and assign its ``level`` to ``1``:

.. code-block:: rst

   ==================================================
   Title Slide
   ==================================================

   <no content>

.. note:: The contents of a title slide should be empty.


.. _slides-directive-section:

Section Slides
--------------------------------------------------

Section slides are the slides that contain actual content.

To define a section slide, use the ``slide`` directive and assign its ``level`` to ``2``:

.. code-block:: rst

   .. slide:: Slide Name
      :level: 2

      This is the content of a section slide.


.. _slides-directive-noheader:

Slides w/o Headers
--------------------------------------------------

You may use slides without headers, when necessary. For example, slides that contain a series of images that want to focus on the differences between individual images work best when the slide does not have a header.

To define a slide with no header, use the ``slide`` directive, assign its ``level`` to ``2``, and leave the slide name empty:

.. code-block:: rst

   .. slide::
      :level: 2

      This is the content of a no-title section slide.

For example, a slide that defines an image that is part of a series of images:

.. code-block:: rst

   .. slide::
      :level: 2

      .. image:: ../../images/filename.png
         :width: 700 px
         :align: center


.. _slides-directive-group:

Group Slides
--------------------------------------------------

Group slides are used within a slide deck to add a title-like slide that can be used to create groups of slides.

To define a group slide, use the ``slide`` directive and assign its ``level`` to ``1``:

.. code-block:: rst

   .. slide:: Slide Group Name
      :level: 1

      <no content>

.. note:: The contents of a group slide should be empty.


.. _slides-directive-build:

build Directive
==================================================

.. slides-directive-build-start

The ``build`` directive defines a series of list items to are added incrementally to the slide each time the space bar is pressed.

For example, to define four steps on a slide:

.. code-block:: rst

   .. rst-class:: build

      - The first list item is shown automatically.
      - Press the spacebar to add the next one.
      - Press the spacebar (again) for the next list item.
      - Press the space (again) to add the final list item. 

.. slides-directive-build-end

.. _slides-example:

Example
==================================================

.. slides-example-start

The following shows an example slide deck:

.. code-block:: rst

   .. 
   .. /slides/
   .. 

   .. slide:: Slide Title Page
      :level: 1
   
      This is a slide title page. While this slide title page has a paragraph on it, typically a slide title page is left blank (except for the title).


   .. slide:: Examples
      :level: 1

      The following slides show examples of the recommended subset for use with slide decks:

      * Paragraphs, including inline formatting
      * Lists
      * Small tables (2x6, 3x6, 4x6, 5x6, 6x6)
      * Small code blocks
      * Images (with or without section titles)
      * Admonitions, such as notes, warnings, or tips


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

      .. image:: ../../images/stages_all.svg
         :width: 600 px
         :align: center

      They may be followed by a short list:

      #. one
      #. two
      #. three
      #. four
      #. five, or so, depending on the image size


   .. slide:: Images without Titles
      :level: 2

      Image slides can be shown without titles simply by omitting the slide name, as shown in the next two slide examples.

   .. slide:: 
      :level: 2

      .. image:: ../../images/mdr_pipeline_components.png
         :width: 700 px
         :align: center


   .. slide:: 
      :level: 2

      .. image:: ../../images/mdr_pipeline_architecture_aws.png
         :width: 700 px
         :align: center


   .. slide:: Simple Code Blocks
      :level: 2

      .. code-block:: python

         retrieve_instructions(
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

.. slides-example-end
