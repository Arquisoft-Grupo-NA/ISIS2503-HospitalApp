from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
print(key)
print(os.urandom(32))