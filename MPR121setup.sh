# Install Dependencies
sudo apt-get update
sudo apt-get install -y build-essential python-dev python-smbus python-pip git

# Download MPR121 Library
cd ~
git clone https://github.com/adafruit/Adafruit_Python_MPR121.git

# Install MPR121 LIbrary
cd Adafruit_Python_MPR121
sudo python setup.py install
