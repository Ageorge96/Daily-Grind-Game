from lib.question_repository import QuestionRepository
from lib.question import Question

def test_can_questions_be_queried(db_connection):
    db_connection.seed("seeds/questions.sql")
    repository = QuestionRepository(db_connection)
    find_question = repository.find()
    result = str(find_question)
    assert result == result