from math import floor
import requests

class PointSystem:
    def __init__(self, user_data, score: int, game: str):
        self.user_data = user_data
        self.score = score
        self.game = game
        self.user_stats = self.get_user_stats()


    def get_user_stats(self):
        url = f'http://127.0.0.1:5000/user_stats/find/{self.user_data['user'].id}'

        response = requests.get(url, cookies=self.user_data['session'])

        if response.status_code == 200:
            print('Found user')
            return response.json()
        
        else:
            print('Failed to add record to player\'s history')


    # wood cutting - 25
    # running - 900
    # memory - 40
    # quiz - 65

    # Call on mini-game completion
    def get_rewards(self):
        exp = self.tally_experience()
        money = self.tally_money()
        self.add_to_user_history(exp, money)

        return exp, money

    def tally_experience(self):
        max_score: int
        game_type: str
        type_level: str

        if self.game == 'woodcutting':
            max_score = 25
            game_type = 'strength'
            type_level = self.user_stats['strength_level']
        elif self.game == 'running':
            max_score = 900
            game_type = 'strength'
            type_level = self.user_stats['strength_level']
        elif self.game == 'quiz':
            max_score = 65
            game_type = 'intellect'
            type_level = self.user_stats['intellect_level']
        elif self.game == 'memory':
            max_score = 40
            game_type = 'intellect'
            type_level = self.user_stats['intellect_level']
        else:
            print("Error calculating results - Game not found")

        if type_level != 0:
            reward = floor(((self.score * type_level) / max_score) * 25)
        else:
            reward = floor((self.score/ max_score) * 25)

        # add exp to user
        url = 'http://127.0.0.1:5000/user_stats/experience'
        payload = {'user_id': self.user_data['user'].id, 'experience': reward, 'game_type': game_type}

        response = requests.post(url, payload)

        if response.status_code == 200:
            print('Users account has been updated')
        
        else:
            print('Failed to add record to player\'s history')

        return reward

    
    def tally_money(self):
        max_score: int
        type_level: str

        if self.game == 'woodcutting':
            max_score = 25
            type_level = self.user_stats['strength_level']
        elif self.game == 'running':
            max_score = 900
            type_level = self.user_stats['strength_level']
        elif self.game == 'quiz':
            max_score = 65
            type_level = self.user_stats['intellect_level']
        elif self.game == 'memory':
            max_score = 40
            type_level = self.user_stats['intellect_level']
        else:
            print("Error calculating results - Game not found")

        print(type_level)

        if type_level != 0:
            reward = floor(((self.score * type_level) / max_score) * 100)
        else:
            reward = floor((self.score/ max_score) * 100)

        # add money to user
        url = 'http://127.0.0.1:5000/user_stats/money'
        payload = {'user_id': self.user_data['user'].id, 'money': reward}

        response = requests.post(url, payload)

        if response.status_code == 200:
            print('Users account has been updated')
        
        else:
            print('Failed to add record to player\'s history')
        
        return reward

    def add_to_user_history(self, experience, money):
        url = 'http://127.0.0.1:5000/stat/add'
        payload = {'user_id': self.user_data['user'].id, 'score': self.score, 'game': self.game, 'experience': experience, 'money': money}

        response = requests.post(url, payload)

        if response.status_code == 200:
            return True
        
        else:
            print(response)
            print('Failed to add record to player\'s history')