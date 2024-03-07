import psycopg2
from flask import g

DB_NAME = 'daily_grind'
DB_USER = 'postgres'

class DBConnection:
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(f'dbname={DB_NAME} user={DB_USER}')
        except psycopg2.OperationalError:
            raise Exception('Connection Error')
    
    def execute(self, query, params=[]):
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description != None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result
                
def get_flask_database_connection(app):
    if not hasattr(g, 'flask_database_connection'):
        g.flask_database_connection = DBConnection()
        g.flask_database_connection.connect()
    return g.flask_database_connection