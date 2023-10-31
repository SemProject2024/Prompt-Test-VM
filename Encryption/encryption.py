import hashlib
client='client-secret'
result = hashlib.sha256(client.encode()) 
print("Result: ",result.hexdigest())
final_hash=result.hexdigest()

from cryptography.fernet import Fernet
import cryptography.fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

message = "<your-message-will-be-this~~./askperntqwe>"
password = b"client-secret"
salt = bytes(final_hash.encode())
print("salt",salt)
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=150,
)
key = base64.urlsafe_b64encode(kdf.derive(password))

fernet = Fernet(key)
print("key is ",key)
encMessage = fernet.encrypt(message.encode())

print("original string: ", message)
print("encrypted string: ", encMessage)

decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)



"""import hashlib
client='client-secret'
result = hashlib.sha256(client.encode()) 
print("Result: ",result.hexdigest())

from cryptography.fernet import Fernet
import cryptography.fernet
import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

message = "<your-message-will-be-this~~./askperntqwe>"
key = base64.urlsafe_b64encode(f"b'{result.hexdigest()}'")
fernet = Fernet(key)
print("key is ",key)
encMessage = fernet.encrypt(message.encode())
print("original string: ", message)
print("encrypted string: ", encMessage)
decMessage = fernet.decrypt(encMessage).decode()
print("decrypted string: ", decMessage)
"""
