# -*- coding: utf-8 -*-
# Deal with py2 and py3 differences
try: # this only works in py2.7
    import configparser
except ImportError:
    import ConfigParser as configparser
from mtproto.Session import Session
from layers.Crypt import server1
from layers.MessageHandler import MessageHandler
from layers.Transport import TCPTransportLayer
from
from time import sleep
from mtproto import TL

config = configparser.ConfigParser()
# Check if credentials is correctly loaded (when it doesn't read anything it returns [])
if not config.read('credentials'):
    print("File 'credentials' seems to not exist.")
    exit(-1)
ip = config.get('App data', 'ip_address')
port = config.getint('App data', 'port')


server1 = TCPTransportLayer(ip, port)
cryptlayer = Cryptlayer(underlying_layer=server1)

S = Session(transport=server1)
i=0
while i<8:
    i+=1
    S.method_call('ping', ping_id=i)
