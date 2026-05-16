from cryptography.fernet import Fernet
from dotenv import load_dotenv
import os

load_dotenv()
f = Fernet(os.getenv("FERNET_KEY").encode())

def encryption(text):
    enText = f.encrypt(text.text().encode())
    return enText


def decryption(enText):
    text = enText.decode().split(":", 1)
    nickname = text[0]
    split_text = text[1]
    msg = f.decrypt(split_text.encode())
    return f"{nickname}: {msg.decode()}"
