# Import os module
import os
import base64

encoded = base64.b64encode(b'os.getenv('DB_TOKEN')')
print(os.getenv('DB_TOKEN'))
print(encoded)
b = base64.b64decode(encoded).decode("utf-8", "ignore")
print(decode)

