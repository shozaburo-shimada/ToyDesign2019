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


class ApproachCharacteristic(Characteristic):

    def __init__(self):
        Characteristic.__init__(self, {
            'uuid': APPROACH_CHARACTERISTIC_UUID,
            'properties': ['read', 'notify', 'write'],
            'value': None
        })

        self._value = 0
        self._updateValueCallback = None

    def onReadRequest(self, offset, callback):
        print()
        callback(Characteristic.RESULT_SUCCESS, self._value)

    def onSubscribe(self, maxValueSize, updateValueCallback):
        print('ApproachCharacteristic - onSubscribe')

        self._updateValueCallback = updateValueCallback

    def onUnsubscribe(self):
        print('ApproachCharacteristic - onUnsubscribe')

        self._updateValueCallback = None

    def onWriteRequest(self, data, offset, withoutResponse, callback):
        self._value = data
        global counter
        counter  = int.from_bytes(data, 'big')
        print('Write Request: ' + str(counter))

        callback(Characteristic.RESULT_SUCCESS)

def onAccept(clientAddress):
    print('Accept: ' + clientAddress)

def onDisconnect(clientAddress):
    print('disconnect: ' + clientAddress)

def onStateChange(state):
    print('on -> stateChange: ' + state)

    if (state == 'poweredOn'):
        bleno.startAdvertising('Approach', [APPROACH_SERVICE_UUID])
    else:
        bleno.stopAdvertising()

def onAdvertisingStart(error):
    print('on -> advertisingStart: ' + ('error ' + error if error else 'success'))

    if not error:
        bleno.setServices([
            BlenoPrimaryService({
                'uuid': APPROACH_SERVICE_UUID,
                'characteristics': [
                    approachCharacteristic
                ]
            })
        ])

def init_servo():
  pass

def init_julius():
  p = subprocess.Popen(["sh /home/pi/Documents/ToyDesign2019/HappyChan/julius.sh"], stdout=subprocess.PIPE, shell=True)
  pid = str(p.stdout.read().decode('utf-8'))
  print("Julius PID: " + pid)
  time.sleep(3)
  return p, pid

def init_sock():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))
  return sock

class servo_Class:

  def __init__(self, Channel, ZeroOffset):
    self.Channel = Channel
    self.ZeroOffset = ZeroOffset

    self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
    self.pwm.set_pwm_freq(60)

  def SetPos(self, pos):
    #pos:  -90 ~ 90
    pos = pos + 90
    #pos: 0 ~ 180
    pulse = int((650 - 150) / 180 * pos) + 150 + self.ZeroOffset    
    self.pwm.set_pwm(self.Channel, 0, pulse)


# Response
def response(keyword):
  global cmd
  global flagstate
  global starttime
  global settimer

  print(keyword)
  if flagstate == 0:

    if keyword == '疲れた':
      print('勉強終わったら遊べるぞ！')
      cmd = 100
      unazuki.SetPos(15)
      kubihuri.SetPos(30)

    elif keyword == '眠い':
      print('起きろ！')
      cmd = 110
      unazuki.SetPos(15)
      kubihuri.SetPos(30)

    elif keyword == '終わりにしたい':
      print('終わったら自由だぞ！')
      cmd = 120
      kubihuri.SetPos(15)
      shippo.SetPos(30)

    elif keyword == '遊びたい':
      print('終わるまでだめだ！')
      cmd = 130
      kubihuri.SetPos(15)
      sippo.SetPos(30)

    elif keyword == 'この問題難しい':
      print('がんばって')
      cmd = 140
      kubihuri.SetPos(30)
      shippo.SetPos(30)

#いっかい初期位置に戻す
    elif keyword == '電源オン':
      print('なにかするの？')
      cmd = 10
      unazuki.SetPos(15)
      time.sleep(0.5)
      unazuki.SetPos(0)
      time.sleep(0.5)
      unazuki.SetPos(15)

    elif keyword == 'おはよう':
      print('おはよう')
      cmd = 200
