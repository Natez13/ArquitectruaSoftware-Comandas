from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Actualizacion de pedido")
    keep_alive = True
    try:
        while(keep_alive):
            n_mesa = input("Ingrese el numero de mesa: ")
            id_patillo = input("Ingrese el id del platillo a cambiar: ")
            id_patillo_new = input("Ingrese el id del nuevo platillo: ")
            try: 
                climsg = {
                    "n_mesa": n_mesa,
                    "id_patillo": id_patillo,
                    "id_patillo_new":id_patillo_new
                }
                a = Client("BUSPU")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()