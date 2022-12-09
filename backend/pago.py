from clients.Service import Service
from database.session import session
from database.models import PedidoPlatillo,Pedido, Platillos, Mesas, to_dict
import json, sys, os, datetime
from time import sleep
# calcula el total
# elemina los platillos en pedidosporplatillos
# liberea la mesa
# cambia el estado del pedido
class Pago(Service):
    def __init__(self):
        print("Servicio de Pago")
        super().__init__("BUSPA")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            numero = climsg["numero"]
            pedplat_arry = []
            total_price = 0
            #platillos = []
            if  db.query(Pedido).filter(Pedido.numero_mesa==numero, Pedido.terminado == False).first():
                pedido = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()
                mesa = db.query(Mesas).filter(Mesas.numero == numero).first()
                
                for pedplat in db.query(PedidoPlatillo).filter(PedidoPlatillo.id_pedido == pedido.id).all():
                    pedplat_arry.append(to_dict(pedplat))
                if pedplat_arry:
                    for pedplat in pedplat_arry:
                        platillo = db.query(Platillos).filter(Platillos.id == pedplat["id_plato"]).first()
                        print(platillo.precio)
                        total_price += platillo.precio
                
                db.query(PedidoPlatillo).filter(PedidoPlatillo.id_pedido == pedido.id).delete()
                db.commit()
                mesa.disponible = True
                db.commit()
                pedido.terminado = True
                db.commit()

                db.close()
                return 'Se envio el total a pagar al sistema de pago externo, total de pago:  '+str(total_price)#+' asignada'#+' con pedido id: '+str(pedido_id.id)
            else:
                db.close()
                return "La mesa no tiene pedido"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Pago()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

