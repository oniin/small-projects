import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
password = b'password'
salt = os.urandom(16)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=390000,
)

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# mainpwd = input("Enter password: ")
key = load_key() + base64.urlsafe_b64encode(kdf.derive(password))
fer = Fernet(key)


# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)


# key = load_key() + mainpwd.encode()


def view():
    with open('wood.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())



def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open('wood.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True: 
    mode = input("Would you like to add new pw or view existing ones?(add, view):  ").lower()
    if mode == "q":
        break
    
    
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid")
        continue