# -*- coding:utf-8 -*-

import threading
import time 
  
  
class ResetableTimer(object):
    def __init__(self, delay, target, auto_start=True, *args, **kwargs):
        self._target = target
        self._args = args 
        self._kwargs = kwargs 
        self._delay = delay
        if auto_start:
            self._thread = self._new_running_thread()
        else:
            self._thread = None

    def _run(self):
        self._target(*self._args, **self._kwargs)
    
    def reset(self):
        """
        Stop Current Thread and create a New one so that the countdown start again
        """
        self._thread.cancel()
        self._thread = self._new_running_thread()

    def _new_running_thread(self):
        t = threading.Timer(self._delay, self._run)
        t.start()
        return t


if __name__ == '__main__':
    def set_on(*args, **kwargs):
        print "Switching On !!"
    def set_off(*args, **kwargs):
        print "Switching Off !!"
    def set_something_with_parameters(param1=".", param2="+", param3="-", *args, **kwargs):
        print param1, param2, param3
        print kwargs
        myparam = kwargs.get('param', "rien")
        print "Some Func with param={0}".format(myparam)

    a = ResetableTimer(1.0, set_on)
    b = ResetableTimer(2.0, set_off)
    c = ResetableTimer(delay=1.0, target=set_something_with_parameters, kwargs=dict(param2="HEllow Orld 2!", param1="HEllow Orld 1!", param4="HEllow Orld 4!"))
    d = ResetableTimer(3.0, set_on)
    time.sleep(4)
    print "reset c..."
    c.reset()
    time.sleep(6)
    c.reset()
    time.sleep(10)
    print "End of code"
