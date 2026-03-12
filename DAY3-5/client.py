import asyncio
import websockets


async def listen(websocket, name):
    """
    Checks for incoming messages,
    if found, immediately displays them to the client
    """
    async for msg in websocket:
        print(f"{msg}")


async def send(websocket):
    """
    asks the user for a message and sends it to another client
    """
    loop = asyncio.get_running_loop()
    while True:
        try:
            msg = await loop.run_in_executor(None, input, 'введите текст:\n')
            await websocket.send(msg)
        except websockets.exceptions.ConnectionClosedOK:
            print("connection is closed")
            await asyncio.sleep(0.5)
            exit()


async def main():
    """
    The main function connects the client to the server
    and activates other functions (listen(), send())
    """
    URI = "ws://localhost:5000"
    async with (websockets.connect
                    ( URI,
                    ping_interval=20,
                    ping_timeout=60)
                as websocket):
        name = input("enter the name: ")
        await websocket.send(f"__name__:{name}")
        await asyncio.gather(listen(websocket, name), send(websocket))


if __name__ == "__main__":
    asyncio.run(main())