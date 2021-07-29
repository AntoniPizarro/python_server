import socket as sck
 
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect((sck.gethostname(), 5500))

# Enviar datos
data = {
    "name" : "Toni",
    "surname" : "Pizarro",
    "age" : 22
}
data = "shootdown server"
s.send(bytes(str(data), "utf-8"))

# Recibir datos
res = s.recv(1024)
res =res.decode("utf-8") # Datos a str
print(res)

s.close()