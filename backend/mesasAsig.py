from clients.Service import Service
from database.session import session
from database.models import Mesas,Pedido, Miembro, Grupo, Evento, to_dict
import json, sys, os, datetime
from time import sleep

class Mesas_Asig(Service):
    def __init__(self):
        print("Servicio de Asignacion de Mesas")
        super().__init__("BUSMA")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            numero = climsg["n_mesa"]
            id_personal = climsg["id_personal"]
            if  db.query(Mesas).filter(Mesas.numero == numero, Mesas.disponible == True).first():
                mesas = db.query(Mesas).filter(Mesas.numero == numero).first()
                mesas.disponible=False
                db.commit()
                pedido = Pedido(numero_mesa=numero, id_personal=id_personal, terminado=False)
                db.add(pedido)
                db.commit()
                #pedido_id = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()
                db.close()
                return 'Mesa numero '+str(numero)+' asignada'#+' con pedido id: '+str(pedido_id.id)
            else:
                db.close()
                return "La mesa esta ocupada"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Mesas_Asig()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

