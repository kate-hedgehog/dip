#библиотека https://pypi.org/project/PySocks/

import socket
import socks


ip='127.0.0.1'
port = 4444

socks.setdefaultproxy(socks.SOCKS5, ip, port)
s = socks.socksocket()
s.connect(("192.168.220.63", 80))
s.sendall("GET / HTTP/1.1 ...")
print(s.recv(4096))


#Ошибка
'''Traceback (most recent call last):
  File "/usr/local/lib/python3.7/dist-packages/socks.py", line 787, in connect
    super(socksocket, self).connect(proxy_addr)
ConnectionRefusedError: [Errno 111] Connection refused

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "socks_proxy.py", line 33, in <module>
    s.connect(("192.168.220.63", 80))
  File "/usr/local/lib/python3.7/dist-packages/socks.py", line 47, in wrapper
    return function(*args, **kwargs)
  File "/usr/local/lib/python3.7/dist-packages/socks.py", line 800, in connect
    raise ProxyConnectionError(msg, error)
socks.ProxyConnectionError: Error connecting to SOCKS5 proxy 127.0.0.1:4444: [Errno 111] Connection refused
'''
