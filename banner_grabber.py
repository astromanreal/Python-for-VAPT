import socket 

target="192.168.1.37"
port=445
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.settimeout(2)
    result=s.connect_ex((target,port))
    if result==0:
        banner=s.recv(1024)
        print(banner.decode())

except Exception as e:
    print("Error:", e)
    
finally:
     s.close()