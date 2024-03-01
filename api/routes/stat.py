from flask import Blueprint, request, Response, session
from lib.stat_repository import StatRepository
from lib.stat import Stat
from lib.db import get_flask_database_connection

import json

route_stat = Blueprint('route_stat', __name__)

@route_stat.route('/stat/list', methods=['GET'])
def stat_list():
    if 'token' in session:
        connection = get_flask_database_connection(route_stat)
        stat_repo = StatRepository(connection)
        stats = stat_repo.list()
        
        response = []
        
        for stat in stats:
            content = {
                'id': stat.id,
                'user_id': stat.user_id,
                'score': stat.score,
                'game': stat.game,
                'date': str(stat.date)
            }
            response.append(content)     
        
        return Response(json.dumps(response), status=200, mimetype='application/json') 
    
    else:
        response = {'message': 'You are not logged in'}
        return Response(response={json.dumps(response)}, status=400, mimetype='application/json')

@route_stat.route('/stat/add', methods=['POST'])
def stat_add():
    if 'token' in session:
        user_id = str(request.form['user_id'])
        score = int(request.form['score'])
        game = str(request.form['game'])
        
        stat = Stat(None, user_id, score, game, None)
        
        connection = get_flask_database_connection(route_stat)
        stat_repo = StatRepository(connection)
        stat_repo.add(stat)
        
        response = {'message': 'Stat succesfully added'}
        return Response(response={json.dumps(response)}, status=200, mimetype='application/json')
        
    else:
        response = {'message': 'You are not logged in'}
        return Response(response={json.dumps(response)}, status=400, mimetype='application/json')
