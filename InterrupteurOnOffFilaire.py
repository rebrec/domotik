# -*- coding:utf-8 -*-
from subprocess import call
import os
from InterrupteurBase import InterrupteurBase
import sys
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
        GPIO.setmode(GPIO.BCM)
        print "Setting GPIO{0} as output for relay {1}".format(self.relay_to_gpio[self.sw], self.sw)
        GPIO.setup(self.relay_to_gpio[self.sw], GPIO.OUT) # configure as output the relay channel

    def on(self, sw=100, *args, **kwargs):
        gpio = self.relay_to_gpio[self.sw]
        print 'Relay {0} : GPIO{1} = {2}'.format(sw, gpio, '1')
        GPIO.output(gpio, GPIO.HIGH)

    def off(self, chan="Z", sw=100, *args, **kwargs):
        gpio = self.relay_to_gpio[self.sw]
        print 'Relay {0} : GPIO{1} = {2}'.format(sw, gpio, '1')
        GPIO.output(gpio, GPIO.LOW)




if __name__ == '__main__':
    relay_to_gpio = {1: 10, 2: 24, 3: 23, 4: 22, 5: 27, 6: 18, 7: 15, 8: 14}

    i = InterrupteurOnOffFilaire(name='Mon OnOff', sw=1, relay_to_gpio=relay_to_gpio)
    print "essaie d'allumage"
    i.set_on()
    print "etat de i : {}".format(i.state)
    i.set_on()
    print "etat de i : {}".format(i.state)
    i.set_off()
    print "etat de i : {}".format(i.state)
    i.set_off()
    print "etat de i : {}".format(i.state)
    i.toggle()
    print "etat de i : {}".format(i.state)
