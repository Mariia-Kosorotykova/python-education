from datetime import datetime
import sys
from time import sleep

while True:
    sys.stderr.write(f'{datetime.now()}\n')
    sleep(1)