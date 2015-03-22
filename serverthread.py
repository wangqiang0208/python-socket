# -*- coding: utf-8 -*-
'''
Created on 2013-3-16

@author: qiangwang
'''

from socket import *
from threading import Thread
import uuid

if __name__ == '__main__':
    print dir(uuid.uuid4())
    print uuid.uuid4().time_mid
    
class ServerThread(Thread):
    def __init__(self, conn, addr, log):
        Thread.__init__(self)
        self.__id__ = uuid.uuid4()
        self.__conn__ = conn
        self.__addr__ = addr
        self.__logger__ = log
    
    def run(self):
        self.__logger__.info('server thread %s' % self.__id__)
        self.__logger__.info('work for %s:%s' % self.__addr__)
        while True:
            data = None
            try:
                data = self.__conn__.recv(1024)
            except:
                data = None

            if not data or len(data) == 0:
                try:
                    self.__logger__.info('%s send no data' % self.__id__)
                    self.__conn__.send('no data')
                except:
                    self.__logger__.info('%s send no data error' % self.__id__)
                break
            elif data == 'q':
                self.__logger__.info('%s close connection' % self.__id__)
                self.__conn__.send('close connection')
                self.__conn__.close()
                break
            else:
                self.__logger__.info('%s send data: %s' % (self.__id__, data))
                self.__conn__.send('Response: %s' % data)
                break
        
        self.__conn__.close()
        self.__logger__.info('socket closed')
                