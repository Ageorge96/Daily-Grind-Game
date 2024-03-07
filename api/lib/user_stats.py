class UserStats:

    def __init__(self, 
            user_id: int, 
            strength_level: int, 
            strength_experience: int,
            intellect_level: int, 
            intellect_experience: int,
            money: int
            ):
        self.user_id = user_id
        self.user_level = strength_level + intellect_level
        self.strength_level = strength_level
        self.strength_experience = strength_experience
        self.intellect_level = intellect_level
        self.intellect_experience = intellect_experience
        self.money = money