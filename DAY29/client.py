import websockets
import asyncio

async def send(websocket):
    loop = asyncio.get_running_loop()
    while True:
        msg = await loop.run_in_executor(None, input, 'message:\n')
        await websocket.send(msg)

async def listen(websocket):
    while True:
        msg = await websocket.recv()
        print(f"\n{msg}")


async def main():
    URI = "ws://localhost:5000"
    async with websockets.connect(URI) as websocket:
        name = input("Enter your name to get started:\n")
        await websocket.send(f'__name__ {name}')
        await asyncio.gather(send(websocket), listen(websocket))

if __name__ == "__main__":
    asyncio.run(main())