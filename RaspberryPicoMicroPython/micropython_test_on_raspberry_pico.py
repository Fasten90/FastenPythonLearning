import machine
led_onboard = machine.Pin(25, machine.Pin.OUT)
led_onboard.value(1)

import utime

while True:
    led_onboard.value(1)
    utime.sleep(0.5)
    led_onboard.value(0)
    utime.sleep(0.5)

