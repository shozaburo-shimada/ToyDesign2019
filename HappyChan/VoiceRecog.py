# -*- coding:utf-8 -*-
import socket
import time 


host = 'localhost'
port = 10500


# Response
def response(keyword):
  if keyword == 'おはよう':
    print('おはようございます')

  if keyword == 'こんにちわ':
    print('こんにちわ、いい天気ですね')

  if keyword == 'ありがとう':
    print('どういたしまして')

  if keyword == 'さようなら':
    print('バイバイ〜')



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


