# server.py
from flask import Flask, render_template, request, send_file, jsonify
from flask_cors import CORS
from flask_restful import Api, Resource
import os
import json
import websockets
import requests
from current_points import CurrentPoints

app = Flask(__name__, static_folder = 'static')
CORS(app)
api = Api(app)


# WebSocket server address
WEBSOCKET_SERVER = "ws://localhost:8000"

# Function to send points data to WebSocket server
async def send_points_to_websocket(points):
    async with websockets.connect(WEBSOCKET_SERVER) as websocket:
        await websocket.send(json.dumps({'points': points}))

# # Function to send points data to WebSocket server
# def send_points_to_websocket(points):
#     # Create a WebSocket connection to the server
#     ws = WebSocketApp(WEBSOCKET_SERVER)
#     ws.run_forever()

#     # Send points data as a message to the WebSocket server
#     ws.send(points)
#     ws.close()



points_collected = CurrentPoints()
    # Logic to fetch rewards data


@app.route('/rewards', methods=['POST'])
def handle_collision():
    if request.method == 'POST':
        data = request.json
        points = data.get('points_collected')
        
        print('Collision detected in Flask!')
        print('Points:', points)

        points_collected.add(points)

        print("game_points flask check:", points_collected.game_points)

        # send_points_to_websocket(points)
        
        return jsonify({'message': 'OK', 'points': points})

@app.route('/rewards')
def get_points():
    points = points_collected.game_points
    print("")

    return render_template('rewards.html', points=points)


@app.route('/rewards_result')
def get_rewards():
        rewards_file_path = os.path.join(app.static_folder, 'rewards.js')
        with open(rewards_file_path, 'r') as file:
            rewards_content = file.read()
        print("reqards content:", rewards_content)
        # Use a marker or delimiter to extract the desired content
        start_marker = '/* START REACT COMPONENT */'
        end_marker = '/* END REACT COMPONENT */'

        start_index = rewards_content.find(start_marker)
        print("start index :", start_index)
        end_index = rewards_content.find(end_marker, start_index)
        print("end index :", end_index)

        if start_index != -1 and end_index != -1:
            desired_content = rewards_content[start_index + len(start_marker):end_index]
            return desired_content.strip()
        # dictionary : key and points
        else:
            return 'Error: Unable to find the desired content in rewards.js'
        
# # Serve the React component
# @app.route('/rewards_component', methods=['GET'])
# def get_rewards_component():
#     with open('rewards.js', 'r') as file:
#         return file.read()

        


# class RewardsResource(Resource):
#     def post(self):
#         print('Collision detected in Flask!')
#         return {'message': 'OK'}

# api.add_resource(RewardsResource, '/rewards')

if __name__ == '__main__':
    app.run(debug=True)
