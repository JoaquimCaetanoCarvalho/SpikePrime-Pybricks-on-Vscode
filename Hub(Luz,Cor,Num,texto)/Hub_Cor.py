# importo os modulos do pybricks para poder utiliar o hub e a função de espera
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color, Port
from pybricks.pupdevices import ColorSensor

#inicializo o hub para poder usar a função de luz
hub = PrimeHub()

#utilizo a função de luz para mostrar as mensagens na tela do hub
hub.light.on(Color.WHITE)
wait(1000)

hub.light.on(Color.RED)
wait(1000)

# defino a porta do sensor de cor para F e inicializo o sensor de cor para poder ler as cores
sensorcor = ColorSensor(Port.F)

# além de criar as cores pré-definidas do pybricks, crio as cores prata, preta, branca
Color.SILVER = Color(h=0, s=0, v=75)
Color.BLACK = Color(h=0, s=0, v=0)
Color.WHITE = Color(h=0, s=0, v=100)

# salvo as cores que podem ser detectadas pelo sensor em uma tupla
cores = (Color.WHITE, Color.YELLOW, Color.BLACK, Color.SILVER)

# permito que as as cores possam ser detectadas pelo sensor de cor
sensorcor.detectable_colors(cores)

# crio um loop infinito para que o sensor de cor possa ler as cores continuamente
while True:
    # defino a variavel cor para receber as cores detectadas pelo sensor de cor
    cor = sensorcor.color()
    # crio estruturas de condicionais para cada cor que for detectada pelo sensor
    if cor == Color.SILVER:
        print("cor prata detectada!")
    elif cor == Color.BLACK:
        print("cor preta detectada!")
    elif cor == Color.WHITE:
        print("cor branca detectada!")
    else:
        print("cor desconhecida detectada!")
    # utilizo a função de espera para que o sensor nao bugue ao detectar!
    wait(500)