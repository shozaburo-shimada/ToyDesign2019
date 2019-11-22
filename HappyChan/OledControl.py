import time
 
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
 
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
 
import subprocess
 
# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
 
# Note you can change the I2C address by passing an i2c_address parameter like:
disp1 = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3C)
disp2 = Adafruit_SSD1306.SSD1306_128_64(rst=RST, i2c_address=0x3D)

# Initialize library.
disp1.begin()
disp2.begin()

 
# Clear display.
disp1.clear()
disp2.clear()
disp1.display()
disp2.display()

 
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width1 = disp1.width
height1 = disp1.height
image1 = Image.new('1', (width1, height1))

width2 = disp2.width
height2 = disp2.height
image2 = Image.new('1', (width2, height2))

 
# Get drawing object to draw on image.
draw1 = ImageDraw.Draw(image1)
draw2 = ImageDraw.Draw(image2)

 
# Draw a black filled box to clear the image.
draw1.rectangle((0,0,width1,height2), outline=0, fill=0)
draw2.rectangle((0,0,width2,height2),outline=0, fill=0)
 
while True:
 
    # Draw a black filled box to clear the image.
    draw1.rectangle((0,0,width1,height1), outline=0, fill=0)
    draw2.rectangle((0,0,width2,height2), outline=0, fill=0) 

    # Draw Object
    cx = 64 # center of circle, x
    cy = 32 # center of circle, y
    cr = 35 # radius of circle
    eh = 70 # height of ellipse
    ew = 40 # width of ellipse

    draw1.ellipse((cx - ew / 2, cy - eh / 2, cx + ew / 2, cy + eh / 2), outline=1, fill=1)
    draw2.ellipse((cx - cr, cy - cr, cx + cr, cy + cr), outline=1, fill=1)

    # Display image.
    disp1.image(image1)
    disp2.image(image2)
    disp1.display()
    disp2.display()
    time.sleep(.1)
