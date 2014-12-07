#!/usr/bin/python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class GetInterHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        name = self.get_argument("name", None, True)
        res = self.controller.get_inter(name)
        self.write(res)



class SetInterHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        name = self.get_argument("name", None, True)
        cmd = self.get_argument("cmd", None, True)
        res = self.controller.set_inter(name, cmd)
        self.write(res)




class MainHandler(tornado.web.RequestHandler):
    def get(self):
        print "REQUETE MAIN"
        self.render("index.html")
