
from subprocess import call
import os
from Interrupteur import Interrupteur
import time


class Minuterie(Interrupteur):
    def __init__(self, name, chan='A', switch=1, timer_delay=1, args=[], timer_autostart=False):
        super(Minuterie, self).__init__(name, { 'press': 'on'}, self.set_on, self.set_off, args,
                                        dict(chan=chan, sw=switch), timer_delay, timer_autostart)

    def set_on(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '1')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath('__file__')), params)
        print "Going to send command : {0}".format(params)
        call([cmd], shell=True)

    def set_off(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '0')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath('__file__')), params)
        print "Going to send command : {0}".format(params)
        call([cmd], shell=True)




if __name__ == '__main__':
    print "Creation d'une minuterie de 5 secondes..."
    m = Minuterie(name='Ma Minuterie', chan='B', switch=2, timer_delay=5, timer_autostart=True )
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