from cement.core.controller import CementBaseController, expose
from sqlalchemy import create_engine


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Controller for running the main app'
        arguments = []

    @expose(help="This command is the base command")
    def default(self):
        self.app.log.info('Inside default command')
