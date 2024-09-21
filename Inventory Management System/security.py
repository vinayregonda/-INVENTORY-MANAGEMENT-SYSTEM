class Security:
    def authenticate(self, username, password, users):
        if username in users and users[username]['password'] == password:
            print(f"User {username} authenticated successfully.")
            return users[username]
        else:
            print(f"Failed login attempt for {username}.")
            return None
