

import sys
import time

import Adafruit_MPR121.MPR121 as MPR121



cap = MPR121.MPR121()


if not cap.begin():
    print('Error initializing MPR121.  Check your wiring!')
    sys.exit(1)


print('Press Ctrl-C to quit.')
last_touched = cap.touched()
while True:
    current_touched = cap.touched()

    for i in range(12):

        pin_bit = 1 << i

        if current_touched & pin_bit and not last_touched & pin_bit:
            print('curr: {:012b}'.format(current_touched))
            print('last: {:012b}'.format(last_touched))

            print('{0} touched!\n'.format(i))


        if not current_touched & pin_bit and last_touched & pin_bit:
            print('curr: {:012b}'.format(current_touched))
            print('last: {:012b}'.format(last_touched))

            print('{0} released!\n'.format(i))


    last_touched = current_touched
    time.sleep(0.1)


