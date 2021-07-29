import socket as sck
import json
 
s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind((sck.gethostname(), 5500))
s.listen(5)
 
while True:
    conexion, addr = s.accept()
    print("Nueva conexion: " + str(addr))

    # Enviar datos
    data = "Datos enviados desde servidor"
    conexion.send(bytes(data, "utf-8"))
 
    # Recibir datos
    peticion = conexion.recv(1024)
    peticion = peticion.decode("utf-8") # Datos a str
    
    try:
        res = {"conexion" : eval(peticion)}
        print(json.dumps(res, sort_keys=False, indent=4))
    except:
        res = {"conexion" : peticion}
        print(res)

    if peticion == "shootdown server":
        print("Apagando servidor")
        break

    conexion.close()