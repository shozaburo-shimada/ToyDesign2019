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
    pos = pos + 90
    pulse = int((650 - 150) / 180 * pos) + 150 + self.ZeroOffset
    self.pwm.set_pwm(self.Channel, 0, pulse)

# Program start here
if __name__ == "__main__":
  print("Start Test Servo")  

if __name__ == '__main__':
  unazuki = servo_Class(Channel=0, ZeroOffset=-5)
  kubihuri = servo_Class(Channel=2, ZeroOffset=-5)
  mimi = servo_Class(Channel=3, ZeroOffset=-5)
  shippo = servo_Class(Channel=8, ZeroOffset=-5)

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
       if servoType[0] == 'u':
          print("くびたてサーボ")
#          print("ちゃんとaって打てたねえらーい")
#          print(int(servoType[1]))
          unazuki.SetPos(int(servoType[1]))
# u174までできる
#          print(int((650 - 150) / 180 * servoType[1]) + 150 + self.ZeroOffset)

       elif servoType[0] == 'k':
#          print("aじゃねーじゃん")
          print("くびよこサーボ")
          kubihuri.SetPos(int(servoType[1]))

       elif servoType[0] == 'm':
          print("みみサーボ")
          mimi.SetPos(int(servoType[1]))

       elif servoType[0] == 's':
          print("しっぽサーボ")
          shippo.SetPos(int(servoType[1]))

       else:
          print("わからん")

  except KeyboardInterrupt:
    print("\nEnd Happy-chan")
    GPIO.cleanup()
    
