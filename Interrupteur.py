#!/usr/bin/python
# -*- coding:utf-8 -*-

class Interrupteur(object):
    def __init__(self, name, func_cmd_on, func_cmd_off, array_args={}):
        self.name = name
        self.func_cmd_on = func_cmd_on
        self.func_cmd_off = func_cmd_off
        self.array_args = array_args
        self.state = False

    def toggle(self):
        if self.state:
            self.set_off()
        else:
            self.set_on()

    def set_on(self):
        self.state = True
        self.func_cmd_on(self.array_args)


    def set_off(self):
        self.state = False
        self.func_cmd_off(self.array_args)


if __name__ == '__main__':
    def func_on(array_args):
        adr = array_args['adr']
        sw = array_args['sw']
        print "ON pour le Switch {} à l'adresse {}".format(sw, adr)

    def func_off(array_args):
        adr = array_args['adr']
        sw = array_args['sw']
        print "OFF pour le Switch {} à l'adresse {}".format(sw, adr)



    i = Interrupteur('test',func_on, func_off, {'adr': 1, 'sw': 10})
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


