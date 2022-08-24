import os
import sys

user=os.getenv('DB_USERNAME')
password=os.getenv('DB_PASSWORD')
print(user)
print(password)
sys.stdout.flush()
