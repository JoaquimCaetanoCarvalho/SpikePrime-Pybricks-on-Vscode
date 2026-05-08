# importo os modulos do pybricks para poder utiliar o hub e a função de espera
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Color

#inicializo o hub para poder usar a função de luz
hub = PrimeHub()

#utilizo a função de luz para mostrar as mensagens na tela do hub
hub.light.on(Color.WHITE)
wait(1000)

hub.light.on(Color.RED)
wait(1000)
