from flask import Flask
from routes.user import route_user
from routes.stat import route_stat
from routes.questions import route_questions
from routes.game_score import route_game_score

import json
import secrets

app = Flask(__name__)
app.secret_key = b'secretkey'
app.register_blueprint(route_user)
app.register_blueprint(route_stat)
app.register_blueprint(route_questions)
app.register_blueprint(route_game_score)

