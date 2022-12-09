from clients.Service import Service
from database.session import session
from database.models import Personal, to_dict
import json, sys, os, datetime
from time import sleep

class Ver_Personal(Service):
    def __init__(self):
        print("Servicio para ver el Personal")
        super().__init__("BUSVP")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            #token = climsg["token"]
           # decoded = jwt.decode(
            #    token, os.environ['SECRET_KEY'], algorithms=['HS256'])
            personal = []
            for persona in db.query(Personal).all():
                personal.append(to_dict(persona))
            if personal:
                output = "----------------------------------------------------\n"
                for persona in personal:
                    output += "ID: "+str(persona["id"])+"\n"
                    output += "Nombre: "+persona["nombre"]+"\n"
                    output += "----------------------------------------------------\n"
                # replace 0xde 
                output = output.replace("\xde", "")
                return (output)
            else:
                return "No hay usuarios"
                    
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return "Error: " + str(e) + " " + fname + " " + str(exc_tb.tb_lineno)

def main():
    try:
        Ver_Personal()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

