from zope import schema
from zope.interface import Interface

from cs.editablefooter import EditableFooterMessageFactory as _

class IProductLayer(Interface):
    """ Custom interface for our layer """

class IEditableFooter(Interface):
    """ The infterface for the editable footer """

    footer_text = schema.Text(title=_(u'Footer text'),
                              description=_(u'Insert here the HTML that will appear in the footer'),
                              required=False,
                              )
