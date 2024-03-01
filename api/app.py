from flask import Flask, request, Response, session, jsonify
from lib.user_repository import UserRepository
from lib.user import User
from lib.db import get_flask_database_connection
from lib.question_repository import QuestionRepository
from lib.question import Question
from routes.user import route_user
from routes.stat import route_stat
from routes.questions import route_questions

import json
import secrets

app = Flask(__name__)
app.secret_key = b'secretkey'
app.register_blueprint(route_user)
app.register_blueprint(route_stat)
app.register_blueprint(route_questions)

