#Apartment List Test

## Approach to this problem
So as you can tell from the code, I got a little excited with setting up the environment.  I know it wasn't necessary for this particular test but I had been researching about Docker and CLI applications, so I wanted to try it out.

Other than that, I set up basic controllers to manage users and, in the future, persistent groups.  I realized after I set it up, it was way out of scope for the actual problem.

## Dependencies

You should be able to run this program as long as you have Docker and Docker Compose installed.  You may also need Python 3.6 on your host machine.

### Create User
```
sudo docker-compose run luncher python3 main.py user create --email=UNIQUE_EMAIL --name=NAME
```

### Main Command
```
sudo docker-compose run luncher python3 main.py
```

Those are the two commands you'll need to use currently.  Setup the users in the database, then make groups.

### Grouping Function

The heart of the application is the grouping function, I took a pretty simplistic approach.

- Load all users from the database (evident scaling issues there)
- Shuffle the users so it's not the same every week
- Check if the total users are divisible by 5, or have a remainder of 3 or more.  If so, set default group size to 5
- Repeat check for 4 if 5 fails
- Default to group 3
- Do these series of checks while looping over the users and add the right number to the group