from zope.interface import Interface
from plone.portlets.interfaces import IPortletManager

class IProductLayer(Interface):
    """ Custom interface for our layer """

class IFooterContent(IPortletManager):
    """ We need our own portlet manager for the footer """
