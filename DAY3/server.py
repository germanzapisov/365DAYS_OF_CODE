import asyncio
import websockets

async def handler(websocket):
    pass

async def main():
    server = await websockets.serve(handler, 'localhost', 5000)
    print("сервер запущен!")
    await asyncio.Future()

asyncio.run(main())