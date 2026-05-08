# importo os modulos do pybricks para poder utiliar o hub e a função de espera
from pybricks import PrimeHub
from pybricks.tools import wait

#inicializo o hub para poder usar a função de texto
hub = PrimeHub()

#utilizo a função de texto para mostrar as mensagens na tela do hub
hub.display.text("Eu falei NASA Aé!")

#função de espera para esperar 2 segundos entre cada mensagem
wait(2000)
hub.display.text("Eu falei Atlas Aé!")
wait(2000)