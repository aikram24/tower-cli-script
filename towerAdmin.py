import tower_cli.resources.team
import tower_cli.resources.user
from tower_cli.conf import settings
import json

USERNAME="admin"
PASSWORD="r78rkD6QVd6v"
HOST="10.42.0.42"

def get_teams():
    team_lst = []
    with settings.runtime_values(username=USERNAME, password=PASSWORD, host=HOST):
        try:
            res = tower_cli.resources.team.Resource()
            json_obj = json.dumps(res.list()['results'])
            i = 1
            for team in res.list()['results']:
                team_lst.append("{} - {}".format(i, team['name']))
                # print("{} - {}".format(i, team['name']))
                i=i+1
        except Exception as e:
            return e
        
    return team_lst


def get_users():
    user_lst = []
    with settings.runtime_values(username=USERNAME, password=PASSWORD, host=HOST):
        try:
            res = tower_cli.resources.user.Resource()
            for user in res.list()['results']:
                user_dict = {}
                user_dict.update({"username": user['username'], "first_name": user['first_name'], "last_name": user['last_name'], "email": user['email']})
                user_lst.append(user_dict)
        except Exception as e:
            return e
    return user_lst

print(get_teams())
print(get_users())