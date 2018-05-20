
from zope import component

from ctrl.core.interfaces import ICtrlExtension
from .extension import CtrlComposeExtension


# register the extension
component.provideUtility(
    CtrlComposeExtension(),
    ICtrlExtension,
    'compose')
