from clients.Service import Service
from database.session import session
from database.models import PedidoPlatillo,Pedido, Platillos, to_dict
import json, sys, os, datetime
from time import sleep

class Pedido_Update(Service):
    def __init__(self):
        print("Servicio de Atualizacion de Pedido")
        super().__init__("BUSPU")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            numero = climsg["n_mesa"]
            id_platillo = climsg["id_patillo"]
            id_platillo_new = climsg["id_patillo_new"]
            #platillos = []
            if  db.query(Pedido).filter(Pedido.numero_mesa==numero, Pedido.terminado == False).first():
                pedido = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()
                pedplat = db.query(PedidoPlatillo).filter(PedidoPlatillo.id_pedido == pedido.id, PedidoPlatillo.id_plato == id_platillo).first()
                if id_platillo_new == '-1':
                    db.delete(pedplat)
                    db.commit()
                    db.close()
                else:
                    #platillos.append(to_dict(pedplat))
                    #print(platillos)
                    pedplat.id_plato=id_platillo_new
                    db.commit()
                    db.close()
                return 'Se modifico el platillo a la mesa numero '+str(numero)#+' asignada'#+' con pedido id: '+str(pedido_id.id)
            else:
                db.close()
                return "La mesa no tiene pedido"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Pedido_Update()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

