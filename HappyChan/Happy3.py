#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from pybleno import *
import time
import socket
import subprocess

import RPi.GPIO as GPIO
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
  p = subprocess.Popen(["sh julius.sh"], stdout=subprocess.PIPE, shell=True)
  pid = str(p.stdout.read().decode('utf-8'))
  print("Julius PID: " + pid)
  time.sleep(3)
  return p, pid

def init_sock():
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))
  return sock


# Response
def response(keyword):
  global cmd

  #print(keyword)
  if keyword == '勉強する':
    print('勉強する')
 
  elif keyword == 'いただきます':
    print('めしあがれ')

  elif keyword == 'ごちそうさま':
    print('ごちそうさま')

  elif keyword == '疲れた':
    print('がんばって')
    cmd = 100
    #mimi.ChangeDutyCycle(degreetoduty(30))
    #time.sleep(100)
    #mimi.changeDutyCycle(degreetoduty(30))
    #time.sleep(100)

  elif keyword == '眠い':
    print('起きろ')

  elif keyword == 'お腹空いた':
     print('何が食べたい？') 

  elif keyword == 'この問題難しい':
    print('がんばって')

  elif keyword == '今から勉強するね':
    print('がんばって')

  elif keyword == '勉強終わったよ':
    print('おつかれさま')

  elif keyword == 'おはよう':
    print('おはよう')
    cmd = 200
    #unazuki.ChangeDutyCycle(degreetoduty(30))
    #time.sleep(100)

  elif keyword == 'おやすみ':
    print('また明日ね')



def notify_task():
  global cmd
  #counter += 1
  approachCharacteristic._value = cmd
  if approachCharacteristic._updateValueCallback:

    print('Sending notification with value : ' + str(approachCharacteristic._value))

    notificationBytes = str(approachCharacteristic._value).encode()
    approachCharacteristic._updateValueCallback(notificationBytes)

  cmd = 0

def degreetoduty(degree):
  duty = ((12-2.5)/180)*degree+2.5 
  return duty

# Global
APPROACH_SERVICE_UUID = '13A28130-8883-49A8-8BDB-42BC1A7107F4'
APPROACH_CHARACTERISTIC_UUID = 'A2935077-201F-44EB-82E8-10CC02AD8CE1'
host = 'localhost'
port = 10500

cmd = 0

# Program start here
if __name__ == "__main__":
  print("Start Happy-chan")  

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

  except KeyboardInterrupt:
    print("\nEnd Happy-chan")
    GPIO.cleanup()
    p.kill()
    subprocess.call(["kill " + pid], shell=True)
    sock.close()
    
