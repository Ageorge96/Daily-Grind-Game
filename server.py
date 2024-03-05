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

        # Use a marker or delimiter to extract the desired content
        start_marker = '/* START REACT COMPONENT */'
        end_marker = '/* END REACT COMPONENT */'

        start_index = rewards_content.find(start_marker)
        end_index = rewards_content.find(end_marker, start_index)

        if start_index != -1 and end_index != -1:
            desired_content = rewards_content[start_index + len(start_marker):end_index]
            return desired_content.strip()
        else:
            return 'Error: Unable to find the desired content in rewards.js'

class RewardsResource(Resource):
    def post(self):
        print('Collision detected in Flask!')
        return {'message': 'OK'}

api.add_resource(RewardsResource, '/rewards')

if __name__ == '__main__':
    app.run(debug=True)
