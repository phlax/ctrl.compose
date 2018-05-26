
from zope import component, interface

from ctrl.core.interfaces import (
    ISettings, ISubcommand, ISystemctl)


@interface.implementer(ISubcommand)
class ComposeSubcommand(object):

    def __init__(self, context):
        self.context = context

    async def handle(self, *args, **kwargs):
        print('Running compose subcommand!')
        await self.start_systemd()

    @property
    def config(self):
        return component.getUtility(ISettings)

    @property
    def services(self):
        sections = [
            s for s
            in self.config
            if s.startswith('service:')]
        for section in sections:
            yield section[8:]

    async def start_systemd(self):
        systemctl = component.getUtility(ISystemctl)
        print(await systemctl.daemon_reload())
        if 'zmq-publish' in self.config['controller']:
            await systemctl.start('zmq-publish.service')
        if 'zmq-listen' in self.config['controller']:
            await systemctl.start('zmq-rpc--proxy.socket')
        for name in self.services:
            print('Starting socket for: %s' % name)
            print(await systemctl.start(
                'controller-%s--proxy.socket'
                % name))
