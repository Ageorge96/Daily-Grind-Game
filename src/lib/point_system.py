from api.lib.stat_repository import StatRepository

class PointSystem:
    def __init__(self, user_id: int, user_type_level: int, score: int, game_type: str):
        self.user_id = user_id
        self.user_type_level = user_type_level
        self.score = score
        self.game_type = game_type

    def tally_experience(self):
        pass
    
    def tally_money(self):
        pass

    def add_to_user_history(self):
        statRepo = StatRepository()