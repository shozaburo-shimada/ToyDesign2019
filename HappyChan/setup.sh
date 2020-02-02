sudo apt-get update

# BLE
sudo apt-get install -y bluetooth 
sudo apt-get install -y libusb-dev 
sudo apt-get install -y libdbus-1-dev 
sudo apt-get install -y libudev-dev 
sudo apt-get install -y libical-dev
sudo apt-get install -y libreadline-dev
sudo apt-get install -y libdbus-glib-1-dev
sudo apt-get install -y libbluetooth-dev

cd ~
wget http://www.kernel.org/pub/linux/bluetooth/bluez-5.45.tar.xz
xz -dv bluez-5.45.tar.xz
tar -xf bluez-5.45.tar
cd bluez-5.45
./configure --enable-experimental
make -j4
sudo make install
sudo pip install pybluez
