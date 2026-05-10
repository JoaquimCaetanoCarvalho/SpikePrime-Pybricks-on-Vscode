# Importando as bibliotecas necessárias para o funcionamento do código
# O programa que o spike pode ser emissor e receptor ao mesmo tempo
# ou seja, ele pode enviar e receber informações
from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Criando o objeto hub para o Spike Prime, configurando o canal de transmissão e observação
hub = PrimeHub(broadcast_channel=2, observe_channels=[1])

# Indicando que esse Hub irá utilizar os motores e sensores conectados
motor_esq = Motor(Port.E)
motor_dir = Motor(Port.F)
ultrasonico  = UltrasonicSensor(Port.B)

# Indicando que canal de transmissão os dados serão passados
hub.ble.broadcast(2)
hub.ble.observe(1)

# Loop infinito para verificar constantemente o estado dos botões e a recepção de informações
while True:

# Verificando se há alguma informação recebida no canal 1 e executando o comando correspondente
    comando = hub.ble.observe(1)

    if comando == 1:
        motor_esq.run(720)
        motor_dir.run(-720)
        print("Botão pressionado")
    else:
        motor_esq.stop()
        motor_dir.stop()
        print("Botão não pressionado")
    # Verificando a distância medida pelo sensor ultrassônico e transmitindo a informação correspondente
    distancia = ultrasonico.distance()

# Verificando se a distância medida está dentro do intervalo desejado e transmitindo a informação correspondente
    if 40 < distancia < 200:
        hub.ble.broadcast(100)
        print("Distância menor ou igual a 200mm")
    else:
        hub.ble.broadcast(0)
        print("Distância maior que 200mm")
    wait(100)