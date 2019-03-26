import socket
ms=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ainfo=socket.getaddrinfo('192.168.1.4',80)
ms.bind(ainfo[0][4])
ms.listen(5)
while True:
      conn,addr = ms.accept()
      print ('Got a request!')
conn.close()
ms.close()
	
