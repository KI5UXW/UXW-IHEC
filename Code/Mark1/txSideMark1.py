#KI5UXW's Ionospheric Height Experiment Contribution
# Transmit Side.

# If on Windows, make sure that automatic time sync is on. 
# Handy guide here: https://www.elevenforum.com/t/windows-time-is-not-syncing-automatically.17871/

# CW Start Message Reads: MSG DE KI5UXW. Ionospheric sounding experiment about to start. Please clear frequency if possible. Experiment repeats every 15 minutes of the hour. Contact KI5UXW, K1FR, or WA5FRF for information.
# CW End Message Reads: MSG DE KI5UXW. Ionospheric sounding experiment completed. Experiment repeats every 15 minutes of the hour. Contact KI5UXW, K1FR, or WA5FRF for information.

import sounddevice as sd
import soundfile as sf
from datetime import datetime
import time

payloadTrack = 'AudioFiles/SEQP Test Signal_v5_Science-payload.wav'
cwPre = "AudioFiles/shortStart.wav"
cwPost = "AudioFiles/shortEnd.wav"

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
        data, fs = sf.read(cwPre, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()
        data, fs = sf.read(payloadTrack, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()
        data, fs = sf.read(cwPost, dtype='float32')  
        sd.play(data, fs)
        status = sd.wait()  # Wait until file is done playing
        time.sleep(5)
        # Total duration is 56 seconds.

myobj = datetime.now()
print('Running sync with computer clock...')
while myobj.second != 0:
    myobj = datetime.now()
    #print(myobj.second)
mark1TX()