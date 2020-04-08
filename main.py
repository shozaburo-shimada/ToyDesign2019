# -*- coding: utf-8 -*-

import sys
import time
import subprocess
import Adafruit_MPR121.MPR121 as MPR121
import pygame
import serial


if __name__ == "__main__":
  cap = MPR121.MPR121()
  pygame.mixer.init()
  ser = serial.Serial('/dev/ttyS0',250000)

  if not cap.begin():
      print('Error initializing MPR121.  Check your wiring!')
      sys.exit(1)


  print('Press Ctrl-C to quit.')
  last_touched = cap.touched()
  flag_video1 = False
  flag_video2 = False
  flag_video3 = False
  music_num = 3
  flag_music = False

  try:
    while True:

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
              #if i == 0:
                  # 0番目がタッチされた
                  # movie0.mp4を再生
              if i == 1:
                if flag_video2 == True or flag_video3 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video2 = False
                  flag_video3 = False
                if flag_video1 == False:
                  command = "sudo omxplayer --win '0 0 1280 720' video1.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video1 = True 

              if i == 2:
                if flag_video1 == True or flag_video3 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video1 = False
                  flag_video3 = False
                if flag_video2 == False:
                  command = "sudo omxplayer --win '0 0 1280 720' video2.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video2 = True 

              if i == 3:
                if flag_video1 == True or flag_video2 == True:
                  proc.stdin.write('q')
                  proc.stdin.flush()
                  flag_video1 = False
                  flag_video2 = False
                if flag_video3 == False:              
                  command = "sudo omxplayer --win '0 0 1280 720' video3.mp4"
                  proc = subprocess.Popen(command, shell=True, stdin =subprocess.PIPE)
                  flag_video3 = True 

              if i == 4:
                flag_music = True
                if music_num == 3:
                  pygame.mixer.music.load("music1.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 1
                elif music_num == 1:
                  pygame.mixer.music.load("music2.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 2
                elif music_num == 2:
                  pygame.mixer.music.load("music3.mp3")
                  pygame.mixer.music.play(0)
                  music_num = 3

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

          # i番目のポートが、前回までタッチされていて、かつ今回タッチされていない = リリースを検出

          if not current_touched & pin_bit and last_touched & pin_bit:
              print('curr: {:012b}'.format(current_touched))
              print('last: {:012b}'.format(last_touched))

              print('{0} released!\n'.format(i))


      last_touched = current_touched
      time.sleep(0.1)
  except KeyboardInterrupt:
    print("\nEnd program\n")
    #GPIO.cleanup()
    #p.kill()
    #subprocess.call(["kill " + pid], shell=True)
    #sock.close()

