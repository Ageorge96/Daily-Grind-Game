# server.py
from flask import Flask, render_template, request, send_file
from flask_cors import CORS
from flask_restful import Api, Resource
import os

app = Flask(__name__, static_folder = 'static')
CORS(app)
api = Api(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rewards', methods=['GET', 'POST'])
def handle_collision():
    if request.method == 'POST':
        print('Collision detected in Flask!')
        return 'OK'
    else:
        rewards_file_path = os.path.join(app.static_folder, 'rewards.js')
        with open(rewards_file_path, 'r') as file:
            rewards_content = file.read()

        return f'Content of rewards.js: {rewards_content}'

class RewardsResource(Resource):
    def post(self):
        print('Collision detected in Flask!')
        return {'message': 'OK'}

api.add_resource(RewardsResource, '/rewards')

if __name__ == '__main__':
    app.run(debug=True)
