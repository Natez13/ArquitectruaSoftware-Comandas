from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Registro de Platillo")
    keep_alive = True
    try:
        while(keep_alive):
            nombre = input("Ingrese el nombre del platillo: ")
            precio = input("Ingrese el precio del platillo: ")
            
            try: 
                climsg = {
                    "nombre": nombre,
                    "precio": precio,
                }
                a = Client("BURPL")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()