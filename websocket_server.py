import asyncio
import websockets

connected_clients = set()

async def handle_connection(websocket, path):

    connected_clients.add(websocket)

    try:
        async for message in websocket:
            points = message
            
            for client in connected_clients:
                await client.send(points) 
    finally:
        connected_clients.remove(websocket)

start_server = websockets.serve(handle_connection, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
