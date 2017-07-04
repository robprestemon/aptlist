from cement.core.controller import CementBaseController, expose
from models.User import User
from random import shuffle


class BaseController(CementBaseController):
    class Meta:
        label = 'base'
        description = 'Controller for running the main app'
        arguments = []

    @expose(aliases=['get-lunch'], help="Group existing users for lunch")
    def default(self):
        try:
            # Open DB connection and get all of our users
            # This would not work in a large table
            session = self.app.session()
            users = session.query(User).all()
            num_users = len(users)

            # Set default group size to lowest possible
            group_size = 3

            # If number is divisible by 5, or remainder is greater than 3, use 5 as base size
            if num_users % 5 == 0 or num_users % 5 >= 3:
                group_size = 5
            # Repeat for 4
            elif num_users % 4 == 0 or num_users % 4 >= 3:
                group_size = 4

            self.app.log.info(
                'Creating groups with base size {size}, last group size {extra}'
                              .format(size=group_size, extra=num_users % group_size))

            # Randomly shuffle users before grouping
            shuffle(users)
            groups = list(self.set_groups(users, group_size))

            for group in groups:
                self.app.log.info(group)
                print('\n')

        except Exception as e:
            self.app.log.error(e)

    def set_groups(self, users, group_size):
        """
        Generator that returns groups of group_size from users
        Found this syntax here https://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks
        and modified naming for clarity in our use case
        """
        for i in range(0, len(users), group_size):
            yield users[i:i + group_size]