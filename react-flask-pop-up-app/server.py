# server.py
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
import os
from current_points import CurrentPoints

app = Flask(__name__, static_folder = 'static')
CORS(app)
api = Api(app)


points_collected = CurrentPoints()
    
@app.route('/rewards', methods=['POST'])
def handle_collision():
    if request.method == 'POST':
        data = request.json
        points = data.get('points_collected')
        user = data.get('username')
        print('Collision detected in Flask!')
        print('Points:', points)
        print('Username:', user)
        points_collected.add(points)
        points_collected.user = user
        print("game_points flask check:", points_collected.game_points)
        return jsonify({'message': 'OK', 'points': points})

@app.route('/rewards')
def get_points():
    points = points_collected.game_points
    user = points_collected.user

    return jsonify({'points': points,
                    "user": user})

if __name__ == '__main__':
    app.run(debug=True)
