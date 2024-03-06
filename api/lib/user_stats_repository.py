from lib.user_stats import UserStats

class UserStatsRepository:

    def __init__(self, connection):
        self._connection = connection

    def find(self, user_id: int):
        query = 'SELECT * FROM user_stats WHERE user_id=%s'
        result = self._connection.execute(query, [user_id])

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
            VALUES (%s, %s, %s, %s, %s, %s, %s)'
        self._connection.execute(query, [
            user_stats.user_id, 
            user_stats.user_level, 
            user_stats.strength_level,
            user_stats.strength_experience,
            user_stats.intellect_level,
            user_stats.intellect_experience,
            user_stats.money])
        
    def add_experience(self, user_id: int, experience: int, game_type: str):
        # get users stats
        # add experience to type level
        # check for level up
            # if level up, increment level and reset experience to 0(add remaining exp)
        user_stats = self.find(user_id)
        add_experience_to = game_type + '_experience'
        type_level = game_type + '_level'

        experience_gain_total = int(experience) + getattr(user_stats, add_experience_to)

        current_level_max = 100 + (getattr(user_stats, type_level) * 20)

        if experience_gain_total >= current_level_max:
            # increment level
            level_up_query = 'UPDATE user_stats SET %s = %s + 1 WHERE user_id=%s'
            self._connection.execute(level_up_query, (type_level, type_level, user_id))

            # reset experience
            reset_experience_query = 'UPDATE user_stats SET %s = 0 WHERE user_id=%s'
            self._connection.execute(reset_experience_query, (add_experience_to, user_id))

            # subract level max from experience gained
            experience_gain_total -= current_level_max

        add_experience_query = 'UPDATE user_stats SET strenght_experience = %s + %s WHERE user_id=%s'
        self._connection.execute(add_experience_query, [ add_experience_to, experience_gain_total, user_id])
        

    def add_money(self, user_id: int, money: int):
        query = 'UPDATE user_stats SET user_money = user_money + %s WHERE user_id=%s'
        self._connection.execute(query, (user_id, money))