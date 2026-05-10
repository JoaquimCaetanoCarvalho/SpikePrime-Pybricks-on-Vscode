# Importando as bibliotecas necessárias para o funcionamento do código
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.tools import wait
from pybricks.parameters import Button
from pybricks.parameters import Color

# Configurando o hub para transmitir no canal 1
hub = PrimeHub(broadcast_channel=1)

# Configurando a luz do hub para azul para indicar que o emissor está ativo
hub.light.on(Color.BLUE)

# Loop principal do programa, onde o emissor verifica constantemente o estado dos botões e
# transmite as condições correspondentes
while True:
    # Verificando quais botões estão pressionados e transmitindo as condições correspondentes
    button = hub.buttons.pressed()
    if Button.LEFT in button:
        # Transmitindo a condição para mover para frente (1) se 
        # o botão esquerdo estiver pressionado
        hub.ble.broadcast(1)
        print("Condição Enviada: Mover pra Frente")
    elif Button.RIGHT in button:
        hub.ble.broadcast(2)
        print("Condição Enviada: Mover pra Trás")
    else:
        hub.ble.broadcast(0)
        print("Nenhuma Condição Enviada")
    wait(1000)