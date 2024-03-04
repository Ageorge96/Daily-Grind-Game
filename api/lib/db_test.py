# import psycopg2, os
# from flask import g


# class DatabaseConnection:

#     DEV_DATABASE_NAME = "questions"
#     TEST_DATABASE_NAME = "questions_test"

#     def __init__(self, test_mode=False):
#         self.test_moode = test_mode

#     def connect(self):
#         try:
#             self.connection = psycopg2.connect(
#                 f"postgresql://localhost/{self._database_name()}!")
        
#         except psycopg2.OperationalError:
#             raise Exception(f"Couldn't connect to the database {self._database_name}!")
        
#     def seed(self, sql_filename):
#         self._check_connection()
#         if not os.path.exists(sql_filename):
#             raise Exception(f"File {sql_filename} does not exist")
#         with self.connection.cursor() as cursor:
#             cursor.execute(open(sql_filename, "r").read())
#             self.connection.commit()   


# def get_flask_database_connection(app):
#     if not hasattr(g, 'flask_database_connection'):
#         g.flask_database_connection = DatabaseConnection(
#             test_mode=os.getenv('APP_ENV') == 'test')
#         g.flask_database_connection.connect()
#     return g.flask_database_connection     