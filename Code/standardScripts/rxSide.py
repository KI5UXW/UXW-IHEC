#KI5UXW's Ionospheric Height Experiment Contribution (UXW-IHEC)
# Receive Side.

# If on Windows, make sure that automatic time sync is on. 
# Handy guide here: https://www.elevenforum.com/t/windows-time-is-not-syncing-automatically.17871/

from datetime import datetime
import time
from time import gmtime, strftime

import sounddevice as sd
from scipy.io.wavfile import write

def mark1RX():
    print("KI5UXW's Ionospheric Height Experiment Contribution.")
    print('RX Program Start')
    timeList = [0, 15, 30, 45]
    while 0 == 0:
        myobj = datetime.now()
        while myobj.minute not in timeList:
            myobj = datetime.now()
            time.sleep(1)
            print(myobj)
        fs = 44100  # Sample rate
        seconds = 58  # Duration of recording
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
        sd.wait()  # Wait until recording is finished
        write(f"{strftime("%Y-%m-%d %H:%M:%S", gmtime())}.wav", fs, myrecording)  # Save as WAV file 

myobj = datetime.now()
while myobj.second != 0:
    myobj = datetime.now()
    #print(myobj.second)
mark1RX()