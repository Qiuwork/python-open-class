import base64
from Crypto.Cipher import AES

src = b'\xe4\xb8\xad\xe5\x9b\xbd\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
print(src.strip(b'\x00').decode('utf8'))