from clients.Service import Service
from database.session import session
from database.models import Platillos
import json, os, datetime
from time import sleep

class Actualizar_Platillo(Service):
    def __init__(self):
        print("Servicio de Actualizar de Platillo")
        super().__init__("BUUPL")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            id = climsg["id"]
            nombre = climsg["nombre"]
            precio = climsg["precio"]
            if db.query(Platillos).filter(Platillos.id == id).first():
                platillo = db.query(Platillos).filter(Platillos.id == id).first()
                platillo.nombre=nombre
                platillo.precio=precio
                db.commit()
                db.close()
                return 'Platillo Actualizado'
            else:
                db.close()
                return "El Platillo no existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Actualizar_Platillo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
