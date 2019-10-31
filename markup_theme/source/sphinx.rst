.. 
.. xxxxx
.. 


==================================================
Sphinx
==================================================

.. sphinx-errors-intro-start

This topic captures errors and warnings and other issues you may see while running Sphinx builds, including suggestions for resolution. This is not a complete list of errors and warnings that may be seen with Sphinx builds.

.. sphinx-errors-intro-end


.. _sphinx-errors-errors:

Sphinx Errors
==================================================

.. sphinx-errors-errors-start

.. 
.. the following block is a template for adding more warnings
.. 
.. **ERROR: xxxxx**
..    Description.
.. 
..    Solution: 
.. 

You may see the following errors:

**Sphinx error: Builder name slides not registered or available through entry point**
   This happens when the builder specified in the ``sphinx-build`` command does not match any of the available builders. For example:

   .. code-block:: console

      $ sphinx-build -b slides markup-theme/markup_slides/source markup-theme/test/slides

   is the command to build Hieroglyph slides. But if the ``conf.py`` file does not specify anything in the ``extensions = []`` configuration setting you will see this error.

   Solution: In addition to running the ``sphinx-build`` command with the correct builder, be sure to specify the correct extension, if required. In the case of Hieroglyph: ``extensions = ['hieroglyph']``.

.. sphinx-errors-errors-end


.. _sphinx-errors-application:

Sphinx Issues
==================================================

.. sphinx-errors-errors-start

.. 
.. the following block is a template for adding more warnings
.. 
.. **Application error: xxxxx**
..    Description.
.. 
..    Solution: 
.. 

You may see the following warnings:

**Application error: config directory doesn't contain a conf.py file**
   This happens when Sphinx cannot find the ``conf.py`` file at the specified source location.

   Solution: Verify the location from which you are running the command and make sure that it is in the correct path to the source directory from the context of the location in the directory from which the command is run. This path is shown in the ALL CAPS section of the command below:

   .. code-block:: bash

      $ sphinx-build -b html PATH/TO/SOURCE/DIRECTORY path/to/output/directory


.. _sphinx-errors-warnings:

Sphinx Warnings
==================================================

.. sphinx-errors-warnings-start

.. 
.. the following block is a template for adding more warnings
.. 
.. **WARNING: xxxxx**
..    Description.
.. 
..    Solution: 
.. 

When running Sphinx, you may see the following warnings:

**WARNING: Block quote ends without a blank line; unexpected unindent**
   This happens typically when some type of list isn't formatted correctly. This warning is *often* (but not always) accompanied by a more specific error that indicates the type of list that is formatted incorrectly.

   Solution: Find the row stated in the error message, find the row stated in the associated error message, and then examine the formatting in that section of the file.

**WARNING: Bullet list ends without a blank line; unexpected unindent**
   This happens when a list isn't formatted correctly, in particular the alignment of the characters that define the list: ``#.`` for ordered lists, ``*`` for unordered lists, a three-space indent for definition lists, and an indented 

   Solution: Find the row stated in the error message. Lists can be ordered, unordered, or definition. Look for misaligned list items. But they may also be in a list-table. For example, note the vertical hyphen alignment in the following list-table:

   .. code-block:: none
   
      .. list-table::
         :widths: 200 400
         :header-rows: 1

         * - columnName
           - columnName
         * - **item1**
           - description
         * - **item2**
          - description

   .. note:: The list-table is a list defined by the asterisks. It then uses a hyphenated list to define each column in the table.

   Another situation you may see this warning is a list that looks like this:

   .. code-block:: none

      * One
       * Two
      * Three


**WARNING: document isn't included in any toctree**
   This happens when a topic is added to the ``/source`` directory, but not also added to the ``toctree`` list in the ``index.rst`` file.

   Solution: Verify the list of topics in the ``index.rst`` file.

