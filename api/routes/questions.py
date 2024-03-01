from flask import Flask, request, Response, session, jsonify, Blueprint
from lib.db import get_flask_database_connection
from lib.question_repository import QuestionRepository
from lib.question import Question


route_questions = Blueprint('route_questions', __name__)

# routes for quiz functionality
@route_questions.route('/questionrange', methods=['GET'])
def get_quiz_range():
    connection = get_flask_database_connection(app)
    repository = QuestionRepository(connection)
    question_range = repository.determine_range()
    if question_range:
        return jsonify({"number": question_range})
    else:
        return jsonify({"error": "No question found"})

@route_questions.route('/quizgame', methods=['GET'])
def get_quiz_questions():
    id = request.args.get('id')
    connection = get_flask_database_connection(app)
    repository = QuestionRepository(connection)
    question_dict = repository.find(id)
    if question_dict:
        return jsonify(question_dict.to_dict())
    else:
        return jsonify({"error": "No question found"})