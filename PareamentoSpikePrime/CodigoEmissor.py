from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

hub = PrimeHub(broadcast_channel=1)
motor1 = Motor(Port.E)

while True:
    motor1.run(500)
    wait(1000)
    motor1.run(-500)
    wait(1000)