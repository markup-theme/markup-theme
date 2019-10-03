.. 
.. xxxxx
.. 



==================================================
Set up |theme|
==================================================

The |theme| theme is not a plugin for Sphinx and is not installed to your system. Instead, it is downloaded as a complete set of directories and files from GitHub.


.. _setup-required:

Required
==================================================

The |theme| theme requires the following applications to be installed on your machine:

* Sphinx 1.8.5: https://pypi.org/project/Sphinx/1.8.5/.

  .. note:: Newer versions of Sphinx are (currently) unsupported.
* Recommonmark: https://recommonmark.readthedocs.io/en/latest/ (A plugin that enables the use of Markdown that follows the Commonmark standard: http://spec.commonmark.org/.)
* Sass: https://sass-lang.com/ (A tool that enables easy management of CSS.)


.. _setup-recommended:

Recommended
--------------------------------------------------
The |theme| theme recommends the following:

* A good text editor. For example: TextMate (https://macromates.com/), Atom (https://atom.io/), or EditPad Pro (https://www.editpadpro.com/)
* A source code repository: either a local Git repo (https://git-scm.com/) or one hosted at Bitbucket (https://bitbucket.org/), GitHub (https://github.com/), or GitLab (https://about.gitlab.com/)
* The ability to use http://localhost/ as part of the local development process for your documentation project
* Access to a CI/CD environment that can automate builds from your source code repository to a location that can host the static HTML output.
* WeasyPrint: http://weasyprint.org/ (A tool that prints PDFs from HTML output. The |theme| theme does not support LaTeX PDF builds, though you may customize the |theme| theme to support that output behavior.)


.. _setup-download:

Download Theme
==================================================

The |theme| theme can be downloaded from GitHub.

**To download the MARKUP theme**

#. Open https://github.com/markup-theme/markup-theme in a web browser.
#. Click **Clone or download**, and then select **Download ZIP**.
#. Open the downloaded ZIP file and move its contents to a location on your local machine.


.. _setup-environment:

Environment Setup
==================================================

The following setup instructions assume the following:

* You are installing on Mac OS
* You are able to run the `pip` command (for non-Sass applications)
* You are able to install Rubygems (for Sass)

For all other installation scenarios, the steps are similarly easy. Please refer to the linked setup docs for each application for the correct information.

**To set up your MARKUP theme environment**

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

   .. code-block:: text

      from recommonmark.parser import CommonMarkParser
      from recommonmark.transform import AutoStructify

      source_parsers = {
        '.md': CommonMarkParser,
      }

   Change ``source_suffix = '.rst'`` to ``source_suffix = ['.rst', '.md']``.

   At the bottom of the `Options for HTML output` configuration section, add:

   .. code-block:: text

      def setup(app):
      app.add_config_value('recommonmark_config', {
        'enable_eval_rst': True,
      }, True)
      app.add_transform(AutoStructify)

#. `Install WeasyPrint <http://weasyprint.readthedocs.io/en/latest/install.html>`__:

   .. code-block:: console

      $ pip install weasyprint

   and then run ``$ weasyprint --version`` to verify.

   .. note:: In some cases, you will need to make sure that the user running the WeasyPrint installation command can write to the install directory. By default, that requires a command similar to:

      .. code-block:: console

         $ sudo chown -R $USER:admin /usr/local


.. _setup-localhost:

Localhost Setup
==================================================

The |theme| theme must be run as an actual website to ensure certain behaviors, especially for top-level navigation linking, left-side navigation linking, correct highlighting in the left-side navigation. This is true even for local development. You can view any HTML page in any browser to read and verify rendering of formatting elements on the pages themselves---notes, warnings, code blocks, tables, etc.---but linking to other pages and/or using the navigation will not behave correctly. Use localhost to enable correct website behaviors on your local machine.

Mac OS machines have built-in localhost abilities that can be enabled.

**To set up localhost on Mac OS**

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

   and then update ``DocumentRoot`` and ``<Directory`` to have the path to the ``/output`` directory for the |theme| theme:

   .. code-block:: text

      $ DocumentRoot "/path/to/markup_theme/output/"
        <Directory "/path/to/markup_theme/output/">

#. Restart Apache.

   .. code-block:: console

      $ sudo apachectl restart



.. _setup-build:

Build the Theme
==================================================

The |theme| theme includes five documentation projects that are designed to fit together to show the entire output of the |theme| theme, including linked top-level navigation, site-specific left-side navigation, presentations, and PDFs, all built from one source repository, using a common toolset, and with the same user experience.

The |theme| theme has a default structure of:

::

   $markup_theme
   │   _ext
   │   _templates
   │   _themes
   │───docs
   │   ├── ...
   │   ├── md
   │   ├── pdf
   │   ├── rst
   │   ├── slides
   │   images
   │   markup_md
   │   markup_pdf
   │   markup_rst
   │   markup_slides
   │   markup_theme
   │   misc
   │   README.md
   │   shared
   │   tokens


.. _setup-output-directories:

Output Directories
==================================================

The output directories are the locations to which Sphinx will put successfully built files. This section describes how to create an output directory structure named ``/docs`` that exists alongside the document source to enable use for GitHub pages.

.. note:: The output location is specified as a parameter of the ``sphinx-build`` command and, as such, can be any location you want.

#. Create the top-level ``/docs`` directory:

   .. code-block:: console

      $ sphinx-build -b html markup_theme/markup_theme/source/ markup_theme/docs/

#. Create the ``/output/md`` directory:

   .. code-block:: console

      $ sphinx-build -b html markup_theme/markup_md/source/ markup_theme/docs/md/

#. Create the ``/output/rst`` directory:

   .. code-block:: console

      $ sphinx-build -b html markup_theme/markup_rst/source/ markup_theme/docs/rst/

#. Create the ``/output/slides`` directory:

   .. code-block:: console

      $ sphinx-build -b html markup_theme/markup_slides/source/ markup_theme/docs/slides/

#. Create the ``/output/pdf`` directory:

   .. code-block:: console

      $ sphinx-build -b html markup_theme/markup_pdf/source/ markup_theme/docs/pdf/

   This is the directory from which PDFs are printed.

   .. note:: When you are using the |theme| theme, you do not have to use this exact process for building PDFs. What you need to do is build the HTML to a location that is available to the ``weasyprint`` command as a URL. This can at a localhost URL, a local ``file:///`` path, an actual staging URL on an internal corpnet website, a public URL, and so on. The PDF should be built from the source at that URL to a location in the ``/output`` or copied there.

   To print a PDF, assuming the source HTML output is located at ``http://localhost/pdf/`` and is built to that, same directory as a PDF file, for ``md.html``:

   .. code-block:: console

      $ weasyprint http://localhost/pdf/md.html markup_theme/docs/pdf/md.pdf

   Repeat this for ``rst.html``:
   
   .. code-block:: console

     $ weasyprint http://localhost/pdf/rst.html markup_theme/docs/pdf/rst.pdf


This should build a website that looks like this:

.. image:: ../../images/markupproject.png
   :width: 600 px
   :align: center

