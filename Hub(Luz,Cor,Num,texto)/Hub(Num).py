# importo os modulos do pybricks para poder utiliar o hub e a função de espera
from pybricks.hubs import PrimeHub
from pybricks.tools import wait

#inicializo o hub para poder usar a função de texto
hub = PrimeHub()

#utilizo a função de número para mostrar as mensagens na tela do hub
hub.display.number(16)

#função de espera para esperar 2 segundos entre cada mensagem
wait(1000)
hub.display.number(8)
wait(1000)