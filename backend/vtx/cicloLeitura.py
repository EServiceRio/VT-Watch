from .models import Gateway, Hist, Node, NodeSetup, Evento
from time import sleep
from threading import Thread
from datetime import datetime, timedelta
from dxm.protocolo import Protocolo

def leitura():
    controle = True
    while controle:
        try:
            sleep(2)
            ip = Gateway.objects.all()[0]
            nodes = Node.objects.all()
            setups = NodeSetup.objects.all()
            for n in nodes:
                info = setups.get(node=n.id)
                dxm = Protocolo(ip.port)
                n.vibraX = dxm.readReg(info.addrVibraX,1,slaveID=info.address)[0]
                n.vibraX2 = dxm.readReg(info.addrVibraX2,1,slaveID=info.address)[0]
                n.vibraZ = dxm.readReg(info.addrVibraZ,1,slaveID=info.address)[0]
                n.vibraZ2 = dxm.readReg(info.addrVibraZ2,1,slaveID=info.address)[0]
                n.temp = dxm.readReg(info.addrTemp,1,slaveID=info.address)[0]
                n.corrente = dxm.readReg(info.addrCorrente,1,slaveID=info.address)[0]
                n.save()
            ip.online=True
            ip.save()
        except KeyboardInterrupt:
            controle = False
        except Exception as EX:
            ip = Gateway.objects.all()[0]
            ip.online = False
            ip.save()
            sleep(5)
            print(f"falha na leitura {str(EX)}")

th = Thread(target=leitura).start()