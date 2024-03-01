from flask import Blueprint, request, Response, session
from lib.user_repository import UserRepository
from lib.user import User
from lib.db import get_flask_database_connection

import json
import secrets

route_user = Blueprint('route_user', __name__)

@route_user.route('/user/login', methods=['POST'])
def user_login():
    if 'token' in session:
        response = {'token': session['token'], 'message': 'Already logged in'}
        return Response(json.dumps(response), status=200, mimetype='application/json') 
    
    else:
        username = request.form['username']
        password = request.form['password']
        
        connection = get_flask_database_connection(route_user)
        user_repo = UserRepository(connection)
        result = user_repo.find(username)
        
        if result != None and password == result.password:
            token = secrets.token_urlsafe(64)
            session['token'] = token        
            response = {'id': result.id, 'username': result.username, 'email': result.email, 'token': token, 'message': 'Succesfully logged In'}
            return Response(json.dumps(response), status=200, mimetype='application/json')
        
        else:
            return Response(response={}, status=400, mimetype='application/json')

@route_user.route('/user/signup', methods=['POST'])
def user_signup():
    if 'token' in session:
        response = {'token': session['token'], 'message': 'Already logged in'}
        return Response(json.dumps(response), status=200, mimetype='application/json') 
    
    else: 
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        
        connection = get_flask_database_connection(route_user)
        user_repo = UserRepository(connection)
        result = user_repo.find(username, email)
        
        if result != None:
            response = {'message': 'User or email already exists'}
            return Response(json.dumps(response), status=400, mimetype='application/json')
        
        else:
            user = User(None, username, password, email)
            user_repo.add(user)
            
            response = {'message': 'Account sucessfully created'}
            return Response(json.dumps(response), status=200, mimetype='application/json')
         
@route_user.route('/user/logout', methods=['GET'])
def user_logout():
    session.pop('token', None)
    return Response(status=200)