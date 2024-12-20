from os import path

import os
import socket
import subprocess



#获取本机IPV4地址
def get_ipv4_address():
    # 获取主机名
    host_name = socket.gethostname()
    # 获取主机的 IPV4 地址
    host_ip = socket.gethostbyname(host_name)
    return host_ip

#获取本机IPV6地址的字符串
def get_ipv6_address():
    # 获取主机名
    host_name = socket.gethostname()
    # 获取主机的 IPV6 地址
    host_ip = socket.getaddrinfo(host_name, None, socket.AF_INET6)
    return host_ip[1][4][0]

# 定义一个函数，用于连接到服务器
def connect_to_server(address, port):
	# 创建一个 socket 对象
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	try:
		# 连接到指定的地址和端口
		sock.connect((address, port))
		print(f"Connected to {address}:{port}")
		
		# 发送数据
		message = "Hello, Server!"
		sock.sendall(message.encode('utf-8'))
		
		# 接收数据
		response = sock.recv(1024)
		print(f"Received: {response.decode('utf-8')}")
	
	except socket.error as e:
		print(f"Socket error: {e}")
	
	finally:
		# 关闭连接
		sock.close()
		print("Connection closed")
		
#创建一个IPV4服务器
def create_ipv4_server(address, port):
    # 创建一个 socket 对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # 绑定到指定的地址和端口
        sock.bind((address, port))
        print(f"Server is listening on {address}:{port}")
        
        # 监听连接
        sock.listen(1)
        
        # 等待连接
        connection, client_address = sock.accept()
        print(f"Connection from {client_address}")
        
        # 接收数据
        data = connection.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        
        # 发送数据
        message = "Hello, Client!"
        connection.sendall(message.encode('utf-8'))
    
    except socket.error as e:
        print(f"Socket error: {e}")
    
    finally:
        # 关闭连接
        connection.close()
        sock.close()
        print("Connection closed")

#创建一个IPV6服务器
def create_ipv6_server(address, port):
    # 创建一个 socket 对象
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    try:
        # 绑定到指定的地址和端口
        sock.bind((address, port))
        print(f"Server is listening on {address}:{port}")
        
        # 监听连接
        sock.listen(1)
        
        # 等待连接
        connection, client_address = sock.accept()
        print(f"Connection from {client_address}")
        
        # 接收数据
        data = connection.recv(1024)
        print(f"Received: {data.decode()}")
        
        # 发送数据
        message = "Hello, Client!"
        connection.sendall(message.encode('utf-8'))
    
    except socket.error as e:
        print(f"Socket error: {e}")
         # 关闭连接
        connection.close()
    finally:
       
        sock.close()
        print("Connection closed")



#创建一个HTTP服务器，使用IPV6地址
def create_http_server(address, port):
    # 创建一个 socket 对象
    sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
    
    try:
        # 绑定到指定的地址和端口
        sock.bind((address, port))
        print(f"Server is listening on {address}:{port}")
        
        # 监听连接
        sock.listen(10)
        
        while True:
            # 等待连接
            connection, client_address = sock.accept()
            print(f"Connection from {client_address}")

            
            
            response = "HTTP/1.1 200 OK\nContent-Type: text/html\n\n".encode()
            with open("index.html", "rb") as file:
                html = file.read()
            response += html
            
            connection.sendall(response)
            # 接收数据
            data = connection.recv(1024)
            print(f"Received: {data.decode()}")
            # 关闭连接
            connection.close()
            print("Connection closed")

    except socket.error as e:
        print(f"Socket error: {e}")
        if(e.errno == 10048):
            print("端口被占用")
            os.system("netstat -ano | findstr 81")
            os.system("taskkill /f /pid 4")
            print("端口被释放")
            
    finally:
        # 关闭连接
        sock.close()
        print("Connection closed")
        #create_http_server(address, port)
#创建一个DDNS服务器
def run_ddns_exe():
    try:
        # 使用 subprocess.run 打开并运行 ddns.exe
        result = subprocess.run([".\\ddns.exe"], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error running ddns.exe: {e}")
