import asyncio
import websockets
from crypto import encryption, decryption


async def listen(websocket, name):
    """
    Checks for incoming messages,
    if found, immediately displays them to the client
    """
    async for msg in websocket:
        new_msg = decryption(msg)
        print(f"Вам сообщение: {new_msg}")


async def send(websocket):
    """
    asks the user for a message and sends it to another client
    """
    loop = asyncio.get_running_loop()
    while True:
        try:
            msg = await loop.run_in_executor(None, input, "введите текст:\n")
            encryption_text = encryption(msg)
            await websocket.send(encryption_text)
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
    while True:
        try:
            async with websockets.connect(URI, ping_interval=20, ping_timeout=60) as websocket:
                name = input("enter the name: ")
                await websocket.send(f"__name__:{name}")
                await asyncio.gather(listen(websocket, name), send(websocket))
        except websockets.exceptions.InvalidURI:
            print("Invalid URI")
            break

        except websockets.exceptions.InvalidHandshake:
            print("Invalid Handshake")
            break

        except ConnectionRefusedError:
            print("Server is not running")
            break

        except websockets.ConnectionClosedError:
            print("reconnecting..for 5 seconds")
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())
