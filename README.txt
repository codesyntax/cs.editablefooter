================================
cs.editablefooter Package Readme
================================

Overview
========

We've always wanted to edit the footer of Plone providing our
customers' contact info.

We've **always** customized both portal_footer.pt and
portal_colophon.pt in our Plone 2.5.x sites, but now we can hide them
easily hiding plone.footer and plone.colophon viewlets through
@@manage-viewlets or setting a viewlets.xml in an extension profile,
thanks to new viewlet infrastructure in Plone3.

This product creates a new PortletManager shown in the portal.footer
viewletmanager and editable through http://plone/@@manage-footer (a
link is provided in the footer). There you can add any kind of
portlets.

At the time of writing this, is not possible to restrict the type of
the portlets assignable to a portlet manager, so until the
implementation of PLIP #207, this will not be possible.

Then, we can restrict the footer manager to show only, say,
plone.portlet.static type portlets.


Author
======

Mikel Larreategi <mlarreategi@codesyntax.com>
CodeSyntax
2008

Credits
=======

Thanks Martin Aspeli for writing "Professional Plone Development"

Thanks Plone Guys for writing Plone

Thanks ZC for creating Zope



