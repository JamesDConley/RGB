import time
import pygatt
from govee_btled import BluetoothLED

MAC = 'a4c138053ec2'

led = BluetoothLED(MAC, bt_backend_cls=pygatt.BGAPIBackend)
led.set_state(True)
led.set_color('blue')
time.sleep(1)
led.set_color('#facd03')
time.sleep(1)
# The bulb seems to have a white-mode which uses cold/warm white LEDs instead of the RGB LEDs.
# Supply a value between -1 (warm) and 1 (cold)
led.set_color_white(-0.4)
