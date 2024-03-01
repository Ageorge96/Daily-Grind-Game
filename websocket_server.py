import asyncio
import websockets

async def handle_connection(websocket, path):
    async for message in websocket:
        if message == "collision":
            print("Collision detected!")
            # Send a WebSocket message back to the client
            await websocket.send("collision_ack")  # You can customize the message as needed

start_server = websockets.serve(handle_connection, "localhost", 8000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
