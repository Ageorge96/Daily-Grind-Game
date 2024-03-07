from lib.user import User

class Screen:
    def __init__(self, width=1000, height=650, user: User=None):
        self.width = width
        self.height = height
        self.theme = 'style/theme.json'
        self.user = user
        