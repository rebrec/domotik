#!/usr/bin/python
# -*- coding:utf-8 -*-


import tornado.ioloop
import tornado.web
from WebHandlers import MainHandler, GetInterHandler, SetInterHandler


class WebView(object):
    def __init__(self, port=8888, controller = None):
        self.controller = controller
        self.port = port

    def add_controller(self, controller):
        self.controller = controller
        self.init_webapp()

    def init_webapp(self):
        self.application = tornado.web.Application([
                                            (r"/", MainHandler),
                                            (r"/index.html", MainHandler),
                                            (r"/inter/get/.*", GetInterHandler, dict(controller=self.controller)),
                                            (r"/inter/set/.*", SetInterHandler, dict(controller=self.controller)),
                                         ])
        self.application.listen(self.port)

    def start(self):
        print "Starting View"
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
    v = WebView()
    v.add_controller(c)
    v.start()

