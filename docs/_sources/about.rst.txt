.. 
.. xxxxx
.. 



==================================================
About |theme|
==================================================

.. include:: index.rst
   :start-after: .. index-markup-intro-start
   :end-before: .. index-markup-intro-end


.. _about-markup-why:

Why |theme|?
==================================================

Sphinx is a great tool that is mostly used for software engineering projects and is typically focused on documentating a single tool or application.

Sphinx is also a great tool that can handle many other types of technical writing projects and can scale beyond documenting a single tool or application.

|theme| exists to provide an alternative to default Sphinx behaviors and navigation patterns found in all of the currently available (and popular!) themes.

|theme| is designed to provide a navigation structure that supports multiple sites within the same cohesive navigation spaces, built with the idea that content that exists within a single document collection can also be reused across any of the others.

In many ways, |theme| is targeted for use by technical writers (and technical writing teams) and is designed to support documenting many tools and applications.


.. _about-markup-goals:

Goals
==================================================

* Enable support for multiple documentation projects within the same site design and user experience
* Separate most navigation elements from the built-in toctree behavior so they may be tailored to your audience
* Provide parity output (same look and feel) for HTML, PDF, and RevealJS presentations as much as possible
* Provide output that can be easily integrated into your company's public-facing or internal-facing websites
* Extend easily. Customize the navigation, add CSS support for new elements, change the colors and add your brand
* Focus on a useful subset of formatting options
* Open source licensed. You may use it for free and may customize it however you want; some components of |theme| are pulled in from other open source projects.
* Support the Commonmark Markdown standard via a plugin; this plugin enables side-by-side use of reStructuredText and Markdown and gives Markdown pages access to the docutils library


.. _about-markup-non-goals:

Non-goals:
==================================================

* Be as cool as all of the various Markdown projects
* Support any non-Commonmark approach to Markdown authoring
* Try to be any of the other existing themes for Sphinx
* Focus on formatting options that are not covered in the included reStructuredText or Markdown formatting guides; they probably all work, but may need some CSS support to look nice
* Focus on automatically documenting content from engineering source code
* Focus on non-HTML, PDF, or RevealJS outputs, such as LaTeX, man page, or ePub; you'll likely want to use a different theme for those outputs
