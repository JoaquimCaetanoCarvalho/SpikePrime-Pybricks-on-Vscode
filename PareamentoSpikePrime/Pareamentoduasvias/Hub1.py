# Importando as bibliotecas necessárias para o funcionamento do programa
# O programa que o spike pode ser emissor e receptor ao mesmo tempo, 
# ou seja, ele pode enviar e receber informações
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor
from pybricks.parameters import Button, Color, Icon
from pybricks.tools import wait

# Criando o objeto hub para o Spike Prime, configurando o canal de transmissão e observação
hub = PrimeHub(broadcast_channel=1, observe_channels=[2])

# Indicando que o Hub que irá transmitir no canal 1 e observar no canal 2 está ativo
hub.light.on(Color.BLUE)

# Loop infinito para verificar constantemente o estado dos botões e a recepção de informações
while True:
    # Verificando se o botão esquerdo está pressionado e transmitindo a informação correspondente
    if Button.LEFT in hub.buttons.pressed():
        hub.ble.broadcast(1)
        print("Botão pressionado")
    else:
        hub.ble.broadcast(0) 
        print("Botão não pressionado")
# Verificando se há alguma informação recebida no canal 2 e exibindo o ícone correspondente
    icone = hub.ble.observe(2)
    if icone == 100:
        hub.display.icon(Icon.HAPPY)
        print("Distância menor ou igual a 200mm")
    else:
        hub.display.icon(Icon.SAD)
        print("Distância maior que 200mm")
        wait(1000)