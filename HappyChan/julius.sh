# Confirm priority of mic
# Require "0 snd_usb_audio"
# cat /proc/asound/modules

# Execute
#julius -C ~/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/Documents/ToyDesign2019/HappyChan/julius/dict/happy -input mic

# Execute as module mode
#julius -C ~/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/Documents/ToyDesign2019/HappyChan/julius/dict/hello -input mic -module
julius -C /home/pi/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram /home/pi/Documents/ToyDesign2019/HappyChan/julius/dict/happy -input mic -module > log.txt &

# Get process ID
echo $!
sleep 2

#python VoiceRecog.py

