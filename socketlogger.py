# -*- coding: utf-8 -*-
'''
Created on 2013-3-16

@author: qiangwang
'''
import logging
import datetime
from Queue import Queue
from threading import Thread
import time

class SocketLogger():
    def __init__(self, logpath):
        self.logger = logging.getLogger(logpath)
        self.handler = logging.FileHandler(logpath)
        formatter = logging.Formatter('%(asctime)s %(levelname)s - %(message)s');
        self.handler.setFormatter(formatter)
        self.logger.setLevel(logging.DEBUG)
#        self.logger.addHandler(self.handler)
        self.queue = Queue()
        self.wthread = Thread(target = self.__write__)
        self.wthread.start();

    def __write__(self):
        while True:
            if self.queue.qsize() > 0:
                self.logger.addHandler(self.handler)
                self.logger.info(self.queue.get())
                self.handler.flush()
                self.logger.removeHandler(self.handler)
            else:
                # 不sleep一会，cpu会很高
                time.sleep(1)
                continue

    def info(self, msg):
        if self.queue.qsize() < 10000:
            self.queue.put(msg)
#        self.logger.info(msg)
#        self.handler.flush()

def getDailyLogger():
    return SocketLogger(str(datetime.date.today()) + '.log')

if __name__ == '__main__':
    print datetime.date.today()
#    slogger = getDailyLogger()
#    slogger.info('sdfd')