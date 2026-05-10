# Importa as bibliotecas nessárias para controlar o hub e exibir imagens na tela.
from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Icon

# Cria uma instância do PrimeHub para controlar o hub.
hub = PrimeHub()

# Exibe um ponto branco na posição (3, 3) da tela do hub.
hub.display.pixel(3, 3, 255)
wait(5000)

# Exibe um ícone de rosto feliz na tela do hub.
hub.display.icon(Icon.HAPPY)
wait(5000)