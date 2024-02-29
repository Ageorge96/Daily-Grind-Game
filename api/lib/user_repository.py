from lib.user import User

class UserRepository:
    
    def __init__(self, connection):
        self._connection = connection
    
    def find(self, username=None, email=None):
        query = 'SELECT * FROM users WHERE username=%s OR email=%s'
        result = self._connection.execute(query, (username, email))
        
        if result != []:
            id = result[0][0]
            username = result[0][1]
            password = result[0][2]
            email = result [0][3]
            
            user = User(id, username, password, email)
            return user
        
        else:
            return None
    
    def add(self, user:User):
        query = 'INSERT INTO users (username, password, email) VALUES (%s, %s, %s)'
        self._connection.execute(query, (user.username, user.password, user.email,))
        
        