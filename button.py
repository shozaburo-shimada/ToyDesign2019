# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
import subprocess
import sys, os

if __name__ == "__main__":
  pin1 = 7
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(pin1, GPIO.IN, pull_up_down = GPIO.PUD_UP)

  print("taiki")

  flag_playback = False
  while True:
    button1 = GPIO.input(pin1)

    if button1 == False and flag_playback == False:
      command = "sudo omxplayer --win '0 0 480 270' video1.mp4"
      proc = subprocess.Popen(command, shell=True, stdin = subprocess.PIPE)
      print("playback video")  
      flag_playback = True

  print("end")
