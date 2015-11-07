#!/usr/bin/python
# -*- coding:utf-8 -*-

import tornado.ioloop
import tornado.web
import sys

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

class ReloadInterHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def post(self):
        # name = self.get_argument("name", "current", True)
        # config_val = self.get_argument("config_val", None, True)
        # print "name %s" % name
        # print "val %s" % config_val
        print "reload-"
        res = self.controller.reload_config()
        self.write(res)

class GetConfigHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        name = self.get_argument("name", "current", True)
        config = self.controller.get_config(name)
        self.render("config.html", json_config=config, name=name )


class SetConfigHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def post(self):
        name = self.get_argument("name", "current", True)
        config_val = self.get_argument("config_val", None, True)
        print "name %s" % name
        print "val %s" % config_val
        res = self.controller.set_config(name, config_val)
        self.write(res)




class DefaultHandler(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self):
        print "REQUETE MAIN"
        sys.stdout.flush()
        get_switch_list_view = self.controller.get_switch_list_view()
        self.render("index.html", get_switch_list_view=get_switch_list_view )
