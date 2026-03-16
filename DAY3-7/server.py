import websockets
import asyncio
from datetime import datetime as dt
from config import logger


def timer():
    """
    return: returns the time at the current moment
    """
    time_now = dt.now().strftime("%d.%H.%M.%S")
    return time_now

async def handshake(websocket):
    while True:
        try:
            pong = await websocket.ping()
            await pong
            print("heartbeat-OK")
        except Exception:
            print("connection lost")
        await asyncio.sleep(20)

clients = {}


async def handler(websocket):
    """
    The function adds the user to the set,
    checks whether messages have arrived on the server,
    and sends them to other clients if the user has disconnected.
    It notifies them of this.
    """
    asyncio.create_task(handshake(websocket))
    try:
        msg = await websocket.recv()
        if msg.startswith("__name__:"):
            name = msg.split(":", 1)[1]
            clients[websocket] = name
            logger.debug(f"{name} the user has connected")
        async for msg in websocket:
            print(msg)
            if msg == "/exit":
                logger.info("user disconnected")
                await websocket.close()
                break
            else:
                for c, c_name in clients.items():
                    if msg.startswith("/check"):
                        await c.send("server alive")
                    else:
                        if c != websocket:
                            try:
                                await c.send(f"{msg}")
                            except websockets.ConnectionClosed:
                                clients.pop(c, None)
    except websockets.exceptions.ConnectionClosedOK:
        logger.info("user disconnected")
        clients.pop(websocket, None)

    except websockets.exceptions.ConnectionClosedError:
        logger.info("server-error")

    except websockets.exceptions.ConnectionClosed:
        logger.info("Connection closed")


async def main():
    """
    The main function starts the server on the local host
    and runs the handler() function.
    """
    host = "localhost"
    port = 5000
    server = await websockets.serve(
        handler, host, port, ping_interval=20, ping_timeout=60
    )
    data_server = server.sockets[0].getsockname()
    print(f"{timer()} | server is running")
    logger.debug(f"server is running {data_server}")
    await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
