from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Eliminar Platillo")
    keep_alive = True
    try:
        while(keep_alive):
            id = input("Ingrese el id del platillo a eliminar: ")
            
            try: 
                climsg = {
                    "id": id,
                }
                a = Client("BUDPL")
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()