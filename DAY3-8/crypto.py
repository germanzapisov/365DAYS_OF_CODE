from cryptography.fernet import Fernet
import base64
import os
from dotenv import load_dotenv

load_dotenv()

def encryption(msg) -> str:
    """
    encrypts the message for sending to the server
    return: Returns the encrypted text encoded in base64 format.
    """
    fernetmsg = Fernet(os.getenv("FERNET")).encrypt(msg.encode())
    based_msg = base64.b64encode(fernetmsg)
    return based_msg.decode()


def decryption(msg) -> str:
    """
    Client-side text decryption function
    return: Returns the decrypted text.
    """
    unbased_msg = base64.b64decode(msg)
    decrypt_msg = Fernet(os.getenv("FERNET")).decrypt(unbased_msg).decode()
    return decrypt_msg
