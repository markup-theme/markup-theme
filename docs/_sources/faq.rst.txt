.. 
.. /esinsider/ui/
.. 

==================================================
FAQ
==================================================

Some frequently asked questions and some answers:

.. expando::
   :title: **What is MARKUP?**

   It's a theme for use with Sphinx, a static site generator for use with documentation projects (and other things).

   |theme| began in ~2014. It was originally built and designed as part of an open source project. The goal was to publish documentation on a corporate website with a similar look and feel as the rest of the corporate branding, but also in a way that allowed it to be tied more closely to types of content that are not typically authored using Sphinx.

   This required stripping out some the default Sphinx behaviors (like previous/next) and led to the de-coupling of the left-side navigation structure from the automatically-built patterns driven by the ``toctree`` directive. A way to embed non-automated links to topics alongside topics that existed within the document collection was necessary.

.. expando::
   :title: **Why is MARKUP like this?**

   |theme| like this because large technical writing projects are typically built using proprietary (and expensive) content management systems. The creators of |theme| didn't want to use those types of tools, but still wanted to be able use more traditional content management patterns. Sphinx offers these things, but needed to bend a little to get there.

   While it's great that so many documentation projects can be automated from source code and that lots of people want to create great documentation, technical writers often see those processes (and the results they create) a bit differently.

   |theme| reflects that.


.. expando::
   :title: **Can I mix Markdown and reStructured Text files?**

   Yes. See the ``/markup_pdf/`` directory in |theme| for an example of how this can work.

   Is it a good idea? Not sure. It's *probably* harder over time to maintain a mixed format collection, especially if it's a large collection for a big serious enterprise software application.

   But mixing them together does work. It might be useful in certain use cases.
