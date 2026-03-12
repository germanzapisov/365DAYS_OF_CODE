from cryptography.fernet import Fernet
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def encryption(msg) -> str:
    fernetmsg = Fernet(os.getenv("FERNET")).encrypt(msg.encode())
    based_msg = base64.b64encode(fernetmsg)
    return based_msg.decode()


def decryption(msg) -> str:
    unbased_msg = base64.b64decode(msg)
    decrypt_msg = Fernet(os.getenv("FERNET")).decrypt(unbased_msg).decode()
    return decrypt_msg
