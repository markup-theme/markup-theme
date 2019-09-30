.. THIS PAGE IS LOCATED AT THE /slides/ PATH.

================================================
About Slide Decks
================================================

.. revealjs::

 .. revealjs:: Slide Decks using the MARKUP Theme
    :noheading:
    :data-transition: none

    .. image:: ../../images/slides_splash.png

    .. rv_note:: 

       This is a speaker note. Hit "s" on the keyboard to view them.

 .. revealjs:: What are slide decks?
    :data-transition: none

    Slide decks built from with the MARKUP theme can build simple reveal.js presentations using the same authoring and build processes as the MARKUP theme

 .. revealjs:: Some Slide Basics
    :data-transition: none

    Slides use a very small subset of the Sphinx directive set: 

    * Paragraphs, including **bold**, *italics*, and ``code``
    * Ordered and unordered lists
    * Fully qualified URLs
    * Code blocks, both by themselves and within ordered lists
    * Images
    * Notes, warnings
    * Fragments, which load part of a slide page
    * Speaker notes via ``rv_note`` directive. Hit the "s" key on the keyboard to view speaker notes.

    .. rv_note:: This is a speaker note.

 .. revealjs:: Code Blocks
    :data-transition: none

    Code blocks use the same directives as the reStructuredText pages. For example, YAML code:

    .. code-block:: yaml

       section:
         property: value
         etc...

 .. revealjs:: Fragments
    :data-transition: none

    .. rst-class:: fragment

       Hit the next arrow...

       .. raw:: html

          <ol>
          <li class="fragment"><code>fragment one</code></li>
          <li class="fragment"><em>fragment two</em></li>
          <li class="fragment"><strong>fragment three</strong></li>
          </ol>

 .. revealjs:: Images
    :data-transition: none

    .. image:: ../../images/busycorp.png

 .. revealjs:: Notes and Warnings
    :data-transition: none

    Notes and warnings! (Use sparingly.)

    .. note:: This is a note.

    .. warning:: This is a warning!

    (You can use other admonitions as well.)

 .. revealjs:: Speaker Notes
    :data-transition: none

    You can use speaker notes by adding the ``.. rv_note::`` directive to a slide.

    Hit "s" on your keyboard to view the notes.

    .. code-block:: none

       .. rv_note:: 

          This is a speaker note. You found this from your keyboard's "s" key.

 .. revealjs:: What else?
    :data-transition: none

    Slide decks can use most of the formatting available to reStructuredText authoring. The CSS for the slide decks is more sparse than the CSS for the Markdown and reStructuredText pages, but still shares a similar look and feel.

 .. revealjs:: Questions?
    :data-transition: none

    .. image:: ../../images/slides_questions.png

 .. revealjs:: Let's Hack!
    :data-transition: none

    .. image:: ../../images/slides_hack.png