#以下テスト
      unazuki.SetPos(15)
      time.sleep(0.5)
      unazuki.SetPos(0)
      time.sleep(0.5)
      unazuki.SetPos(15)


    elif keyword == '今から勉強するね':
      print('がんばって')
      cmd = 310

    elif keyword == 'がんばるね':
      print('がんばって')
      cmd = 400
      mimi.SetPos(30)
      unazuki.SetPos(30)

    elif keyword == 'あと何分':
      print('弱音を吐くな！')
      cmd = 500
      mimi.SetPos(30)
      unazuki.SetPos(30)
#何秒経過したかがわかる
      print((time.time()-starttime) / 60)
      print('分経過')

    elif keyword == '終わった':
      print('やったー')
      cmd = 600
      mimi.SetPos(30)
      unazuki.SetPos(15)
      shippo.SetPos(30)

    elif keyword == '終わり':
      print('おめでとう！遊ぼう')
      cmd = 610
      mimi.SetPos(30)
      unazuki.SetPos(15)
      shippo.SetPos(30)

    elif keyword == 'フィニッシュ':
      print('グッジョブ！！')
      cmd = 620
      mimi.SetPos(30)
      unazuki.SetPos(15)
      shippo.SetPos(30)

    elif keyword == 'できた':
      print('やったー！')
      cmd = 630
      mimi.SetPos(30)
      unazuki.SetPos(15)
      shippo.SetPos(30)

    elif keyword == '勉強終わったよ':
      print('おつかれさま')
      cmd = 640
      mimi.SetPos(30)

    elif keyword == 'よし':
      print('どうしたの？')
      cmd = 700
      kubihuri.SetPos(30)

    elif keyword == 'なんでもない':
      print('そっか')
      cmd = 710
      kubihuri.SetPos(30)

    elif keyword == 'おやすみ':
      print('また明日ね')
      cmd = 1000
      shippo.SetPos(30)

    elif keyword == 'いただきます':
      print('めしあがれ')
      cmd = 1100
      unazuki.SetPos(45)

    elif keyword == 'お腹空いた':
      print('何が食べたい？') 
      cmd = 1120
      mimi.SetPos(30) 

#言われた時間だけはかる
    elif keyword == '勉強する':
      print('時間はかろうか？')
      cmd = 300
      flagstate = 1

#時間はかるモードに変える
  if flagstate == 1:

  #  if keyword == 'おはよう':
  #    print('こんにちは')

    if keyword == 'にじゅっぷん':
      print('にじゅぷんはかるよ')
      cmd = 20
#現在の時間を取得
      starttime = time.time()
      settimer = 20
      cmd = 77
#音声認識モードに戻す
      flagstate = 0

    elif keyword == 'さんじゅっぷん':
      cmd = 30
      startime = time.time()
      settimer = 30
      cmd = 77
      flagstate = 0

    elif keyword == 'よんじゅうごふん':
      cmd = 45
      starttime = time.time()
      settimer = 45
      cmd = 77
      flagstate = 0

    elif keyword == 'ろくじゅぷん':
      cmd = 60
      starttime = time.time()
      settimer = 60 
      cmd = 77
      flagstate = 0

    else:
  #    print('わかんなかったからもういっかい言って')
      cmd = 78

def notify_task():
  global cmd
  #counter += 1
  approachCharacteristic._value = cmd
  if approachCharacteristic._updateValueCallback:

    print('Sending notification with value : ' + str(approachCharacteristic._value))

    notificationBytes = str(approachCharacteristic._value).encode()
    approachCharacteristic._updateValueCallback(notificationBytes)

  cmd = 0

#def degreetoduty(degree):
#  duty = ((12-2.5)/180)*degree+2.5 
#  return duty