**WARNING: Enumerated list ends without a blank line; unexpected unindent.**
   This happens when a list is formatted incorrectly.

   Solution: Find the row stated in the error message. You might see something like this:

   .. code-block:: none

      #. One
       #. Two
      #. Three


**WARNING: Error parsing content block for the "list-table" directive: uniform two-level bullet list expected, but row 2 does not contain the same number of items as row 1 (2 vs 3)**
   This happens when the stated row does not contain the same number of columns as declared at the top of the list-table via the ``:widths:`` property.

   Solution: Double-check the columns declared at the top of the list-table vs. the number of columns declared in each row in the table.

**WARNING: Inline strong start-string without end-string**
   This often is because a word (or string) has been applied bold elements (starting and ending double-asterisk) incorrectly.

   Solution: Find the row stated in the error message. This may be in a paragraph, a column in a table, or any other area where paragraph-level content is acceptable in the topic. Look for a bolded string that has spaces immediately before or after the double-asterisk. For example:

   .. code-block:: none

      ** string**

   or:

   .. code-block:: none

      **string **

**WARNING: "list-table" widths do not match the number of columns in table**
   This happens when there is a mismatch between the number of columns declared at the top of the list-table via the ``:widths:`` property vs. the number of columns declared somewhere else in the table.

   Solution: Double-check the columns declared at the top of the list-table vs. the number of columns declared in each row in the table.

**WARNING: Pygments lexer name u'' is not known**
   This happens when the lexer name is misspelled or does not exist.

   .. note:: Only use the supported formatting options for code blocks.

   Solution: Verify the name of the code-block formatting option specified in the code block. For example:

   .. code-block:: rst

      .. code-block:: python

   If the name has a typo:

   .. code-block:: rst

      .. code-block:: pythom

   you will see a warning like this: `Pygments lexer name u'pythom' is not known`


**WARNING: toctree contains reference to nonexisting document u'FILENAME'**
   This happens when a topic is added to the ``toctree`` list in the ``index.rst`` file, but does not exist in the ``/source`` directory.

   Solution: Verify the list of files in the ``/source`` directory. Look for typos in both the ``toctree`` list and the list of files or some other type of mismatch. Use lowercase characters for filenames and ``toctree`` lists.





WARNING: Explicit markup ends without a blank line; unexpected unindent.

**WARNING: undefined label: <label-name> (if the link has no caption the label must precede a section header)**
   This happens when there is no space between the anchor reference and the header title. This warning is often accompanied by another warning:

   **WARNING: Explicit markup ends without a blank line; unexpected unindent.**

   Solution: Find the label name specified by ``<label-name>`` and verify the formatting for the anchor reference and the following header. For example, this will break:

   .. code-block:: rst

      .. _format-content-admonitions:
      Admonitions
      ==================================================

   because there is not a blank line between the anchor reference and the section title. This will not break:

   .. code-block:: rst

      .. _format-content-admonitions:

      Admonitions
      ==================================================





.. sphinx-errors-warnings-end


.. _sphinx-theme-errors:

Theme Issues
==================================================

.. sphinx-theme-issues-start

When running Sphinx, you may see the following issues that are related to the Sphinx theme:

**Reason: TemplateSyntaxError("expected token ':', got ','",)**
   This is because the ``nav-docs.html`` file for the topic collection is malformed.

   Solution: The ``nav-docs.html`` file can be tricky, in part because it looks like JSON, but also because it's part of a Jinja template that is only fully rendered during a Sphinx build. The various structures within the ``nav-docs.html`` file are important and they are particular.

   Examine the structure of the ``nav-docs.html`` file, especially with regard to very recent changes. If there are missing or misplaced characters (square brackets, curly brackets, quotes, colons, commas, etc.) the file may not be renderable and you will get a syntax error when the character isn't the one that is expected.

   .. note:: Sphinx generally will not tell you *where* in the ``nav-docs.html`` file the error is. You will have to examine the file, starting with the areas in which you most recently made changes.

.. sphinx-theme-issues-end

