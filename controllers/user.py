from cement.core.controller import CementBaseController, expose
from models.User import User
from sqlalchemy.exc import IntegrityError


class UserController(CementBaseController):
    class Meta:
        label = 'user'
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Controller for managing users'
        arguments = [
            (['-n', '--name'],
             dict(action='store', dest='name', help='Name for a new user')),
            (['-e', '--email'],
             dict(action='store', dest='email', help='Email for a new user'))
        ]

    @expose(help="This command creates a new user")
    def create(self):
        name = self.app.pargs.name
        email = self.app.pargs.email

        if name is not None and email is not None:
            self.add_user(name, email)

    def add_user(self, name, email):
        session = self.app.session()
        try:
            new_user = User(name=name, email=email)
            session.add(new_user)
            session.commit()
            self.app.log.info(
                'Successfully added new user with {name} with email {email}'
                    .format(name=name, email=email)
            )
        except IntegrityError:
            self.app.log.error('User with email {email} already exists.'.format(email=email))
            session.rollback()
        except Exception as e:
            print(e)
