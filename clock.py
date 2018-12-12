import datetime
import os
from time import sleep

while True:
    print(datetime.datetime.today().time())
    sleep(0.1)
    os.system("clear")
