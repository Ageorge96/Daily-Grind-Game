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
        exp = data.get('exp')
        money = data.get('money')
        print('Collision detected in Flask!')
        print('exp:', exp)
        print('money:', money)

       
        
        points_collected.set_user(user)
        points_collected.add(points)
        points_collected.add_exp(exp)
        points_collected.add_money(money)
        print("exp collection",points_collected.exp)
        
        return jsonify({'message': 'OK', 'points': points})

@route_game_score.route('/rewards')
def get_points():
    points = int(points_collected.game_points)
    
    user = points_collected.user
    exp = points_collected.exp
    money = points_collected.money

    print("exp_points flask check:", exp)

    points_collected.reset()
    return jsonify({'points': points,
                    'user': user,
                    'exp': exp,
                    'money': money
                    })


