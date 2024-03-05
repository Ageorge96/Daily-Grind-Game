from flask import Blueprint, request, Response, session
from api.lib.user_repository import UserRepository
from lib.user_stats import UserStats
# from lib.user_stats_repository import UserStatsRepository
from lib.db import get_flask_database_connection

import json

route_user_stats = Blueprint('route_user_stat/', __name__)

@route_user_stats.route('/user_stats/add', methods=['POST'])
def add_user_stat():
    username = request.form['username']

    connection = get_flask_database_connection(route_user_stats)
    user_repo = UserRepository(connection)

    user = user_repo.find(username)

    if user != None:
        response = {'message': 'Unable to find user'}
        return Response(json.dumps(response), status=400, mimetype='application/json')
    
    else:
        user_stats_repo = UserRepository(route_user_stats)
        user_stats = UserStats(user.id, 0, 0, 0, 0, 0)

        user_stats_repo.add(user_stats)

        response = {'message': 'User stats sucessfully created'}
        return Response(json.dumps(response), status=200, mimetype='application/json')

