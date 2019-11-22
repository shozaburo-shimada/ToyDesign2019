# For Face Detection
import numpy as np
import cv2

# For Display Control
import time
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess

# Initialize Face Detection
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

# Initialize Display Control
## Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
 
## Note you can change the I2C address by passing an i2c_address parameter like:
disp1 = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
disp2 = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

## Initialize library.
disp1.begin()
disp2.begin()

## Clear display.
disp1.clear()
disp2.clear()
disp1.display()
disp2.display()

## Create blank image for drawing.
## Make sure to create image with mode '1' for 1-bit color.
width1 = disp1.width
height1 = disp1.height
image1 = Image.new('1', (width1, height1))

width2 = disp2.width
height2 = disp2.height
image2 = Image.new('1', (width2, height2))

## Get drawing object to draw on image.
draw1 = ImageDraw.Draw(image1)
draw2 = ImageDraw.Draw(image2)

## Draw a black filled box to clear the image.
draw1.rectangle((0,0,width1,height2), outline=0, fill=0)
draw2.rectangle((0,0,width2,height2),outline=0, fill=0)

# "while True:" is same as "loop()" of Arduino
while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,     
        scaleFactor=1.2,
        minNeighbors=5,     
        minSize=(20, 20)
    )
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]  
    cv2.imshow('video',img)

    ratio_x = ((x + w) / 2) / 640
    ratio_y = ((y + h) / 2) / 480

    cx = 128 * ratio_x
    cy = 64 * ratio_y
    cr = 35
    draw1.ellipse((cx - cr, cy - cr, cx + cr, cy + cr), outline=1, fill=1)
    draw2.ellipse((cx - cr, cy - cr, cx + cr, cy + cr), outline=1, fill=1)

    ##Quit
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

# Finalize Face Detection
cap.release()
cv2.destroyAllWindows()