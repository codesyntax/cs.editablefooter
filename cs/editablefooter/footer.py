__version__ = '$Id$'

from zope.component import adapts
from zope.interface import implements
from zope.formlib import form

from plone.app.controlpanel.form import ControlPanelForm
from plone.app.layout.viewlets.common import ViewletBase

try:
    from plone.app.form.widgets.wysiwygwidget import WYSIWYGWidget
    KUPU_WIDGET = True
except ImportError:
    KUPU_WIDGET = False


from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFDefault.formlib.schema import SchemaAdapterBase
from Products.CMFPlone.utils import safe_unicode
from Products.CMFPlone.interfaces import IPloneSiteRoot
from Products.CMFCore.utils import getToolByName

from cs.editablefooter import EditableFooterMessageFactory as _
from cs.editablefooter.interfaces import IEditableFooter
class EditableFooterControlPanelAdapter(SchemaAdapterBase):
    adapts(IPloneSiteRoot)
    implements(IEditableFooter)

    def __init__(self, context):
        super(EditableFooterControlPanelAdapter, self).__init__(context)
        self.portal = context
        pprop = getToolByName(self.portal, 'portal_properties')
        self.context = pprop.site_properties
        self.encoding = pprop.site_properties.default_charset
        self.fprops = pprop.footer_properties

    def get_footer_text(self):
        language = self.portal.REQUEST.get('LANGUAGE', '')
        ida='footer_text_' + language
        text = getattr(self.fprops, ida, u'')
        return safe_unicode(text)

    def set_footer_text(self, value):
        language = self.portal.REQUEST.get('LANGUAGE', '')
        ida='footer_text_' + language
        if value is not None:
            value=value.encode(self.encoding)
        else:
            value=''

        if self.fprops.hasProperty(ida):
            setattr(self.fprops, ida, value)
        else:
            self.fprops.manage_addProperty(ida,value,'text')


    footer_text = property(get_footer_text, set_footer_text)



class EditableFooterControlPanel(ControlPanelForm):
    form_fields = form.FormFields(IEditableFooter)

    if KUPU_WIDGET:
        form_fields['footer_text'].custom_widget = WYSIWYGWidget

    form_name = _(u'Editable footer')
    label = _(u'Editable footer content')
    description = _(u'Enter the content of the footer')


class EditableFooterViewlet(ViewletBase):

    def update(self):
        language = self.request.get('LANGUAGE', '')
        ida='footer_text_' + language
        pprops = getToolByName(self.context, 'portal_properties')
        fprops = pprops.footer_properties
        text = getattr(fprops, ida, u'')

        transforms = getToolByName(self.context, 'portal_transforms', None)
        data = transforms.convertTo('text/x-html-safe',
                                    text,
                                    mimetype='text/html',
                                    context=self.context)
        if data is None:
            self.footer_text = safe_unicode(text)
        else:
            output = data.getData()
            self.footer_text = safe_unicode(output)


    render = ViewPageTemplateFile('footer.pt')
