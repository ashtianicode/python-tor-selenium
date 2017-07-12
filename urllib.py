#https://gist.github.com/KhepryQuixote/46cf4f3b999d7f658853
#polipo socksParentProxy=localhost:9050

# tor starts on 127.0.0.1:9050 and because of torrc controller starts in 9051
# polipo converts socks proxy of tor to http proxy
### ====> for using with urllib2 it routes socks to socket of python connection

import urllib2
import socks
import socket
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

urllib2.urlopen("url") # now it uses python socket which is the tor connection actually