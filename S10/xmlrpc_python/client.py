import xmlrpc.client

ser = xmlrpc.client.ServerProxy('http://192.168.25.12:8000')
res = ser.add(10, 20)

print(res)