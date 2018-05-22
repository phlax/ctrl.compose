
import os

from zope import component

import yaml

from ctrl.config.config import Config
from ctrl.config.interfaces import ICtrlConfig
from ctrl.command.interfaces import IShell


class ComposeConfig(Config):

    async def load(self):
        ctrl_config = component.getUtility(ICtrlConfig)
        shell = component.getUtility(IShell)
        context = ctrl_config.config.get('controller', 'context')
        os.environ['COMPOSE_CONTEXT'] = context
        self.config = yaml.load(
            await shell.command(
                '/controller/bin/docker-compose',
                'config',
                cwd=context))

    def dump(self):
        pass
