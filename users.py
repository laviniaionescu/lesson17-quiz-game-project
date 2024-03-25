import json


def add_user(player_id: str, all_players: dict, path: str = "users.json") -> dict:
    full_name = input("Insert your name (optional): ")
    full_name = player_id if full_name == "" or not full_name.isalnum() else full_name
    passwd = ""
    confirm_passwd = " "

    while len(passwd) < 3:
        while passwd != confirm_passwd:
            passwd = input("Insert your password: ")
            confirm_passwd = input("Confirm password: ")
        if len(passwd) < 3:
            print("Password is too short!")
            passwd = ""
            confirm_passwd = " "

    new_user = {player_id: {"full_name": full_name, "high_score": 0, "password": passwd}}
    all_players.update(new_user)

    with open(path, "w") as f:
        f.write(json.dumps(all_players, indent=4))

    return new_user

def login(path: str = "users.json"):
    is_new_user = False
    new_user = {}
    user = input("Login: ")
    with open(path, "r") as f:
        users = json.loads(f.read())

    if user not in users:
        user_pick = input("User does not exist. Do you want to sign up as new player? Y/N: ")
        if user_pick.lower() == 'y':
            new_user = add_user(player_id=user, all_players=users)
            is_new_user = True
        else:
            while user not in users:
                user = input("Login, the user does not exist: ")

    if not is_new_user:
        passwd = input("Insert password: ")
        counter = 0
        while passwd != users[user]["password"]:
            passwd = input("Wrong password, insert password again: ")
            counter += 1
            if counter == 3:
                raise Exception("Password inserted too many times!")

    else:
        return new_user

    return {user: users[user]}
