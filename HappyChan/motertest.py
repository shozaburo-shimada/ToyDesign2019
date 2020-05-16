# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#gp_out = 14 
#GPIO.setup(gp_out,GPIO.OUT)
#mimi = GPIO.PWM(gp_out,50)
#mimi.start(0.0)

#gp_out = 3
#GPIO.setup(gp_out,GPIO.OUT)
#shippo = GPIO.PWM(gp_out,50)
#shippo.start(0.0)

#gp_out = 4 
#GPIO.setup(gp_out,GPIO.OUT)
#kubihuri = GPIO.PWM(gp_out,50)
#kubihuri.start(0.0)

gp_out = 18 
GPIO.setup(gp_out,GPIO.OUT)
unazuki = GPIO.PWM(gp_out,50)
unazuki.start(0.0)


bot = 2.5 #0度
mid = 7.2 #90度
top = 12.0 #180度

print ("bot")
#mimi.ChangeDutyCycle(bot)
#shippo.ChangeDutyCycle(bot)
#kubihuri.ChangeDutyCycle(bot)
unazuki.ChangeDutyCycle(bot)
time.sleep(2)

print ("mid")
#mimi.ChangeDutyCycle(mid)
#shippo.ChangeDutyCycle(mid)
#kubihuri.ChangeDutyCycle(mid)
unazuki.ChangeDutyCycle(mid)
time.sleep(2)

print ("top")
#mimi.ChangeDutyCycle(top)
#shippo.ChangeDutyCycle(top)
#kubihuri.ChangeDutyCycle(top)
unazuki.ChangeDutyCycle(top)
time.sleep(2)


GPIO.cleanup()
