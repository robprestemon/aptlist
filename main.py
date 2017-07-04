from cement.core.foundation import CementApp
from cement.utils.misc import init_defaults
from controllers.user import UserController
from controllers.base import BaseController
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
    engine = create_engine('postgresql://luncher:getlunch@postgres/luncher')
    app.session = sessionmaker(bind=engine)
    app.run()
