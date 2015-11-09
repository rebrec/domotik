
from subprocess import call
import os
from InterrupteurBase import InterrupteurBase
import time
import sys


class MinuterieFilaire(InterrupteurBase):
    def __init__(self, name, relay_to_gpio, press_action='on', timer_delay=1,
                 timer_autostart=False, *args, **kwargs):
        self.relay_to_gpio = relay_to_gpio
        super(MinuterieFilaire, self).__init__(name, on_off=False,
                                        press_action=press_action,
                                        func_cmd_on=self.on,
                                        func_cmd_off=self.off,
                                        timer_delay=timer_delay,
                                        timer_autostart=timer_autostart,
                                        *args, **kwargs)

    def on(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '1')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.abspath(__file__)), params)
        print "Going to send command : {0}".format(params)
        sys.stdout.flush()
        call([cmd], shell=True)

    def off(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '0')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.abspath(__file__)), params)
        print "Going to send command : {0}".format(params)
        sys.stdout.flush()
        call([cmd], shell=True)




if __name__ == '__main__':
    print "Creation d'une minuterie de 5 secondes..."
    m = MinuterieFilaire(name='Ma MinuterieSansFils', chan='B', sw=2, timer_delay=5, timer_autostart=True, press_action='off' )
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
