# Importando as bibliotecas necessárias para o funcionamento do código
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port, Button, Color
from pybricks.tools import wait

# Configurando o hub para observar no canal 1
hub = PrimeHub(observe_channels=[1])

# Configurando a luz do hub para verde para indicar que o receptor está ativo
hub.light.on(Color.GREEN)

# Configurando os motores conectados às portas E e F
motoresquerdo = Motor(Port.E)
motordireito = Motor(Port.F)

# Loop principal do programa, onde o receptor verifica constantemente os dados recebidos
while True:
    # Verificando os dados recebidos e controlando os motores de acordo com as condições recebidas
    data = hub.ble.observe(0)
    # Controlando os motores com base nos dados recebidos
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