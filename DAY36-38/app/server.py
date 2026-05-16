import asyncio
import websockets


async def handler(websocket):
    async for msg in websocket:
        if msg.startswith("__name__"):
            name = msg.split(" ")
            nickname = name[1]
            clients[websocket] = name
            continue
        else:
            print(msg)
            for c in clients:
                if c != websocket:
                    await c.send(f"{nickname}:{msg}")


async def main():
    host = "localhost"
    port = 5000
    server = await websockets.serve(handler, host, port)
    print("server is running")
    await asyncio.Future()


if __name__ == "__main__":
    clients = {}
    asyncio.run(main())
