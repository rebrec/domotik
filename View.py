#!/usr/bin/python
# -*- coding:utf-8 -*-


import tornado.ioloop
import tornado.web
from WebHandlers import *
import os
import sys

class WebView(object):
    def __init__(self, port=8888, controller = None):
        self.controller = controller
        self.port = port

    def add_controller(self, controller):
        self.controller = controller
        self.init_webapp()

    def init_webapp(self):
        settings = {
            'debug': True,
            'static_path': os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'),
        }
        handlers = [
                        (r"/index.html", DefaultHandler, dict(controller=self.controller)),
                        (r"/config/get/.*", GetConfigHandler, dict(controller=self.controller)),
                        (r"/config/set/.*", SetConfigHandler, dict(controller=self.controller)),
                        (r"/config/reload/.*", ReloadInterHandler, dict(controller=self.controller)),
                        (r"/inter/get/.*", GetInterHandler, dict(controller=self.controller)),
                        (r"/inter/set/.*", SetInterHandler, dict(controller=self.controller)),
                        (r'/static/(.*)', tornado.web.StaticFileHandler, dict(path=settings['static_path'])),
                        (r"/.*", DefaultHandler, dict(controller=self.controller)),
                                             ]
        self.application = tornado.web.Application(handlers, **settings)
        self.application.listen(self.port)

    def start(self):
        print "Starting View"
        sys.stdout.flush()
        tornado.ioloop.IOLoop.instance().start()



if __name__ == '__main__':
    class Controller(object):
        def __init__(self):
            print "init"

        def get_inter(self, address, number):
            """
            :param address:
            :param number:
            :return:
            """
            return "Get : {} / {}".format(address, number)

        def set_inter(self, address, number, cmd):
            """
            :param address:
            :param number:
            :param cmd:
            :return:
            """
            return "Set {} : {} / {}".format(cmd, address, number)

    c = Controller()
    v = WebView(8080)
    v.add_controller(c)
    v.start()

