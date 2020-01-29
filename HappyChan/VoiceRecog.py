
# -*- coding:utf-8 -*-
import socket
import time
import pygame.mixer 


host = 'localhost'
port = 10500


# Response
def response(keyword):
  #print(keyword)
　if keyword == '勉強する':
    print('勉強する')
    pygame.mixer.music.load('furefure.mp3')
    pygame.mixer.music.play(1) 

　if keyword == 'いただきます':
    print('めしあがれ')
  #  pygame.mixer.music.load('info-girl1-ganbattane1.mp3')
  #  pygame.mixer.music.play(1) 

  if keyword == 'ごちそうさま':
    print('ごちそうさま')
    pygame.mixer.music.load('gochisousama.mp3')
    pygame.mixer.music.play(1) 

　if keyword == '疲れた':
    print('がんばって')
    pygame.mixer.music.load('info-girl1-ganbattane1.mp3')
    pygame.mixer.music.play(1) 

　if keyword == '眠い'
    print('起きろ')
  #  pygame.mixer.music.load('info-girl1-ganbattane1.mp3')
  #  pygame.mixer.music.play(1) 

　if keyword == 'お腹空いた':
     print('何が食べたい？')
  #  pygame.mixer.music.load('info-girl1-ganbattane1.mp3')
  #  pygame.mixer.music.play(1) 
 

　if keyword == 'この問題難しい':
    print('がんばって')
    pygame.mixer.music.load('info-girl1-ganbattane1.mp3')
    pygame.mixer.music.play(1) 

　if keyword == '今から勉強するね':
    print('がんばって')
    pygame.mixer.music.load('furefure.mp3')
    pygame.mixer.music.play(1) 

　if keyword == '勉強終わったよ':
    print('おつかれさま')
    pygame.mixer.music.load('yatta.mp3')
    pygame.mixer.music.play(1)

　if keyword == 'おはよう':
    print('おはよう')
    pygame.mixer.music.load('ohayou.mp3')
    pygame.mixer.music.play(1) 
 
　if keyword == 'おやすみ':
    print('また明日ね')
    pygame.mixer.music.load('mataashita.mp3')
    pygame.mixer.music.play(1) 



    time.sleep(10)
    pygame.mixer.music.stop()


# init mp3
pygame.mixer.init()


# Communicate with julios module
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

res = ''

while True:
  # Waiting for the end of sentence(='\n.')
  while(res.find('\n.') == -1):
    # Store the data from julius
    res += sock.recv(1024)

  word = ''
  for line in res.split('\n'):
    index = line.find('WORD=')
    #print('OK')

    # If there is a word we want to get
    if index != -1:
      line = line[index + 6:line.find('"', index + 6)]
      if line != '[s]':
        word = word + line

    #print(word)

    # Response for keyword
    response(word)

    res = ''


