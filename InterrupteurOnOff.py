# -*- coding:utf-8 -*-
from subprocess import call
import os
from InterrupteurBase import InterrupteurBase
import time


class InterrupteurOnOff(InterrupteurBase):
    def __init__(self, name, *args, **kwargs):
        super(InterrupteurOnOff, self).__init__(name,
                                                on_off=True,
                                                func_cmd_on=self.on,
                                                func_cmd_off=self.off,
                                                *args, **kwargs)

    def on(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '1')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath('__file__')), params)
        print "Going to send command : {0}".format(params)
        call([cmd], shell=True)

    def off(self, chan="Z", sw=100, *args, **kwargs):
        params = 'I {0} {1} {2}'.format(chan, sw, '0')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath('__file__')), params)
        print "Going to send command : {0}".format(params)
        call([cmd], shell=True)




if __name__ == '__main__':
    i = InterrupteurOnOff(name='Mon OnOff', chan='B', sw=2)
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