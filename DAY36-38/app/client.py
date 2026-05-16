import asyncio
import websockets
from messenger_window import *
from encryption import encryption, decryption
from PyQt6.QtWidgets import QLabel
from utils import *

async def send(websocket):
    if text.text():
        success.setText("sent...")
        await websocket.send(encryption(text).decode())
    else:
        success.setText("enter text!")
    success.show()
    await asyncio.sleep(2)
    success.hide()


async def listen(websocket):
    async for msg in websocket:
        print(msg)
        label = QLabel(decryption(msg.encode()))
        label.setFixedHeight(55)
        style_for_messages(label)
        label.show()
        messages_layout.addWidget(label)


def send_message():
    asyncio.create_task(send(websocket_gl))


async def main():
    URI = "ws://localhost:5000"
    window.show()
    async with websockets.connect(URI) as websocket:
        name = input("input the nickname: ")
        await websocket.send(f"__name__ {name}")
        global websocket_gl
        websocket_gl = websocket
        print("client is running")
        asyncio.create_task(listen(websocket))
        while True:
            app.processEvents()
            await asyncio.sleep(0.01)


if __name__ == "__main__":
    button.clicked.connect(send_message)
    asyncio.run(main())
