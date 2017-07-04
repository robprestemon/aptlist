from cement.core.controller import CementBaseController, expose
from models.User import User
from sqlalchemy import create_engine


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Controller for running the main app'
        arguments = []

    @expose(aliases=['get-lunch'], help="Group existing users for lunch")
    def default(self):
        try:
            session = self.app.session()
            users = session.query(User).all()
            for user in users:
                print(user.name)

        except Exception as e:
            print(e)