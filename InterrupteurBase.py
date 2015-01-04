#!/usr/bin/python
# -*- coding:utf-8 -*-
import re
from ResetableTimer import ResetableTimer


class InterrupteurBase(object):
    def __init__(self, name,
                 chan='Z', sw = 100,
                 on_off=True,
                 press_action='on',
                 func_cmd_on=None,
                 func_cmd_off=None,
                 timer_delay=0,
                 timer_autostart=False,
                 *args, **kwargs):
        self.name = "sw-{0}".format(re.sub(r'\W+', '', name.lower()))
        self.caption = name
        self.chan = chan
        self.sw = sw
        self.on_off = on_off
        #self.type = type
        self.func_cmd_on = func_cmd_on
        self.func_cmd_off = func_cmd_off
        self.args = args
        self.kwargs = kwargs
        self.state = False
        if not on_off:
            if press_action == 'on':
                self._press_func = self.set_on
                self.resetable_timer = ResetableTimer(timer_delay, self.set_off, auto_start=timer_autostart, *self.args, **self.kwargs)
            elif press_action == 'off':
                self._press_func = self.set_off
                self.resetable_timer = ResetableTimer(timer_delay, self.set_on, auto_start=timer_autostart, *self.args, **self.kwargs)
            else:
                raise Exception("Wrong 'press' parameter, must be 'on' or 'off' !")
        else:
            self.resetable_timer = None

    def toggle(self):
        if self.state:
            self.set_off()
        else:
            self.set_on()

    def press(self):
        self._press_func(*self.args, **self.kwargs)
        self.resetable_timer.reset()

    def set_on(self):
        self.state = True
        self.func_cmd_on(chan=self.chan, sw=self.sw, *self.args, **self.kwargs)
    def set_off(self):
        self.state = False
        self.func_cmd_off(chan=self.chan, sw=self.sw, *self.args, **self.kwargs)



if __name__ == '__main__':
    def func_on(adr="", sw="", *args, **kwargs):
        print "ON pour le Switch {} à l'adresse {}".format(sw, adr)
    def func_off(adr="", sw="", *args, **kwargs):
        print "OFF pour le Switch {} à l'adresse {}".format(sw, adr)
    i = InterrupteurBase('test', {'on_off': True }, func_on, func_off, [], dict(adr='A', sw=1))
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


