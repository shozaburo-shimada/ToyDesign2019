#!/usr/bin/python
# coding:utf-8
import time
import RPi.GPIO as GPIO
import os

pinnumber=23
GPIO.setmode(GPIO.BCM)

#GPIO23pin
GPIO.setup(pinnumber,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

while True:
    GPIO.wait_for_edge(pinnumber,GPIO.RISING)
    sw_counter = 0

    while True:
        sw_status = GPIO.input(pinnumber)
        if sw_status == 1:
            sw_counter = sw_counter + 1
            if sw_counter >= 50:
                print("nagaoshi")
                os.system("sudo shutdown -h now")
                break
        else:
           print("mijikai")
           break

        time.sleep(0.01)

    print(sw_counter)