# Global
APPROACH_SERVICE_UUID = '13A28130-8883-49A8-8BDB-42BC1A7107F4'
APPROACH_CHARACTERISTIC_UUID = 'A2935077-201F-44EB-82E8-10CC02AD8CE1'
host = 'localhost'
port = 10500

cmd = 0
flagstate = 0
starttime = 0
settimer = 0

# Program start here
if __name__ == "__main__":
  print("Start Happy-chan")  

  unazuki = servo_Class(Channel=0, ZeroOffset=-5)
  kubihuri = servo_Class(Channel=2, ZeroOffset=-5)
  mimi = servo_Class(Channel=3, ZeroOffset=-5)
  shippo = servo_Class(Channel=8, ZeroOffset=-5)

  unazuki.SetPos(0)
  kubihuri.SetPos(0)
  mimi.SetPos(0)
  shippo.SetPos(0)

#  try:
#    while True:
#      print("45")
#      servo0.SetPos(45)
#      time.sleep(2)
#      servo1.SetPos(45)
#      time.sleep(2)
#      servo2.SetPos(45)
#      time.sleep(2)      
#      servo3.SetPos(45)
#      time.sleep(2)

#      print("90")
#      servo0.SetPos(90)
#      time.sleep(2)
#      servo1.SetPos(90)
#      time.sleep(2)
#      servo2.SetPos(90)
#      time.sleep(2)
#      servo3.SetPos(90)
#      time.sleep(2)

#  except KeyboardInterrupt:
#    print("End PCM9685 test")



  """
  # servo set
  GPIO.setmode(GPIO.BCM)

  gp_out = 2 
  #pin3
  GPIO.setup(gp_out,GPIO.OUT)
  mimi = GPIO.PWM(gp_out,50)
  mimi.start(0.0)

  gp_out = 3
  #pin5
  GPIO.setup(gp_out,GPIO.OUT)
  shippo = GPIO.PWM(gp_out,50)
  shippo.start(0.0)

  gp_out = 4 
  #pin7
  GPIO.setup(gp_out,GPIO.OUT)
  kubihuri = GPIO.PWM(gp_out,50)
  kubihuri.start(0.0)

  gp_out = 18 
  #pin12
  GPIO.setup(gp_out,GPIO.OUT)
  unazuki = GPIO.PWM(gp_out,50)
  unazuki.start(0.0)


  #bot = 2.5 #0度
  #mid = 7.2 #90度
  #top = 12.0 #180度
  """

  # Init BLE  
  approachCharacteristic = ApproachCharacteristic()
  bleno = Bleno()
  bleno.on('stateChange', onStateChange)
  bleno.on('accept', onAccept)
  bleno.on('disconnect', onDisconnect)
  bleno.on('advertisingStart', onAdvertisingStart)
  bleno.start()

  # Init Julius
  p, pid = init_julius()

  # Init Socket
  sock = init_sock()  
  res = ''

  # Init Servo

  print("End initialize")


  #Main Loop
  print("Start voice recognition")
  try:
    while True:

      # Waiting for the end of sentence(='\n.')
      while(res.find('\n.') == -1):
        # Store the data from julius
        res += str(sock.recv(1024).decode('utf-8'))

      word = ''
      for line in res.split('\n'):
        index = line.find('WORD=')
        # print('OK')

        # If there is a word we want to get
        if index != -1:
          line = line[index + 6:line.find('"', index + 6)]
          if line != '[s]':
            word = word + line

        #print(word)

        # Response for keyword
        response(word)

        res = ''

      #BLE Notify
      if cmd != 0:
        notify_task() 

      #timer
      if time.time() - starttime > settimer * 60 and starttime != 0:
        print('経過したよ')
        starttime = 0
        settimer = 0

  except KeyboardInterrupt:
    print("\nEnd Happy-chan")
    GPIO.cleanup()
    p.kill()
    subprocess.call(["kill " + pid], shell=True)
    sock.close()
    
