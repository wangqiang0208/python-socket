# -*- coding: utf-8 -*-
"""
Created on 2012-12-2

@author: qiangwang
"""
from socket import *
import uuid
from threading import Thread
import time


def connection(name, host, port):
    count = 0
    while count < 10:
        addr = (host, port)
        socketClient = socket(AF_INET, SOCK_STREAM)
        socketClient.connect(addr)
        count = count + 1
        socketClient.send('%s send %d' % (name, count))
        data = socketClient.recv(1024)
        if not data:
            break
        print data
        socketClient.close()
        time.sleep(10 / 10)
    
if __name__ == "__main__":
    HOST = "192.168.3.103"
    PORT = 54321
    
    for i in range(0, 5):
        name = uuid.uuid4().time_mid
        t = Thread(target = connection, args=(name, HOST, PORT))
        t.start();