from clients.Service import Service
from database.session import session
from database.models import Platillos
import json, os, datetime
from time import sleep

class Eliminar_Platillo(Service):
    def __init__(self):
        print("Servicio de Eliminar de Platillo")
        super().__init__("BUDPL")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            id = climsg["id"]
            if db.query(Platillos).filter(Platillos.id == id).first():
                platillo = db.query(Platillos).filter(Platillos.id == id).first()
                db.delete(platillo)
                db.commit()
                db.close()
                return 'Platillo Eliminado'
            else:
                db.close()
                return "El Platillo no existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Eliminar_Platillo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
