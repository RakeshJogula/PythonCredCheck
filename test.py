# Import os module
import os
import base64
import requests

encoded = base64.b64encode(os.getenv('DB_TOKEN').encode('ascii'))
print(os.getenv('DB_TOKEN'))
print(encoded)
decode = base64.b64decode(encoded).decode("utf-8", "ignore")
print(decode)

headers = {'Authorization': 'token ' + os.getenv('DB_TOKEN')}
login = requests.get('https://api.github.com/RakeshJogula', headers=headers)
print(login.json())
