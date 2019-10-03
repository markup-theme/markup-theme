.. 
.. /esinsider/ui/
.. 

==================================================
FAQ
==================================================

Some frequently asked questions and some answers:

.. expando::
   :title: **What is the MARKUP theme?**

   |theme| began in ~2014. It was originally built and designed as part of an open source project. The goal was to publish documentation on a corporate website with a similar look and feel as the rest of the corporate branding and in a way that allowed it to be tied more closely to similar types of content (training, support, and so on) that was not authored using Sphinx. This required stripping out much of the default Sphinx behaviors (like previous/next) and led to the de-coupling of the left-side navigation structure from the automatically-built patterns driven by the toctree directive. A way to embed non-automated links to topics alongside topics that existed within the document collection was necessary.

   |theme| has continued to evolve. It's been used in production at 3 different companies, two of which wanted to use Sphinx, but needed something that could publish dozens of different documentation sets in a way that shared the corporate branding look and feel, provided a cohesive structure across the entire collection, and could act as an internal-facing knowledgebase and also as a corporate-branded gateway for a smaller set of customer-facing content. These companies have slower upgrade cycles and require a stable authoring platform measured in years. (This is partly the reason why--for now--|theme| runs on Sphinx 1.8.5. Plans for moving to 2.0.1 are underway.)

   |theme| represents the common subset of customizations that form the basis of how it's been used in the wild. It's published as an open source project not because we expect it to take off and become the most popular theme in the world. Quite the opposite. It doesn't make sense for many engineering and software documentation projects. But we wanted to share the experience and the results. In part to show the possibilities of Sphinx themes and templates, in part to provide something that's usable and can be experienced right now. In addition, there are so few examples out there for customizing and extending Sphinx. So we put some of those in here too.

.. expando::
   :title: **Why is the MARKUP theme opinionated the way it is?**

   |theme| is opinionated the way it is because large technical writing projects are typically built around proprietary (and expensive) content management systems. We don't want to use those, but we still want access to more traditional content management patterns, which Sphinx offers.

   While it's great that so many documentation projects can be automated from source code and that lots of people want to create great documentation, technical writers often see those processes (and the results they create) a bit differently.

   So this theme reflects that. We know that it's unlike many of the other themes out there in the Sphinx ecosystem, but we're fine with that. We wish there were more projects like |theme| in the Sphinx ecosystem so we could make this even better.


