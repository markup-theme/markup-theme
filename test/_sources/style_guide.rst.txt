.. 
.. xxxxx
.. 



==================================================
Style Guide
==================================================

.. note:: This is a sample style guide. You might not like it! If that's the case, update this to be whatever you'd want your style guide to be.

This topic is a placeholder style guide for |theme| and contains a collection of #protips for working with |theme|. Refer to the `Google Developer Documentation Style Guide <https://developers.google.com/style/>`__ for anything not listed here. Use this topic as a starting place for a real style guide to use with your own project(s).


.. _style-guide-code-blocks:

Code Blocks
==================================================

.. style-guide-code-blocks-start

Code blocks show code, commands, scripts, data tables, configuration files, and more. Sphinx parses code blocks using a library called Pygments, which validates the structure in the code block against what would be reasonably expected for that code type. Highlighting is applied to the built code block by Pygments CSS.

Indentation Patterns
--------------------------------------------------
Use a two-character indendation pattern for code blocks as often as possible, even if this violates some arbitrary rule advocated by proponents of that coding language.

For most code block types this is easy. For example, Python:

**Do this**

.. code-block:: python

   subsample = maybe.load_table(
     path='filename.csv',
     column=True)
   maybe.get_name(column)

**Not this**

.. code-block:: python

   subsample = maybe.load_table(path='filename.csv',
                                column=True)
   maybe.get_name(column)


