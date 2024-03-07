from flask import Blueprint, request, Response, session
from lib.user_stats_repository import UserStatsRepository
from lib.user_repository import UserRepository
from lib.user_stats import UserStats
from routes.user import route_user
# from lib.user_stats_repository import UserStatsRepository
from lib.db import get_flask_database_connection

import json

route_user_stats = Blueprint('route_user_stats/', __name__)

@route_user_stats.route('/user_stats/find/<user_id>', methods=['GET'])
def find_user_stat(user_id):
    
    # user_id = request.args.get('user_id')
    connection = get_flask_database_connection(route_user_stats)
    user_stat_repo = UserStatsRepository(connection)
    user_stats = user_stat_repo.find(user_id)
    # print(response)

    response = {
        'user_id': user_stats.user_id,
        'strength_level': user_stats.strength_level, 
        'strength_experience': user_stats.strength_experience,
        'intellect_level': user_stats.intellect_level, 
        'intellect_experience': user_stats.intellect_experience,
        'money': user_stats.money
    }
    
    return Response(json.dumps(response), status=200, mimetype='application/json') 
    
    # else:
    #     response = {'message': 'You are not logged in'}
    #     return Response(response={json.dumps(response)}, status=400, mimetype='application/json')


@route_user_stats.route('/user_stats/add', methods=['POST'])
def add_user_stat():
    username = request.form['username']

    connection = get_flask_database_connection(route_user_stats)
    user_repo = UserRepository(connection)

    user = user_repo.find(username)

    if user == None:
        response = {'message': 'Unable to find user'}
        return Response(json.dumps(response), status=400, mimetype='application/json')
    
    else:
        connection = get_flask_database_connection(route_user_stats)
        user_stats_repo = UserStatsRepository(connection)
        print(type(user.id))
        user_stats = UserStats(user.id, 0, 0, 0, 0, 0)

        user_stats_repo.add(user_stats)

        response = {'message': 'User stats sucessfully created'}
        return Response(json.dumps(response), status=200, mimetype='application/json')

@route_user_stats.route('/user_stats/experience', methods=['POST'])
def add_experience():
    user_id = request.form['user_id']
    experience = request.form['experience']
    game_type = request.form['game_type']

    connection = get_flask_database_connection(route_user_stats)
    user_stats_repo = UserStatsRepository(connection)

    user = user_stats_repo.find(user_id)

    if user == None:
        response = {'message': 'Unable to find user'}
        return Response(json.dumps(response), status=400, mimetype='application/json')
    
    else:
        user_stats_repo.add_experience(user_id, experience, game_type)

        response = {'message': 'User experience updated'}
        return Response(json.dumps(response), status=200, mimetype='application/json')
    
@route_user_stats.route('/user_stats/money', methods=['POST'])
def add_money():
    user_id = request.form['user_id']
    money = request.form['money']

    connection = get_flask_database_connection(route_user_stats)
    user_stats_repo = UserStatsRepository(connection)

    user = user_stats_repo.find(user_id)
    print('made')

    if user == None:
        response = {'message': 'Unable to find user'}
        return Response(json.dumps(response), status=400, mimetype='application/json')
    
    else:
        user_stats_repo.add_money(user_id, money)

        response = {'message': 'User funds updated'}
        return Response(json.dumps(response), status=200, mimetype='application/json')