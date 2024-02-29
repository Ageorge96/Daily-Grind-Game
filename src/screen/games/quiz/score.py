class Score():
    def __init__(self, game_score = 0):
        self.game_score = game_score

    def add_points(self):
        self.game_score += 5

    def remove_points(self):
        self.game_score -= 7