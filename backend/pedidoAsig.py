from clients.Service import Service
from database.session import session
from database.models import PedidoPlatillo,Pedido, Platillos, to_dict
import json, sys, os, datetime
from time import sleep

class Pedido_Asig(Service):
    def __init__(self):
        print("Servicio de Asignacion de Pedido")
        super().__init__("BUPEA")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            numero = climsg["n_mesa"]
            id_platillo = climsg["id_patillo"]
            if  db.query(Pedido).filter(Pedido.numero_mesa==numero, Pedido.terminado == False).first():
                pedido = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()
                pedplat = PedidoPlatillo(id_pedido=pedido.id,id_plato=id_platillo)                
                db.add(pedplat)
                db.commit()
                #pedido_id = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()
                db.close()
                return 'Se agrego el platillo a la mesa numero '+str(numero)#+' asignada'#+' con pedido id: '+str(pedido_id.id)
            else:
                db.close()
                return "La mesa no tiene pedido"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Pedido_Asig()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

