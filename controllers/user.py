from cement.core.controller import CementBaseController, expose
from models.User import User
from models.Group import Group
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func, desc

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

    @expose(help="This command shows info for a user")
    def show(self):
        email = self.app.pargs.email
        session = self.app.session()
        user = session.query(User.id, User.name, Group.created, Group.id)\
            .join(User.groups) \
            .filter(User.email==email)\
            .order_by(desc(Group.created))\
            .limit(1).one()

        self.app.log.info(user)

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
