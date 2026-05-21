# Importo as bibliotecas necessárias para controlar os motores e o hub
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait

# Inicializo o hub e os motores conectados às portas F e E
hub = PrimeHub()

motor_esq = Motor(Port.F)
motor_dir = Motor(Port.E)

# Loop infinito para rodar os motores em um ciclo de movimento e pausa
while True:
    # rodos os dois motores juntos para frente controlando a velocidade e o comprimento
    motor_esq.run_angle(150, -720, wait = False)
    motor_dir.run_angle(150, 720, wait = True)

    # paro os motores e espero por 5 segundos antes de iniciar o próximo ciclo
    motor_esq.stop()
    motor_dir.stop()
    wait(5000)