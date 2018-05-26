
from zope import component

from ctrl.core.extension import CtrlExtension
from ctrl.core.interfaces import (
    ICommandRunner, ICtrlExtension,
    ICtrlConfig, ISubcommand)

from .config import ComposeConfig

from .command import ComposeSubcommand


class CtrlComposeExtension(CtrlExtension):

    @property
    def requires(self):
        return ['config', 'command']

    def register_adapters(self):
        component.provideAdapter(
            factory=ComposeSubcommand,
            adapts=[ICommandRunner],
            provides=ISubcommand,
            name='compose')

    async def register_utilities(self):
        config = ComposeConfig()
        await config.load()
        component.provideUtility(
            config,
            provides=ICtrlConfig,
            name='compose')


# register the extension
component.provideUtility(
    CtrlComposeExtension(),
    ICtrlExtension,
    'compose')
