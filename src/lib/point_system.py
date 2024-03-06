from math import floor
import requests

class PointSystem:
    def __init__(self, user_id: int, user_type_level: int, score: int, game: str):
        self.user_id = user_id
        self.user_type_level = user_type_level
        self.score = score
        self.game = game

    # wood cutting - 25
    # running - 900

    # Call on mini-game completion
    def get_rewards(self):
        exp = self.tally_experience()
        money = self.tally_money()
        self.add_to_user_history()

        return exp, money

    def tally_experience(self):
        max_score: int
        game_type: str

        if self.game == 'woodcutting':
            max_score = 25
            game_type = 'strength'
        elif self.game == 'running':
            max_score = 900
            game_type = 'strength'
        elif self.game == 'quiz':
            game_type = 'intellect'
        elif self.game == 'memory':
            game_type = 'intellect'
        else:
            print("Error calculating results - Game not found")

        reward = floor(((self.score * self.user_type_level) / max_score) * 25)

        # add exp to user
        url = 'http://127.0.0.1:5000/user_stats/experience'
        payload = {'user_id': self.user_id, 'experience': reward, 'game_type': game_type}

        response = requests.post(url, payload)

        if response.status_code == 200:
            print('Users account has been updated')
        
        else:
            print('Failed to add record to player\'s history')

        print(reward)
        return reward

    
    def tally_money(self):
        max_score: int
        game_type: str
        if self.game == 'woodcutting':
            max_score = 25
            game_type = 'strength'
        elif self.game == 'running':
            max_score = 900
            game_type = 'strength'
        elif self.game == 'quiz':
            max_score = 700
            game_type = 'intellect'
        else:
            print("Error calculating results - Game not found")

        reward = floor(((self.score * self.user_type_level) / max_score) * 100)

        # add money to user
        url = 'http://127.0.0.1:5000/user_stats/money'
        payload = {'user_id': self.user_id, 'money': reward}

        response = requests.post(url, payload)

        if response.status_code == 200:
            print('Users account has been updated')
        
        else:
            print('Failed to add record to player\'s history')
        
        print(reward)
        return reward

    def add_to_user_history(self):
        url = 'http://127.0.0.1:5000/stat/add'
        payload = {'user_id': self.user_id, 'score': self.score, 'game': self.game}

        response = requests.post(url, payload)

        if response.status_code == 200:
            return True
        
        else:
            print(response)
            print('Failed to add record to player\'s history')