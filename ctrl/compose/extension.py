
from zope import component

from ctrl.core.interfaces import (
    ICommandRunner, ICtrlConfig, ISubcommand)

from .config import ComposeConfig

from .command import ComposeSubcommand


class CtrlComposeExtension(object):

    @property
    def requires(self):
        return ['config', 'command']

    async def register(self, app):
        config = ComposeConfig()
        await config.load()
        component.provideUtility(
            config,
            provides=ICtrlConfig,
            name='compose')

        component.provideAdapter(
            factory=ComposeSubcommand,
            adapts=[ICommandRunner],
            provides=ISubcommand,
            name='compose')
