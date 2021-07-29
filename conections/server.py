import socket as sck
import json

host = "192.168.1.36"
port = 5500

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
 
while True:
    connection, addr = s.accept()
    print("Nueva connection: " + str(addr))

    # Send data
    data = "Datos enviados desde servidor"
    connection.send(bytes(data, "utf-8"))
 
    # Get data
    petition = connection.recv(1024)
    petition = petition.decode("utf-8") # Data to string
    
    separator = "_-_type_-_"
    if petition.count(separator) == 1:
        print("Data segura")
        data_type = petition[petition.find(separator) + len(separator):]
        petition = petition[:petition.find(separator)]
    else:
        print("Cuidado")
        pos = 0
        revision = petition

        while revision.count(separator) > 0:
            pos += revision.find(separator) + len(separator)
            revision = revision[revision.find(separator) + len(separator):]
        
        data_type = revision
        petition = petition[:pos - len(separator)]

    if data_type == "dict":
        res = {"connection" : eval(petition), "data_type" : data_type}
    
    elif data_type == "range" or data_type == "frozenset" or data_type == "bytearray":
        res = {"connection" : eval(petition), "data_type" : data_type}
    
    elif data_type != "str":
        res = {"connection" : eval(f"{data_type}({petition})"), "data_type" : data_type}
    
    else:
        res = {"connection" : petition, "data_type" : data_type}
    
    print(json.dumps(res, sort_keys=False, indent=4))

    if petition == "shootdown server":
        print("Shutting down server")
        break

    connection.close()