Command Lines
--------------------------------------------------
With command lines it can be more difficult. But we should still take a presentation-first approach. Super-long command lines will never look good :(.

**Do this**

.. code-block:: console

   $ service add --name="s3" --type="s3" bucket="company_bucket" \
   aws_access_key_id="KEY" aws_secret_access_key="KEY"


**Not this**

.. code-block:: console

   $ service add --name="s3" --type="s3" bucket="company_bucket" aws_access_key_id="KEY" aws_secret_access_key="KEY"


.. _style-guide-command-prompts:

Command Prompts
==================================================

.. style-guide-command-prompts-start

Always use the ``$`` symbol at the start of any command a user would enter as a command. We don't differentiate the required role of the user (such as "administrator") via the command prompt symbol. If a specific role is required, introduce that role in preceding text.

.. note:: Only use the ``console`` code block to show command-line prompts.

For example, do this:

.. code-block:: console

   $ sphinx-build -h html /path/to/source /path/to/output

and not:

.. code-block:: console

   sphinx-build -h html /path/to/source /path/to/output

For command prompts that *return* information, do not use the ``$`` for the returned information. For example, do this:

.. code-block:: console

   $ sphinx-build -h html /path/to/source /path/to/output

returns:

.. code-block:: console

   Build succeeded.

.. style-guide-command-prompts-end


.. _style-guide-copypasta:

Copypasta
==================================================

.. style-guide-copypasta-start

Copying and pasting (AKA "copypasta") from non-text file formats, such as Confluence pages and Word documents, may cause you some real pain, especially with quotations, tabs, and other invisible hidden characters. In rare cases after copypasta, the character you see in the text file isn't the character that is actually in the text file. This is super annoying. If you copy/paste from somewhere into files used with |theme|, expect to do some work to clean that up, such as pedantically finding all the curly quotes and replacing them with straight quotes. Or other stuff.

.. style-guide-copypasta-end


.. _style-guide-field-names:

Field Names vs. Field Values
==================================================

.. style-guide-field-names-start

In a user interface, the names of fields and buttons and other elements that users interact with often have names, such as **Subscription ID** or **Custom domain names**. These names will have capitalization, either title case or camel case. In general, technical documentation should follow this pattern when referencing the field names.

However, everything else associated with these names--values, nouns, what-have-yous, and-so-ons!--should not follow this pattern. Instead, write this as normal plain boring words without capitalization or formatting. Zzzzz.

For example:

"Copy the information in the **Subscription ID** and save it for later. You will need the subscription ID to complete the sign-up process."

Or:

"Select the **Custom domain names** tab. You will need to create a custom domain name that uniquely identifies this use of [some product name goes here]."

There are exceptions, of course. Of course there are exceptions! The goal here is to document things using plain language. Save the jargon, extra content formatting, and capitalizations for when it truly matters.

.. style-guide-field-names-end


.. _style-guide-future-features:

Future Features
==================================================

.. style-guide-future-features-start

Avoid trying to document future features or products, even in innocuous ways, but especially in ways that promise functionality that does not (or may never) exist.

.. style-guide-future-features-end


.. _style-guide-gerunds:

Gerunds
==================================================

.. style-guide-gerunds-start

In titles, headers, and navigation elements, an important goal is to create the shortest possible header (that can still be understood and/or followed by the reader). The |theme| rewards the non-use of gerunds in the left-side navigation and in topic titles! Every time you do this, please give yourself a gold star.

.. admonition:: Famous quotes:

   When writing documentation ask yourself "What does the user want or need to do?"

   The answer is never "The user wants to adding a widget."

.. style-guide-gerunds-end



.. _style-guide-glossary:

Glossary
==================================================

.. style-guide-glossary-start

Ideally a glossary should exist. See the :ref:`glossary tutorial <tutorials-glossary>` for how to add a link to a glossary page that is a global element within the left-side navigation.

.. style-guide-glossary-end


.. _style-guide-jargon:

Jargon
==================================================

.. style-guide-jargon-start

Por favor to not use jargon.

.. admonition:: Famous quotes:

   "The use of clear, simple words over needlessly complex ones can actually make authors appear more intelligent."

   Paraphrased from a book by Daniel Oppenheimer titled *Consequences of Erudite Vernacular Utilized Irrespective of Necessity: Problems with Using Long Words Needlessly*.

.. style-guide-jargon-end


.. _style-guide-lists-within-lists:

Lists within Lists
==================================================

.. style-guide-lists-within-lists-start

.. tip:: Anytime you see a list within a list it's a clear sign that content should be broken down into smaller topics. Especially if the list within a list is within a procedure.

Lists within lists add unncessary structure to documentation. These should be avoided.

Any time you run into a situation where a list within a list seems to make sense, the next step is to refactor the structure of the content and/or the information to be presented to remove the secondary list elements. Does a table within the list work better? Sometimes that answer is "Yes." Maybe a different topic structure will solve the problem. Often, that answer is "Yes!".

For example:

**To configure this thing**

#. Configure the thing via the log file:

   #. Open the log file and do something.
   #. Run a command, maybe.

#. Save your work if you want to.

presents better when it's like this:

**Configure via log file**

#. Open the log file and do something.
#. Run a command, maybe.
#. Save your work if you want to.

Or:

**Our favorite random list items**

* We like these ones the best:

  * One.
  * Two.
  * Three.

* But also Four sometimes.

presents better when it's like this:

**Our favorite random list items**

* One.
* Two.
* Three.
* Four (sometimes).

.. style-guide-lists-within-lists-end



.. _style-guide-long-titles-headers:

Long Titles, Headers
==================================================

.. style-guide-long-titles-headers-start

Question: How do I know if my topic titles and/or headers are too long?

Answer #1: If a topic title or header wraps in the right-side navigation.

Answer #2: If a topic title or header, as written in the topic, wraps in the left-side navigation. The left-side navigation is not built automatically. One solution here is to create a shorter entry in the left-side navigation, and then use a longer title or header in the topic.

.. style-guide-long-titles-headers-end




.. _style-guide-oxford-comma:

Oxford (or Serial) Comma
==================================================

.. style-guide-oxford-comma-start

Technical documentation should follow the Google Developer's Style Guide regarding the `use of the Oxford (or serial) comma <https://developers.google.com/style/commas>`__: "In a series of three or more items, use a comma before the final 'and' or 'or.'". 

.. style-guide-oxford-comma-end



.. _style-guide-procedures:

Procedures
==================================================

.. style-guide-procedures-start

Focus procedures on a single goal. For example, if two things can be set up and configured, instead of bifurcating the steps within a procedure just make two procedures.

.. tip:: One way to keep procedures focused is to use no more than 9 steps.

.. style-guide-procedures-end


.. _style-guide-procedures-do:

Do this
--------------------------------------------------

.. style-guide-procedures-do-start

**To set something to yes**

#. Open something.
#. Click on this.
#. Click on that.
#. Choose **yes**.

and

**To set something to no**

#. Open something.
#. Click on this.
#. Click on that.
#. Choose **no**.

.. style-guide-procedures-do-end


.. _style-guide-procedures-not:

Not this
--------------------------------------------------

.. style-guide-procedures-not-start

**To set something**

#. Open something.
#. Click on this.
#. Click on that.
#. Choose one of the following options:

   If (some explanation about why yes) for yes click **yes**.

   If (some explanation about why yes) for no click **no**.

.. style-guide-procedures-not-end





.. _style-guide-screen-shots:

Screen Shots
==================================================

.. style-guide-screen-shots-start

People love screen shots. Or at least think they do. Screen shots can be helpful as part of technical documentation. Some tips:

#. Screen shots should be in SVG and PNG format.
#. Consider how the image will look when printed out.
#. Images should be no larger than ~750px wide. Or less, depending on the output formats and the quality of the image.
#. Images that are published to multiple output formats must be PNG format.
#. Verify that images published to multiple outputs look OK.
#. Use mockup diagrams for full-screen UIs if possible.

.. style-guide-screen-shots-end





.. _style-guide-tables-of-content:

Table of Contents
==================================================

.. style-guide-tables-of-content-start

Table of contents built via the default behavior of the Sphinx ``toctree`` directive is unsupported in |theme| for all output formats. This is because |theme| does not automatically-generate left-side navigation.

.. style-guide-tables-of-content-end



.. _style-guide-tables:

Tables and Columns
==================================================

.. style-guide-tables-start

Tables are a great way to present certain types of information. The most important consideration with regard to tables is not the information you want to put into the table, but rather what the table looks like when you are done.

Put differently:

* Tables need to work for both HTML and print formats.
* Table widths must consider the information that will go into each column, and also the width of the page.
* Contents of table rows must be sensible. For example, a 5-column table. Four of the columns contain short words, port numbers, and error codes. And one of the columns contains a description that's 30 lines long for each row. Is that a good table?

Sometimes it's better to break a table down into subtopics rather than rows. And sometimes it's better to have a table that goes on for 10 pages. It just depends. As long as it looks great when you're finished and the information presents cleanly, then it's probably a good table.

.. style-guide-tables-end




.. _style-guide-tabs:

Tabs vs. Evil
==================================================

.. style-guide-tabs-start

Tabs are evil in an environment that uses reStructuredText. As such, many topics are formatted one whitespace character at a time. This can be annoying when formatting large code blocks and tables, especially if your editor of choice is the console (and not a text editor), but that's the way it is. Tabs may break formatting. Occasionally they may even break a build.

.. note:: Good news! `Developers that use spaces make more money than those who use tabs. <https://stackoverflow.blog/2017/06/15/developers-use-spaces-make-money-use-tabs/>`__ It's on StackOverflow, so it must be true!

.. style-guide-tabs-end



.. _style-guide-text-editor:

Text Editor
==================================================

.. style-guide-text-editor-start

Many text editors, especially those embedded in command shell workflows, tend to create hard wrapping in the documentation similar to:

::

   This is a topic that has a hard wrapping
   at forty characters as an example of
   hard wrapping in documentation. This
   type of formatting technically builds
   fine (mostly), but it can introduce
   some challenges with ensuring that
   Sphinx-authored content builds as
   nicely as we want it to.

From a technical writing perspective, formatting like that is super annoying. Especially when trying to edit that content in a normal text editor. Technical writers often work on multiple topics at the same time (either via tabs in a text editor or in multiple windows) and rely on the text wrapping at the window width so they can actually see, read, and edit the content.

Topics should not wrap at some arbitrary width and should instead wrap with the size of the text editor. Mostly because technical writers do not use the command shell to author and edit topics.

.. admonition:: Recommended Text Editors

   These text editors are good ones:
   
   * `Atom <https://atom.io/>`__
   * `EditPad Pro <https://www.editpadpro.com/>`__
   * `TextMate <https://macromates.com/>`__
   
   There are others, for sure.

.. style-guide-text-editor-end




.. _style-guide-title-vs-sentence-case:

Title vs. Sentence Case
==================================================

.. style-guide-title-vs-sentence-case-start

Only use title case in topic titles, headers, and left-side navigation elements. Everywhere else, use sentence case *even when* an application user interface, internal jargon, non-trademarked third parties use title case. |theme| don't care. Readability is more important than following other people's random rules for capitalization.

Title case, When Used in Paragraphs makes everything look like Jargon and it creates important-seeming Words that are **Not Important**. Software, in particular, is very guilty of using Too Many Capital Letters in the Documentation. Save the capital letters!

tl;dr: Use sentence case everywhere except for topic titles, topic header structures, and left-side navigation.

.. style-guide-title-vs-sentence-case-end

