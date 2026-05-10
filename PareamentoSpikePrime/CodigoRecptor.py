from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub(observe_channels=[1])

hub.light.on(Color.GREEN)

motoresquerdo = Motor(Port.E)
motordireito = Motor(Port.F)

while True:
    data = hub.ble.observe(0)
    if data == 1:
        motoresquerdo.run(500)
        motordireito.run(-500)
        print("Condição Recebida: Mover pra Frente")
    elif data == 2:
        motoresquerdo.run(-500)
        motordireito.run(500)
        print("Condição Recebida: Mover pra Trás")
    else:
        motoresquerdo.stop()
        motordireito.stop()
        print("Nenhuma Condição Recebida")
    wait(1000)