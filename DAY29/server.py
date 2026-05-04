import websockets
import asyncio

clients = {}
async def handler(websocket):
    async for msg in websocket:
        if msg.startswith('__name__'):
            parts = msg.split(' ')
            name = parts[1]
            clients[websocket] = name
            print(name, msg)
        else:
            try:
                for client in clients:
                    if client != websocket:
                        await client.send(f"{name}: {msg}")
            except websockets.exceptions.ConnectionClosedError:
                del clients[websocket]
                print("The client disconnected with an error.")


async def main():
    host='localhost'
    port=5000
    server = await websockets.serve(handler,host,port)
    print("server is running\n")
    await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())