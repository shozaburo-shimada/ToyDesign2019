# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
#import subprocess
#import sys, os

if __name__ == "__main__":
  ain1 = 13
  ain2 = 15
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ain1, GPIO.OUT)
  GPIO.setup(ain2, GPIO.OUT)
  pwm = GPIO.PWM(ain2, 1000)
  
  GPIO.output(ain1, GPIO.HIGH)

  pwm.start(0)
  time.sleep(1) 
  pwm.ChangeDutyCycle(50)
  time.sleep(1)
  pwm.ChangeDutyCycle(100)
  time.sleep(1)
  pwm.ChangeDutyCycle(0)
  time.sleep(1)
  GPIO.output(ain1, GPIO.LOW)
  pwm.ChangeDutyCycle(100)
  time.sleep(1)
  pwm.ChangeDutyCycle(0)
  GPIO.cleanup()

