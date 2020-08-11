# imports
import time
import os

# ask for countdown time
timer = int(input('Shutdown in X mintues: '))

# loop every 1 minute
for x in range(timer):
    timeleft = timer - x
    print('Time left: ' + str(timeleft))
    time.sleep(60)

# shutdown computer (windows 10)
shutthatshitdown = "shutdown -s -t 1"

print('Shutting down!')
os.system(shutthatshitdown)
