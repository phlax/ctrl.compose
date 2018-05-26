
import os

from zope import component

import yaml

from ctrl.core.interfaces import ISettings, IShell


class ComposeConfig(object):

    async def load(self):
        ctrl_config = component.getUtility(ISettings)
        shell = component.getUtility(IShell)
        context = ctrl_config['controller']['context']
        os.environ['COMPOSE_CONTEXT'] = context
        self.config = yaml.load(
            await shell.command(
                '/controller/bin/docker-compose',
                'config',
                cwd=context))

    def dump(self):
        pass
