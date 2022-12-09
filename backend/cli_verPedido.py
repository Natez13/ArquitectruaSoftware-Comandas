from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Ver Pedido")
    keep_alive = True
    try:
        while(keep_alive):
            numero = input("Ingrese el numero de la mesa: ")
            try: 
                climsg = {
                    "numero": numero
                }
                a = Client("BUVPE")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()