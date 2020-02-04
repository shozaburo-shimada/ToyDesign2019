
# -*- coding:utf-8 -*-
import socket
import time
import subprocess
#import pygame.mixer
#import RPI.GPIO as GPIO

host = 'localhost'
port = 10500

# Response
def response(keyword):
  #print(keyword)
  if keyword == '勉強する':
    print('勉強する')
  
  elif keyword == 'いただきます':
    print('めしあがれ')

  elif keyword == 'ごちそうさま':
    print('ごちそうさま')

  elif keyword == '疲れた':
    print('がんばって')

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
 
  if keyword == 'おやすみ':
    print('また明日ね')
 
def init_servo():
  pass

def init_julius():
  p = subprocess.Popen(["sh julius.sh"], stdout=subprocess.PIPE, shell=True)
  pid = str(p.stdout.read().decode('utf-8'))
  print("Julius PID: " + pid)
  time.sleep(3)
  return p, pid

if __name__ == "__main__":
  # init mp3
  #pygame.mixer.init()

  # init servo
  # GPIO.setmode(xxx)
  # gp_out -- xxx.start() made
  # bat, mid, top

  # init julius
  p, pid = init_julius()  

  # Communicate with julios module
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.connect((host, port))

  res = ''

  print("Start voice recognition")
  try:
    while True:
      # Waiting for the end of sentence(='\n.')
      while(res.find('\n.') == -1):
        # Store the data from julius
        #res += sock.recv(1024)
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

  except KeyboardInterrupt:
    print("\n")
    print("End voice recognition")

    p.kill()
    subprocess.call(["kill " + pid], shell=True)
    sock.close()


