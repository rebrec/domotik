# -*- coding:utf-8 -*-
from subprocess import call
import os
from InterrupteurBase import InterrupteurBase
import sys
if os.uname()[4][:3] == 'arm':
    import RPi.GPIO as GPIO


class InterrupteurOnOffFilaire(InterrupteurBase):
    def __init__(self, name, relay_to_gpio, *args, **kwargs):
        super(InterrupteurOnOffFilaire, self).__init__(name,
                                                on_off=True,
                                                func_cmd_on=self.on,
                                                func_cmd_off=self.off,
                                                *args, **kwargs)
        # for now, we use the SW number (of wireless power plugs) as the relay number to command for wired switchs (var "SW")
        self.relay_to_gpio = relay_to_gpio
        if os.uname()[4][:3] == 'arm':
            GPIO.setmode(GPIO.BCM)
        print "Setting GPIO{0} as output for relay {1}".format(self.relay_to_gpio[self.sw], self.sw)
        if os.uname()[4][:3] == 'arm':
            GPIO.setup(self.relay_to_gpio[self.sw], GPIO.OUT) # configure as output the relay channel
            GPIO.output(self.relay_to_gpio[self.sw],GPIO.LOW)

    def on(self, sw=100, *args, **kwargs):
        gpio = self.relay_to_gpio[self.sw]
        print 'Relay {0} : GPIO{1} = {2}'.format(sw, gpio, '1')
        if os.uname()[4][:3] == 'arm':
            GPIO.output(gpio, GPIO.LOW) # inverted logic 0V = Relay On

    def off(self, chan="Z", sw=100, *args, **kwargs):
        gpio = self.relay_to_gpio[self.sw]
        print 'Relay {0} : GPIO{1} = {2}'.format(sw, gpio, '0')
        if os.uname()[4][:3] == 'arm':
            GPIO.output(gpio, GPIO.HIGH) # inverted logic 3.3V = Relay Off




if __name__ == '__main__':
    import time
    relay_to_gpio = {1: 10, 2: 24, 3: 23, 4: 22, 5: 27, 6: 18, 7: 15, 8: 14}

    i = InterrupteurOnOffFilaire(name='Mon OnOff', sw=1, relay_to_gpio=relay_to_gpio)
    i.set_off()
    print "etat de i : {}".format(i.state)
    time.sleep(1)
    print "essaie d'allumage"
    i.set_on()
    print "etat de i : {}".format(i.state)
    time.sleep(3)
    i.set_on()
    print "etat de i : {}".format(i.state)
    time.sleep(3)
    # inverted logic 0V = Relay Onprint "etat de i : {}".format(i.state)
    time.sleep(3)
    i.set_off()
    print "etat de i : {}".format(i.state)
    time.sleep(3)
    i.toggle()
    print "etat de i : {}".format(i.state)
    time.sleep(3)
