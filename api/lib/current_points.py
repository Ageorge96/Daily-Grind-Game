class CurrentPoints():
    def __init__(self):
        self.game_points = 0
        self.user = ""
    def add(self, single_points):
        self.game_points += single_points
    def reset(self):
        self.game_points = 0