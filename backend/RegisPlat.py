from clients.Service import Service
from database.session import session
from database.models import Platillos
import json, os, datetime
from time import sleep

class Registro_Platillo(Service):
    def __init__(self):
        print("Servicio de Registro de Platillo")
        super().__init__("BURPL")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            nombre = climsg["nombre"]
            precio = climsg["precio"]
            if not db.query(Platillos).filter(Platillos.nombre == nombre).first():
                platillo = Platillos(nombre=nombre, precio=precio)
                db.add(platillo)
                db.commit()
                db.close()
                return 'Platillo Ingresado'
            else:
                db.close()
                return "El Platillo ya existe"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Registro_Platillo()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()
