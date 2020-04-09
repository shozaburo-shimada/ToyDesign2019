# -*- coding: utf-8 -*-

import sys
import time
import subprocess
import Adafruit_MPR121.MPR121 as MPR121
import pygame
import serial
import RPi.GPIO as GPIO

if __name__ == "__main__":

  # Init Motor Control
  ain1 = 13 # Direction
  ain2 = 15 # Enable
  speed = 40
  flag_motor = False
  GPIO.setmode(GPIO.BOARD)
  GPIO.setup(ain1, GPIO.OUT)
  GPIO.setup(ain2, GPIO.OUT)
  pwm = GPIO.PWM(ain2, 1000) # 1kHz

  GPIO.output(ain1, GPIO.HIGH)
  pwm.start(speed)

  # Init music
  pygame.mixer.init()
  music_num = 3
  flag_music = False 
  
  # Init movie
  flag_video1 = False
  flag_video2 = False
  flag_video3 = False

  # Init Serial (Heartbeat)
  ser = serial.Serial('/dev/ttyS0',250000)

  # Init captive
  cap = MPR121.MPR121()
  if not cap.begin():
      print('Error initializing MPR121.  Check your wiring!')
      sys.exit(1)

  last_touched = cap.touched()


  print('Press Ctrl-C to quit.')

  try:
    while True:
      '''
      try:
        hr = ser.read()
        hr = hr.decode()
        hr = ord(hr)
      except:
        print("ofr")
        hr = 150
      print(hr)

      if hr < 70:
        if music_num != 1:
          print("m1")
          pygame.mixer.music.load("music1.mp3")
          pygame.mixer.music.play(0)
          music_num = 1
          flag_music = True
      elif hr < 90 and hr >= 70:
        if music_num != 2:
          print("m2")
          pygame.mixer.music.load("music2.mp3")
          pygame.mixer.music.play(0)
          music_num = 2
          flag_music = True
      elif hr >= 90 and hr <= 110:
        if music_num != 3:
          print("m3")
          pygame.mixer.music.load("music3.mp3")
          pygame.mixer.music.play(0)
          music_num = 3
          flag_music = True
      else:
        print("out of range")
      '''

      #print(ord(hr))
      #time.sleep(1)
      current_touched = cap.touched()

      for i in range(12):

          pin_bit = 1 << i
          
          # i番目のポートが、前回タッチされてなくて、かつ今回タッチされたときだけ = タッチを検出
          if current_touched & pin_bit and not last_touched & pin_bit:
              print('curr: {:012b}'.format(current_touched))
              print('last: {:012b}'.format(last_touched))

              print('{0} touched!\n'.format(i))
              
              # Touch no.1, playback movie no.1
              if i == 1:
                if flag_video2 == True or flag_video3 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video2 = False
                  flag_video3 = False
                if flag_video1 == False:
                  command = "sudo omxplayer --win '0 0 1280 720' video/video1.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video1 = True 

              # Touch no.2, playback movie no.2
              if i == 2:
                if flag_video1 == True or flag_video3 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video1 = False
                  flag_video3 = False
                if flag_video2 == False:
                  command = "sudo omxplayer --win '0 0 1280 720' video/video2.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video2 = True 

              # Touch no.3, playback movie no.3
              if i == 3:
                if flag_video1 == True or flag_video2 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video1 = False
                  flag_video2 = False
                if flag_video3 == False:              
                  command = "sudo omxplayer --win '0 0 1280 720' video/video3.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video3 = True 

              # Toggle music
              if i == 4:
                flag_music = True
                if music_num == 3:
                  pygame.mixer.music.load("music/music1.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 1
                elif music_num == 1:
                  pygame.mixer.music.load("music/music2.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 2
                elif music_num == 2:
                  pygame.mixer.music.load("music/music3.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 3

              # Stop movie and music
              if i == 0:
                if flag_video1 == True or flag_video2 == True or flag_video3 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video1 = False              
                  flag_video2 = False
                  flag_video3 = False
                if flag_music == True:
                  pygame.mixer.music.stop()
                  flag_music = False
                  music_num = music_num -1
                  if music_num == 0:
                    music_num = 3

              # Motor ON/OFF
              if i == 5:
                if flag_motor == True:
                  print('Motor OFF')
                  flag_motor = False
                else:
                  print('Motor ON')
                  flag_motor = True
              
              # Control motor speed +
              if i == 6:
                if flag_motor == True:
                  speed += 20
                  if speed > 100:
                    speed = 100
                  print('Set speed: ' + str(speed))

              # Control motor speed -
	      if i == 7:
                if flag_motor == True:
                  speed -= 20
                  if speed < -100:
                    speed = -100
                  print('Set speed: ' + str(speed))
              

          # i番目のポートが、前回までタッチされていて、かつ今回タッチされていない = リリースを検出
          if not current_touched & pin_bit and last_touched & pin_bit:
              print('curr: {:012b}'.format(current_touched))
              print('last: {:012b}'.format(last_touched))

              print('{0} released!\n'.format(i))

      # Motor Control
      if flag_motor == True:
        # Set Direction
        if speed > 0:
          GPIO.output(ain1, GPIO.HIGH)
        else:
          GPIO.output(ain1, GPIO.LOW)
        # Set Speed
        pwm.ChangeDutyCycle(abs(speed))

      else:
        pwm.ChangeDutyCycle(0)

      # Touch
      last_touched = current_touched
      time.sleep(0.1)

  except KeyboardInterrupt:
    print("\nEnd program\n")
    GPIO.cleanup()
    proc.kill()
    #subprocess.call(["kill " + pid], shell=True)
    ser.close()

