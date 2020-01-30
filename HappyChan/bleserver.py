
from RN42 import RN42
import time

# Confirm Bluetooth MAC Address with "$ hciconfig" command
ras = RN42("ras", "B8:27:EB:20:C2:96 ", 1)
ras.connectBluetooth(ras.bdAddr, ras.port)

while True:
  try:
    ras.sock.send("Hello World")
    print "send data"

