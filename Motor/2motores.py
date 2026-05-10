# Importo todas as bibliotecas necessárias para o funcionamento do programa
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

#Inicializo o hub e o motor que será utilizado para a rotação
hub = PrimeHub()
motor1 = Motor(Port.F)
motor2 = Motor(Port.E)

# Crio um loop infinito para que o motor fique rodando continuamente, e alternando o sentido
while True:
    motor1.run(500)
    motor2.run(-500)
    wait(1000)
    motor1.run(-500)
    motor2.run(500)
    wait(1000)
    # faz os motores pararem por um tempo, para depois recomeçar o ciclo
    motor1.stop()
    motor2.stop()
    wait(1000)