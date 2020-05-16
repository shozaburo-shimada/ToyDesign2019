import Adafruit_PCA9685
import time

class servo_Class:

  def __init__(self, Channel, ZeroOffset):
    self.Channel = Channel
    self.ZeroOffset = ZeroOffset

    self.pwm = Adafruit_PCA9685.PCA9685(address=0x40)
    self.pwm.set_pwm_freq(60)

  def SetPos(self, pos):
    pulse = int((650 - 150) / 180 * pos) + 150 + self.ZeroOffset
    self.pwm.set_pwm(self.Channel, 0, pulse)

if __name__ == '__main__':
  servo0 = servo_Class(Channel=0, ZeroOffset=-5)
  servo1 = servo_Class(Channel=1, ZeroOffset=-5)
  servo2 = servo_Class(Channel=2, ZeroOffset=-5)
  servo3 = servo_Class(Channel=3, ZeroOffset=-5)

  try:
    while True:
      print("45")
      servo0.SetPos(45)
      time.sleep(2)
      servo1.SetPos(45)
      time.sleep(2)
      servo2.SetPos(45)
      time.sleep(2)      
      servo3.SetPos(45)
      time.sleep(2)
      
      print("90")
      servo0.SetPos(90)
      time.sleep(2)
      servo1.SetPos(90)
      time.sleep(2)
      servo2.SetPos(90)
      time.sleep(2)
      servo3.SetPos(90)
      time.sleep(2)



  except KeyboardInterrupt:
    print("End PCM9685 test")

