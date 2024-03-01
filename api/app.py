from flask import Flask, request, Response, session, jsonify
from lib.user_repository import UserRepository
from lib.user import User
from lib.db import get_flask_database_connection
from lib.question_repository import QuestionRepository
from lib.question import Question
from routes.user import route_user
from routes.stat import route_stat

import json
import secrets

app = Flask(__name__)
app.secret_key = b'secretkey'
app.register_blueprint(route_user)
app.register_blueprint(route_stat)

# routes for quiz functionality
@app.route('/questionrange', methods=['GET'])
def get_quiz_range():
    connection = get_flask_database_connection(app)
    repository = QuestionRepository(connection)
    question_range = repository.determine_range()
    if question_range:
        return jsonify({"number": question_range})
    else:
        return jsonify({"error": "No question found"})

@app.route('/quizgame', methods=['GET'])
def get_quiz_questions():
    id = request.args.get('id')
    connection = get_flask_database_connection(app)
    repository = QuestionRepository(connection)
    question_dict = repository.find(id)
    if question_dict:
        return jsonify(question_dict.to_dict())
    else:
        return jsonify({"error": "No question found"})