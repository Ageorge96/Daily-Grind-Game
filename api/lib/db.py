import psycopg2
from flask import g
import os

DB_NAME = 'daily_grind'
DB_USER = 'postgres'

class DBConnection():
    
    def connect(self):
        try:
            self.connection = psycopg2.connect(f'dbname={DB_NAME} user={DB_USER}')
        except psycopg2.OperationalError:
            raise Exception('Connection Error')
    
    def execute(self, query, params=[]):
        print(params)
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description != None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result
        
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()

    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'

    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)
                
def get_flask_database_connection(app):
    if not hasattr(g, 'flask_database_connection'):
        g.flask_database_connection = DBConnection()
        g.flask_database_connection.connect()
    return g.flask_database_connection