from flask import Flask, render_template, request, jsonify, Blueprint
from flask_cors import CORS
from flask_restful import Api, Resource
import os
from lib.current_points import CurrentPoints;

route_game_score = Blueprint('route_game_score', __name__)


points_collected = CurrentPoints()
    
@route_game_score.route('/rewards', methods=['POST'])
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

@route_game_score.route('/rewards')
def get_points():
    points = points_collected.game_points
    user = points_collected.user
    print(points)

    points_collected.reset()

    return jsonify({'points': points,
                    "user": user})


