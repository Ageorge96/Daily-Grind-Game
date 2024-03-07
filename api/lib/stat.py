class Stat:
    def __init__(self, id, user_id, score, game, experience, money, date=None):
        self.id = id
        self.user_id = user_id
        self.score = score
        self.game = game
        self.experience = experience
        self.money = money
        self.date = date