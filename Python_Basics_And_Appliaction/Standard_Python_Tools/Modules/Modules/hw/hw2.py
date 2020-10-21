import Crypto
import simplecrypt

with open("encrypted.bin", "rb") as inp:
    encrypted = inp.read()

s = ""

with open("passwords.txt", "r") as file:
    for line in file:
        s += line

for password in s.split("\n"):
    try:
        print(simplecrypt.decrypt(password, encrypted))
    except Exception:
        pass


