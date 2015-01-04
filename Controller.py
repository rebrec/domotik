#!/usr/bin/python
# -*- coding:utf-8 -*-

from InterrupteurOnOff import InterrupteurOnOff
from Minuterie import Minuterie
from View import WebView
from subprocess import call
import os

import re


class Controller:
    def __init__(self, communicator, view):
        self.switches = []
        self.communicator = communicator
        self.view = view
        self.view.add_controller(self)
        print "Controller Init"

    def start(self):
        self.view.start()

    def add_inter(self, switch):
        self.switches += [switch]

    def get_switch(self, name):
        l = [switch.name for switch in self.switches]
        return self.switches.__getitem__(l.index(name))

    def get_switch_list_view(self):
        return  [(switch.name, switch.caption, switch.on_off) for switch in self.switches]




    def set_inter(self, name, cmd):
        if   cmd.lower() == 'on':       self.get_switch(name).set_on()
        elif cmd.lower() == 'off':      self.get_switch(name).set_off()
        elif cmd.lower() == 'toggle':   self.get_switch(name).toggle()
        elif cmd.lower() == 'press':   self.get_switch(name).press()
        return { 'result': 'done' }

    def get_inter(self, name, all):
        if all:
            res = {}
            for switch in self.switches:
                res[switch.name] = switch.state
            return res
        else:
            return {'state': self.get_switch(name).state}


if __name__ == '__main__':
    def devant_maison_on(array_args):
        chan = array_args['chan']
        sw = array_args['sw']
        params = 'I {0} {1} {2}'.format(chan, sw, '1')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath(__file__)), params)
        print "Going to launch {0} with parameters : {1}".format(cmd, params)
        call([cmd], shell=True)
        #s.send_while('I {0} {1} {2}\r'.format(chan, sw, '1'), '.')
    def devant_maison_off(array_args):
        chan = array_args['chan']
        sw = array_args['sw']
        params = 'I {0} {1} {2}'.format(chan, sw, '0')
        cmd = "{0}/send {1}".format(os.path.dirname(os.path.realpath(__file__)), params)
        print "Going to launch {0} with parameters : {1}".format(cmd, params)
        call([cmd], shell=True)

        #s.send_while('I {0} {1} {2}\r'.format(chan, sw, '0'), '.')

    #s = SerialCommunicator('/dev/ttyUSB0', 9600, 3, 1, True)
    v = WebView(8080)
    c = Controller(None, v)
    c.add_inter(InterrupteurOnOff(name='Lampe Extérieur', chan='C', sw=3))
    c.add_inter(Minuterie(name='Minuterie Lampe Extérieur', chan='C', sw=3, press_action='on', timer_delay=5, timer_autostart=True))
    c.add_inter(InterrupteurOnOff(name='Sapin de Noel', chan='C', sw=2))
    print c.get_switch_list_view()
    c.start()
