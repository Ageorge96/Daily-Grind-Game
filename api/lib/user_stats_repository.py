from lib.user_stats import UserStats

class UserStatsRepository:

    def __init__(self, connection):
        self._connection = connection

    def find(self, user_id: int):
        query = 'SELECT * FROM user_stats WHERE user_id=%s'
        result = self._connection.execute(query, user_id)

        if result != []:
            user_id = result[0][0]
            strength_level = result[0][2]
            strength_experience = result [0][3]
            intellect_level = result[0][4]
            intellect_experience = result [0][5]
            user_money = result[0][6]

            user_stats = UserStats(
                user_id, 
                strength_level, 
                strength_experience, 
                intellect_level, 
                intellect_experience, 
                user_money
            )

            return user_stats
        
    def add(self, user_stats: UserStats):
        query = 'INSERT INTO user_stats (user_id, user_level, strength_level, strength_experience, intellect_level, intellect_experience, user_money) \
            VALUES (%s, %s, %s)'
        self._connection.execute(query, (
            user_stats.user_id, 
            user_stats.user_level, 
            user_stats.strength_level,
            user_stats.strength_experience,
            user_stats.intellect_level,
            user_stats.intellect_experience,
            user_stats.money))