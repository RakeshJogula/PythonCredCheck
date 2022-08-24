# Import os module
import os
import base64

encoded = base64.b64encode(os.getenv('DB_TOKEN').encode('ascii'))
print(os.getenv('DB_TOKEN'))
print(encoded)
decode = base64.b64decode(encoded).decode("utf-8", "ignore")
print(decode)

