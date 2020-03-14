#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pybleno import *
import time
import socket
import subprocess

import RPi.GPIO as GPIO
import time

import Adafruit_PCA9685
import time

def init_servo():
  pass

class servo_Class:

  def __init__(self, Channel, ZeroOffset):
    self.Channel = Channel
    self.ZeroOffset = ZeroOffset

    self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
    self.pwm.set_pwm_freq(60)

  def SetPos(self, pos):
    pulse = int((650 - 150) / 180 * pos) + 150 + self.ZeroOffset
    self.pwm.set_pwm(self.Channel, 0, pulse)

# Program start here
if __name__ == "__main__":
  print("Start Test Servo")  

if __name__ == '__main__':
  unazuki = servo_Class(Channel=0, ZeroOffset=-5)
  kubihuri = servo_Class(Channel=1, ZeroOffset=-5)
  mimi = servo_Class(Channel=2, ZeroOffset=-5)
  shippo = servo_Class(Channel=3, ZeroOffset=-5)

  unazuki.SetPos(0)
  kubihuri.SetPos(0)
  mimi.SetPos(0)
  shippo.SetPos(0)

  #Main Loop
  print("Start main loop")
  try:
    while True:
       print('入力してね')
       inputString = input()
       print(inputString)
       servoType = inputString.split()
       print(servoType)
       if servoType[0] == 'a':
          print("ちゃんとaって打てたねえらーい")
          print(int(servoType[1]))
          unazuki.SetPos(int(servoType[1]))
#          print(int((650 - 150) / 180 * servoType[1]) + 150 + self.ZeroOffset)

       elif servoType[0] == 'b':
          print("aじゃねーじゃん")
          kubihuri.SetPos(int(servoType[1]))

       elif servoType[0] == 'c':
          mimi.SetPos(int(servoType[1]))

       elif servoType[0] == 'd':
          shippo.SetPos(int(servoType[1]))

  except KeyboardInterrupt:
    print("\nEnd Happy-chan")
    GPIO.cleanup()
    
