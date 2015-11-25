
from subprocess import call
import os
from InterrupteurBase import InterrupteurBase
import time
import sys
if os.uname()[4][:3] == 'arm':
    import RPi.GPIO as GPIO


class MinuterieFilaire(InterrupteurBase):
    def __init__(self, name, relay_to_gpio, press_action='on', timer_delay=1,
                 timer_autostart=False, *args, **kwargs):
        super(MinuterieFilaire, self).__init__(name, on_off=False,
                                        press_action=press_action,
                                        func_cmd_on=self.on,
                                        func_cmd_off=self.off,
                                        timer_delay=timer_delay,
                                        timer_autostart=timer_autostart,
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
    print "Creation d'une minuterie de 5 secondes..."
    m = MinuterieFilaire(name='Ma MinuterieSansFils', sw=1, timer_delay=5, timer_autostart=True, press_action='off' )
    print ".... attente 8 secondes..."
    time.sleep(8)
    print "Relance du Timer"
    m.press()
    print ".... attente 3 secondes"
    time.sleep(3)
    print "Relance du Timer"
    m.press()
    print ".... attente 3 secondes"
    time.sleep(3)
    print "Relance du Timer"
    m.press()
    print ".... attente 3 secondes"
    time.sleep(3)
    print "Relance du Timer"
    m.press()
    print "attente de 10 SECONDES Finales"
    time.sleep(10)
