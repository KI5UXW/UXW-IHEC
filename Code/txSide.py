#KI5UXW's Ionospheric Height Experiment Contribution
# Transmit Side.

# If on Windows, make sure that automatic time sync is on. 
# Handy guide here: https://www.elevenforum.com/t/windows-time-is-not-syncing-automatically.17871/

import winsound
file = "C:/Users/ervin/UXW-IHEC/AudioFiles/SEQP Test Signal_v5_Science-payload.wav"
#os.system("afplay " + file)
#os.system("mpg123 " + file)
winsound.PlaySound(file, winsound.SND_FILENAME)