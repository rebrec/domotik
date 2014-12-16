#!/usr/bin/python
# -*- coding:utf-8 -*-
from Communicator import SerialCommunicator
from Interrupteur import Interrupteur
from View import WebView
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
        return  [(switch.name, switch.caption) for switch in self.switches]




    def set_inter(self, name, cmd):
        if   cmd.lower() == 'on':       self.get_switch(name).set_on()
        elif cmd.lower() == 'off':      self.get_switch(name).set_off()
        elif cmd.lower() == 'toggle':   self.get_switch(name).toggle()
        return { 'result': 'done'}

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
        s = array_args['s']
        s.send_while('I {0} {1} {2}\r'.format(chan, sw, '1'), '.')
    def devant_maison_off(array_args):
        chan = array_args['chan']
        sw = array_args['sw']
        s = array_args['s']
        s.send_while('I {0} {1} {2}\r'.format(chan, sw, '0'), '.')
    s = SerialCommunicator('/dev/ttyUSB0', 9600, 3, 1, True)

    v = WebView(8080)
    c = Controller(s, v)
    c.add_inter(Interrupteur('Lampe Extérieur', devant_maison_on, devant_maison_off, {'s': s, 'chan': 'C', 'sw': 3}))
    c.add_inter(Interrupteur('Sapin de Noel', devant_maison_on, devant_maison_off, {'s': s, 'chan': 'C', 'sw': 2}))
    print c.get_switch_list_view()
    c.start()
