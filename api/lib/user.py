class User:
    def __init__(self, id, username, password, email=None):
        self.id = id
        self.username = username
        self.password = password
        self.email = email