#! python3
# currentLauncher.py - opens stream for 89.3 The Current in VLC
# switches audio device from default (headphones for me) to second item on list (speakers for me)

import os, pyautogui, time, sys

# launch VLC, increase buffer and open stream from URL
command = r'"C:\Program Files\VideoLAN\VLC\vlc.exe" -vvv --network-caching=10000 --no-embedded-video "http://current.stream.publicradio.org/kcmp.aac"'
os.popen(command)

# give it time to load
time.sleep(2)

# switch audio device
pyautogui.write(["alt", "a", "down", "right", "down", "enter"])

# close
sys.exit()