#!/usr/bin/python
# -*- coding:utf-8 -*-

import serial
import time


class SerialCommunicator(object):
    def __init__(self, device, speed, cmd_timeout, send_interval, debug = False):
        """
        :param device: ex: /dev/ttyUSB0
        :param speed: ex: 9600
        :param cmd_timeout: timout after which function will return even if it didn't worked
        :param send_interval: interval for sending commands
        :param debug: debug flag (default is False)
        :return:
        """
        self.connection = serial.Serial(device, speed)
        self.cmd_timeout = cmd_timeout
        self.send_interval = send_interval
        self.debug = debug

    def close(self):
        try:
            self.connection.close()
        except:
            print "Problème de fermeture de la liaison", self.connection

    def send_while(self, cmd, until, max_delay = -1):
        self.connection.write('\r')
        if max_delay <0: max_delay = self.cmd_timeout # crappy way of managing default value
        start = end = time.time()
        line = self.connection.readline()
        while line.splitlines()[0] != until and end-start<max_delay:
            if self.debug:
                print "Sending {0} ... until {1}".format(cmd.strip(), until)
            self.connection.write(cmd)
            time.sleep(self.send_interval)
            line = self.connection.readline()
            print 'Data receivend : {0}'.format(line)
            end = time.time()
        if end-start > self.cmd_timeout:
            if self.debug:
                print "Delais maximum atteint"
        if self.debug:
            print 'Flushing Input'
        self.connection.flushInput()
    def send(self, cmd):
        self.connection.write(cmd)

if __name__ == '__main__':
    try:
        s = SerialCommunicator('/dev/ttyUSB0', 9600, 3, 1, True)
        s.send("OFF\r".encode())
        while(True):
            print "on"
            s.send_while('I {0} {1} {2}\r'.format('C', 2, '1'), '.')
            print "off"
            s.send_while('I {0} {1} {2}\r'.format('C', 2, '0'), '.')

    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        s.close()
