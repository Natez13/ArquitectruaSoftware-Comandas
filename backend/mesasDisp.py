from clients.Service import Service
from database.session import session
from database.models import Mesas, Miembro, Grupo, Evento, to_dict
import json, sys, os, datetime
from time import sleep

class Mesas_Disp(Service):
    def __init__(self):
        print("Servicio para ver las Mesas Disponibles")
        super().__init__("BUSMD")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            #token = climsg["token"]
           # decoded = jwt.decode(
            #    token, os.environ['SECRET_KEY'], algorithms=['HS256'])
            mesas_list = []
            for mesas in db.query(Mesas).all():
                mesas_list.append(to_dict(mesas))
            if mesas_list:
                output = "----------------------------------------------------\n"
                for mesas in mesas_list:
                    output += "Numero: "+str(mesas["numero"])+"\n"
                    output += "Capacidad: "+str(mesas["capacidad"])+"\n"
                    output += "Disponible: "+str(mesas["disponible"])+"\n"
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
        Mesas_Disp()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

