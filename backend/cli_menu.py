from clients.Client import Client
from getpass import getpass
import json
        
if __name__ == "__main__":
    print("Service: Ver Menu")
    keep_alive = True
    try:
        while(keep_alive):
            print('Servicio accesible')
            input('Presione cualquier tecla paara continuar...')
            token = ''
            try: 
                a = Client("BUSMN")
                climsg = {
                    "token": token,
                }
                msg = a.exec_client(debug=True, climsg=json.dumps(climsg))
                print("###################################\n\n", msg, "\n\n###################################")
                
            except Exception as e:
                print("Error: ", e)
    except KeyboardInterrupt:
        print("\nCerrando cliente, hasta pronto ....")
        keep_alive = False
        exit()