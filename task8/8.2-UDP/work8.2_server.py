#coding:utf-8
import socket
from time import ctime
host = ''   #host为空表示bind可以绑定到所有有效地址上
port = 23456
bufsiz = 1024
ADDR = (host,port)

udpSerSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udpSerSock.bind(ADDR)

try:
    while True:
        print 'waiting for connection...'
        data,addr = udpSerSock.recvfrom(bufsiz)
        udpSerSock.sendto('[%s] %s' %(ctime(),data),addr)
        if data == 'exit':
            break
        print '...received from and returned to:',addr
except BaseException, e:
    print e
    udpSerSock.close()