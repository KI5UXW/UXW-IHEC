#KI5UXW's Ionospheric Height Experiment Contribution
# Receive Side.

# If on Windows, make sure that automatic time sync is on. 
# Handy guide here: https://www.elevenforum.com/t/windows-time-is-not-syncing-automatically.17871/

def runRX(timesPerHour):
    timeRX = timesPerHour / 60
    if timeRX < 3:
        print('ERROR: Transmits too often. Please try again.')
        return
    pass