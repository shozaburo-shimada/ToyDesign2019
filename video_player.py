import subprocess
import time

command = "sudo omxplayer --win '0 0 480 270' video1.mp4"
proc = subprocess.Popen(command, shell=True, stdin = subprocess.PIPE)
print("playback video")

# To wait for waking up omxplayer and skip introduction 
time.sleep(10) 

# Volume Down 5 times
for num in range(5):
  time.sleep(1)
  proc.stdin.write('-')
  proc.stdin.flush()

# Volume Up 5 times
for num in range(5):
  time.sleep(1)
  proc.stdin.write('+')
  proc.stdin.flush()

# Finish
time.sleep(5)
proc.stdin.write('q')
proc.stdin.flush()
print("stop video")
