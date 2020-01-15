# Confirm priority of mic
# Require "0 snd_usb_audio"
cat /proc/asound/modules

# Execute
# julius -C ~/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/Documents/ToyDesign2019/HappyChan/julius/dict/hello -input mic

# Execute as module mode
#julius -C ~/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/Documents/ToyDesign2019/HappyChan/julius/dict/hello -input mic -module
julius -C ~/Documents/ToyDesign2019/HappyChan/julius/julius-kit/dictation-kit-v4.4/am-gmm.jconf -nostrip -gram ~/Documents/ToyDesign2019/HappyChan/julius/dict/happy -input mic -module &

python VoiceRecog.py

