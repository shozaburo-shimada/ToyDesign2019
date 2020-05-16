cd ~

git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
git clone https://github.com/adafruit/Adafruit_Python_PureIO.git

cd Adafruit_Python_PCA9685
sudo python setup.py install
sudo python3 setup.py install

cd ~
cd Adafruit_Python_GPIO
sudo python setup.py install
sudo python3 setup.py install

cd ~
cd Adafruit_Python_PureIO
sudo python setup.py install
sudo python3 setup.py install
