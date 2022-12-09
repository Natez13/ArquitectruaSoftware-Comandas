from clients.Service import Service
from database.session import session
from database.models import PedidoPlatillo,Pedido, Platillos, Mesas, to_dict
import json, sys, os, datetime
from time import sleep
# calcula el total
# elemina los platillos en pedidosporplatillos
# liberea la mesa
# cambia el estado del pedido
class Ver_Pedido(Service):
    def __init__(self):
        print("Servicio de ver Pedido")
        super().__init__("BUVPE")
        self.start_service(debug=True)

    def service_function(self, climsg):
        '''Funcion temporal, sera reemplazada en los distintos servicios'''
        db = session()
        try:
            climsg = json.loads(climsg)
            numero = climsg["numero"]
            pedplat_arry = []
            #platillos = []
            if  db.query(Pedido).filter(Pedido.numero_mesa==numero, Pedido.terminado == False).first():
                pedido = db.query(Pedido).filter(Pedido.numero_mesa == numero, Pedido.terminado == False).first()

                for pedplat in db.query(PedidoPlatillo).filter(PedidoPlatillo.id_pedido == pedido.id).all():
                    pedplat_arry.append(to_dict(pedplat))
                if pedplat_arry:
                    print(pedplat_arry)
                    output = "----------------------------------------------------\n"
                    for pedplat in pedplat_arry:
                        platillo = db.query(Platillos).filter(Platillos.id == pedplat["id_plato"]).first()
                        output += "ID: "+str(platillo.id)+"\n"
                        output += "Nombre: "+platillo.nombre+"\n"
                        output += "Precio: "+str(platillo.precio)+"\n"
                        output += "----------------------------------------------------\n"
                        # replace 0xde 
                    output = output.replace("\xde", "")
                    return (output)
            else:
                db.close()
                return "La mesa no tiene pedido"
        except Exception as e:
            db.close()
            return str(e)

def main():
    try:
        Ver_Pedido()
    except Exception as e:
        print(e)
        sleep(30)
        main()

if __name__ == "__main__":
    main()

