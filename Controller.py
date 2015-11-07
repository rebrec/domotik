#!/home/pi/projets/domotik/venv/bin/python
# -*- coding:utf-8 -*-

import json
from InterrupteurOnOff import InterrupteurOnOff
from MinuterieSansFils import MinuterieSansFils
from View import WebView
import sys
import os

import re


class Controller:
    def __init__(self, communicator, view):
        self.switches = []
        self.communicator = communicator
        self.view = view
        self.view.add_controller(self)
        print "Controller Init"
        sys.stdout.flush()

    def start(self):
        self.view.start()

    def add_inter(self, switch):
        self.switches += [switch]

    def get_switch(self, name):
        l = [switch.name for switch in self.switches]
        return self.switches.__getitem__(l.index(name))

    def get_switch_list_view(self):
        return  [(switch.name, switch.caption, switch.on_off) for switch in self.switches]

    def reload_config(self):
        try:
            os.execl(sys.executable, *([sys.executable]+sys.argv))
            print "reload"
            return { 'result': 'done' } # on n'ira jamais jusque la...
        except Exception:
            return { 'result': 'error' }

    def get_config(self, name):
        if name == 'current': # seul cas pris en charge actuellement
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
            with open(config_file) as json_data_file:
                configuration = json.load(json_data_file)
            return configuration
        else:
            return None

    def set_config(self, name, config_val):
        if name == 'current': # seul cas pris en charge actuellement
            config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
            try:
                configuration = json.loads(config_val)
                dump=json.dumps(configuration, indent=4)
                f = open(config_file, 'w')
                f.write(dump)
                f.close()
                return { 'result': 'done' }
            except Exception:
                return { 'result': 'error' }
        else:
            return { 'result': 'error' }



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
    # Chargement de la configuration
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.json')
    with open(config_file) as json_data_file:
        configuration = json.load(json_data_file)

    v = WebView(configuration['listen'])
    c = Controller(None, v)

    for inter in configuration['interrupteurs']:
        if inter['type'] == 'on/off':
            c.add_inter(InterrupteurOnOff(**inter['param']))
        elif inter['type'] == 'minuterie':
            c.add_inter(MinuterieSansFils(**inter['param']))
        else:
            print "Type d'interrupteur inconnu : %s" % inter['type']
            sys.stdout.flush()
    print c.get_switch_list_view()
    sys.stdout.flush()
    c.start()
