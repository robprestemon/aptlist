from cement.core.controller import CementBaseController, expose


class UserController(CementBaseController):
    class Meta:
        label = 'user'
        stacked_on = 'base'
        description = 'Controller for managing users'
        arguments = []

    @expose(help="This command creates a new user")
    def create(self):
        self.app.log.info('Inside create user command')
