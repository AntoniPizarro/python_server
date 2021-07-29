import socket as sck

def send_data(data, host="localhost", port=5500):

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect((host, port))

    # Send data
    type_nom = str(type(data))
    data_type = "_-_type_-_" + type_nom[type_nom.find("'") + 1:type_nom.find("'>")]
    if type(data) != str:
        s.send(bytes(str(data) + data_type, "utf-8"))
    else:
        s.send(bytes(data + data_type, "utf-8"))

    # Get data
    res = s.recv(1024)
    res =res.decode("utf-8") # Data to string
    print(res)

    s.close()

def close_server(host="localhost", port=5500):
    data = "shootdown server"

    s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
    s.connect((host, port))

    # Send data
    type_nom = str(type(data))
    data_type = "_-_type_-_" + type_nom[type_nom.find("'") + 1:type_nom.find("'>")]
    if type(data) != str:
        s.send(bytes(str(data) + data_type, "utf-8"))
    else:
        s.send(bytes(data + data_type, "utf-8"))

    # Get data
    res = s.recv(1024)
    res =res.decode("utf-8") # Data to string
    print(res)

    s.close()