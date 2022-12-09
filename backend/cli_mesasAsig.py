from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Asignacion de mesa")
    keep_alive = True
    try:
        while(keep_alive):
            n_mesa = input("Ingrese el numero de mesa: ")
            id_personal = input("Ingrese el id del personal que atendera la mesa: ")
            try: 
                climsg = {
                    "n_mesa": n_mesa,
                    "id_personal": id_personal
                }
                a = Client("BUSMA")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()