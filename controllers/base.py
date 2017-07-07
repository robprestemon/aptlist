from cement.core.controller import CementBaseController, expose
from models.User import User
from models.Group import Group
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

            # Randomly shuffle users before grouping
            shuffle(users)

            # set up empty list for groups
            groups = []

            # set initial start index for slicing the user list
            start_index = 0

            while num_users > 0:
                # If number is divisible by 5, or remainder is greater than 3, use 5 as base size
                # The >= 5 is necessary since num % 5 returns the numerator as the result
                if num_users >= 5 and (num_users % 5 == 0 or num_users % 5 >= 3):
                    group_size = 5
                # Repeat for 4
                elif num_users >= 4 and (num_users % 4 == 0 or num_users % 4 >= 3):
                    group_size = 4
                else:
                    group_size = 3

                user_group = users[start_index:group_size + start_index]
                groups.append(user_group)

                # increase the start index by the current group size
                start_index += group_size
                # decrease the number of users by the current group size to allow loop to end
                num_users -= group_size

            for group in groups:
                new_group = Group()
                for user in group:
                    new_group.users.append(user)
                session.commit()
                print(group, '\n')

        except Exception as e:
            self.app.log.error(e)