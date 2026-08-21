import socket

target="www.geeksforgeeks.org"
port=80

request = (
    "GET / HTTP/1.1\r\n"
    "Host: www.geeksforgeeks.org\r\n"
    "Connection: close\r\n"
    "\r\n"
)

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.settimeout(3)
    result=s.connect_ex((target,port))
    

    if result==0:
        s.sendall(req.encode())
        res=s.recv(1024)
        print(res.decode())

except Exception as e:
    print("Error:", e)

finally:
    s.close()

