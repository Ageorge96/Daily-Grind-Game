import random
from random import sample
from lib.question import Question

class QuestionRepository:

    def __init__(self, connection):
        self._connection = connection

    def determine_range(self):
        # generate random selection
        query = 'SELECT MAX(id) FROM questions'
        result = self._connection.execute(query)
        highest_value = int(result[0][0])
        random_selection = random.sample(range(0,highest_value), k=1)[0]
        return highest_value

    def find(self, id):
        # get the random question
        question_result = self._connection.execute('SELECT * FROM questions WHERE id = %s',[id])
        if question_result != []:
            id = question_result[0][0]
            question = question_result[0][1]
            options = question_result[0][2]
            answer = question_result [0][3]
        
        return Question(id, question, options, answer)

