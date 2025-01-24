import time
import os
from dotenv import load_dotenv 

load_dotenv()

api_key = os.environ.get('TOKEN')

print(api_key)


print("test")
time.sleep(3) # Sleep for 3 seconds

print("test -all")
