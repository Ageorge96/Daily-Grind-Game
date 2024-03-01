from flask import Flask
from routes.user import route_user
from routes.stat import route_stat

app = Flask(__name__)
app.secret_key = b'secretkey'
app.register_blueprint(route_user)
app.register_blueprint(route_stat)