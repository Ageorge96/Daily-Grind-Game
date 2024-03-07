class CurrentPoints():
    def __init__(self):
        self.game_points = 0
        self.user = None
        self.exp = 0
        self.money = 0

    def set_user(self, username):
        self.user = username

    def add(self, single_points):
        if self.user is not None:
            self.game_points += int(single_points)

    def add_exp(self, exp):
        if self.user is not None:
            self.exp += int(exp)

    def add_money(self, money):
        if self.user is not None:
            self.money += int(money)

    def reset(self):
        self.game_points = 0
        self.user = None
        self.exp = 0
        self.money = 0
