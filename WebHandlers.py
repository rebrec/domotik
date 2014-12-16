#!/usr/bin/python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web


class GetInterHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        name = self.get_argument("name", None, True)
        all = self.get_argument("all", False, True)
        res = self.controller.get_inter(name, all)
        self.write(res)



class SetInterHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        name = self.get_argument("name", None, True)
        cmd = self.get_argument("cmd", None, True)
        res = self.controller.set_inter(name, cmd)
        self.write(res)




class DefaultHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        print "REQUETE MAIN"
        get_switch_list_view = self.controller.get_switch_list_view()
        self.render("index.html", get_switch_list_view=get_switch_list_view )
