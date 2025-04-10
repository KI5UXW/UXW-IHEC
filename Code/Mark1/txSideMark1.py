#KI5UXW's Ionospheric Height Experiment Contribution
# Transmit Side.

# If on Windows, make sure that automatic time sync is on. 
# Handy guide here: https://www.elevenforum.com/t/windows-time-is-not-syncing-automatically.17871/

# CW Start Message Reads: MSG DE KI5UXW. Ionospheric sounding experiment about to start. Please clear frequency if possible. Experiment repeats every 15 minutes of the hour. Contact KI5UXW, K1FR, or WA5FRF for information.
# CW End Message Reads: MSG DE KI5UXW. Ionospheric sounding experiment completed. Experiment repeats every 15 minutes of the hour. Contact KI5UXW, K1FR, or WA5FRF for information.

import winsound
from datetime import datetime
import time

file = "C:/Users/ervin/UXW-IHEC/AudioFiles/SEQP Test Signal_v5_Science-payload.wav"
messageCWstart = "C:/Users/ervin/UXW-IHEC/AudioFiles/shortStart.wav"
messageCWend = "C:/Users/ervin/UXW-IHEC/AudioFiles/shortEnd.wav"

def mark1TX():
    print("KI5UXW's Ionospheric Height Experiment Contribution.")
    print('Transmit Program Start.')
    timeList = [0, 15, 30, 45]
    print(f"Will transmit every {timeList} of the hour.")
    while 0 == 0:
        myobj = datetime.now()
        while myobj.minute not in timeList:
            myobj = datetime.now()
            time.sleep(1)
            print(myobj)
        winsound.PlaySound(messageCWstart, winsound.SND_FILENAME) #0:19
        winsound.PlaySound(file, winsound.SND_FILENAME) #0:18
        winsound.PlaySound(messageCWend, winsound.SND_FILENAME) #0:19
        # Total duration is 56 seconds.

myobj = datetime.now()
while myobj.second != 0:
    myobj = datetime.now()
    #print(myobj.second)
mark1TX()