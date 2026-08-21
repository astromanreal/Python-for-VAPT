import socket

try:
    target="192.168.1.37"
    
    for port in range(1, 65536):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result=s.connect_ex((target, port))
        if result==0:
            print(f"{port},open")
        s.close()
        
except Exception as e:
    print("Error:", e)
