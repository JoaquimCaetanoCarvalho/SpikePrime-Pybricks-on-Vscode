from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Button
from pybricks.parameters import Color

hub = PrimeHub(broadcast_channel=1)

hub.light.on(Color.BLUE)

while True:
    button = hub.buttons.pressed()
    if Button.LEFT in button:
        hub.ble.broadcast(1)
        print("Condição Enviada: Mover pra Frente")
    elif Button.RIGHT in button:
        hub.ble.broadcast(2)
        print("Condição Enviada: Mover pra Trás")
    else:
        hub.ble.broadcast(0)
        print("Nenhuma Condição Enviada")
    wait(1000)