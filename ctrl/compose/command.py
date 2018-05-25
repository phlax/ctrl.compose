
from zope import component, interface

from ctrl.core.interfaces import (
    ICtrlConfig, IShell, ISubcommand, ISystemctl)


@interface.implementer(ISubcommand)
class ComposeSubcommand(object):

    def __init__(self, context):
        self.context = context

    async def handle(self, *args, **kwargs):
        print('Running compose subcommand!')
        await self.start_systemd()

    @property
    def config(self):
        return component.getUtility(ICtrlConfig).config

    @property
    def services(self):
        sections = [
            s for s
            in self.config.sections()
            if s.startswith('service:')]
        for section in sections:
            yield section[8:]

    async def start_systemd(self):
        systemctl = component.getUtility(ISystemctl)
        shell = component.getUtility(IShell)
        print(await systemctl.daemon_reload())
        if self.config.has_option('controller', 'zmq-publish'):
            await shell.command(
                'systemctl',
                'start',
                'zmq-publish.service')
        if self.config.has_option('controller', 'zmq-listen'):
            await shell.command(
                'systemctl',
                'start',
                'zmq-rpc--proxy.socket')
        for name in self.services:
            print('Starting socket for: %s' % name)
            print(
                await shell.command(
                    'systemctl',
                    'start',
                    'controller-%s--proxy.socket' % name))
