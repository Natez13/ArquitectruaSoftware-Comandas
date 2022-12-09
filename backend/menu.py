from clients.Service import Service
from database.session import session
from database.models import Platillos, Miembro, Grupo, Evento, to_dict
import json, sys, os, datetime
from time import sleep

class Menu(Service):
    def __init__(self):
        print("Servicio para ver el Menu")
        super().__init__("BUSMN")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            #token = climsg["token"]
           # decoded = jwt.decode(
            #    token, os.environ['SECRET_KEY'], algorithms=['HS256'])
            platillos = []
            for platillo in db.query(Platillos).all():
                platillos.append(to_dict(platillo))
            if platillos:
                output = "----------------------------------------------------\n"
                for platillo in platillos:
                    output += "ID: "+str(platillo["id"])+"\n"
                    output += "Nombre: "+platillo["nombre"]+"\n"
                    output += "Precio: "+str(platillo["precio"])+"\n"
                    output += "----------------------------------------------------\n"
                # replace 0xde 
                output = output.replace("\xde", "")
                return (output)
            else:
                return "No hay platillos inscritos"
                    
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return "Error: " + str(e) + " " + fname + " " + str(exc_tb.tb_lineno)

def main():
    try:
        Menu()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

