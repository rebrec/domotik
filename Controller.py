#!/usr/bin/python
# -*- coding:utf-8 -*-
from Communicator import SerialCommunicator
from Interrupteur import Interrupteur
from View import WebView


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

    def set_inter(self, name, cmd):
        if   cmd.lower() == 'on':       self.get_switch(name).set_on()
        elif cmd.lower() == 'off':      self.get_switch(name).set_off()
        elif cmd.lower() == 'toggle':   self.get_switch(name).toggle()
        return { 'result': 'done'}

    def get_inter(self, name):
        return {'state': self.get_switch(name).state}


if __name__ == '__main__':
    def devant_maison_on(array_args):
        adr = array_args['adr']
        sw = array_args['sw']
        ser = array_args['s']
        s.send_while('ON\r', 'Commande : ON\r\n')


    def devant_maison_off(array_args):
        ser = array_args['s']
        s.send_while('OFF\r', 'Commande : OFF\r\n')



    s = SerialCommunicator('/dev/ttyUSB0', 9600, 3, 1, True)
    i = Interrupteur('LampeDevant', devant_maison_on, devant_maison_off, {'s': s, 'adr': 1, 'sw': 10})
    v = WebView()
    c = Controller(s, v)
    c.add_inter(i)
    c.start()