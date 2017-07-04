from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from controllers.user import UserController
from controllers.base import BaseController


defaults = init_defaults('collector', 'daemon')
defaults['collector']['debug'] = True


class Luncher(CementApp):
    class Meta:
        label = 'collector'
        base_controller = 'base'
        config_defaults = defaults
        handlers = [BaseController, UserController]
        extensions = ['json']

with Luncher() as app:

    app.run()
    app.log.debug(app.pargs)
