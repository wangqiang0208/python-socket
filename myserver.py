# -*- coding: utf-8 -*-
'''
Created on 2012-12-2

@author: qiangwang
'''
from socket import *
from time import ctime
from serverthread import *
from socketlogger import *

if __name__ == "__main__":
    
    HOST = "192.168.3.100"
    PORT = 54321
    ADDR = (HOST, PORT)
    mysocket = socket(AF_INET, SOCK_STREAM)
    mysocket.bind(ADDR)
    mysocket.listen(5)
    
    print 'server ready, at port:%d' % PORT
    log = getDailyLogger()
    while True:
        connection, address = mysocket.accept()
        
        if connection == None or address == None:
            continue

        st = ServerThread(connection, address, log)
        st.start()

    mysocket.close()