from lib.stat import Stat
from datetime import datetime
import time

class StatRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def list(self):
        query = 'SELECT * FROM stats'
        result = self._connection.execute(query)
        
        if result != []:
            stats = []
        
            for row in result:
                id = row[0]
                user_id = row[1]
                score = row[2]
                game = row[3]
                date = row[4]
                
                stat = Stat(id, user_id, score, game, date)
                stats.append(stat)
        
            return stats
        
        else:
            return None
    
    def add(self, stat:Stat):

        timestamp = time.time()
        stat.date = datetime.fromtimestamp(timestamp, tz=None)
        
        query = 'INSERT INTO stats (user_id, score, game, date) VALUES (%s, %s, %s, %s)'
        self._connection.execute(query, (stat.user_id, stat.score, stat.game, stat.date,))
        
        