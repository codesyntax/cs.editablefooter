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

This product adds a new viewlet called cs.editablefooter and it's
added automatically to plone.portalfooter portlet manager

It also creates a new control panel in which you can edit the content
of the viewlet using a Kupu-based WYSIWYG editor.

Dependencies
============

To use the WYSIWYG editor, you must use plone.app.form's
plip200-kupu-widget svn branch. This branch will be merged into
plone.app.form for Plone 3.1.

If you don't want to use this svn code, the control panel will default
to a common textarea.

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



