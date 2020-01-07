import serial
import time
import sys

print('start')

ser = serial.Serial('/dev/ttyS0', 9600)

ser.write("hello")

try:
  while True:
    c = ser.read()
    print(c)

except KeyboardInterrupt:
  ser.close()
  print('end')
  sys.exit(0)
