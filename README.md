# -SpikePrime-Pybricks-on-Vscode-
  Esté é a introdução ao Utilizar o Pybricks, poder progamar com a API, modúlos e utilizar o firmware do Pybricks é necessário trocar o Driver do Hub do Spike Prime.
  - COMO TROCAR O DRIVER?
    - Para trocar o Driver é necessário coloca-lo no tipo de USB serial sem barramento universal, com o driver WinUSB
    - O WinUsb é o driver que permite a comunicação direta entre usuário e dispositivo USB eliminando a necessidade de desenvolver driver complexos e personalizados
    - Com o Software "Zadig" isso é possivel - https://zadig.akeo.ie/ -
    - Dentro do Software selecione o dispositivo DFU do Spike, verifique o USB ID(tem que ser de 0694:0008) e selecione o driver WinUsb e instale o Driver
    <img width="589" height="260" alt="zadig" src="https://github.com/user-attachments/assets/33618462-732a-4b84-b369-6da48de7820d" />
    - Com o Zadig instalado Pressione o Botão de Bluetooth do spike ate ficar com a coloração roxa e insira o cabo conectado ao computador assim entrando em modo download
    - Terminado assim a instalação do driver, indo pra ultima etapa de Atualização de Firmware do pybricks
  - COMO ATUALIZAR O FIRMWARE?
    - No site do Pybricks - https://code.pybricks.com/ -
    - Siga as instruções de instalação de firmware presente no site!
    - E indo para o Vscode para finalmente podermos começar a Progamar!!
  - INSTALAÇÃO NO VISUAL STUDIO CODE
    - Dentro do Vscode na aba de Extensão(obs: tenha o Python 3.12 para frente para evitar problemas!)
    - Na aba de Extensão Procure por: "Pybricks Runner" e "BlocklyPy" permitindo a conexão do Vscode com o SpikePrime
    <img width="815" height="213" alt="image" src="https://github.com/user-attachments/assets/12118a24-1bfb-4150-94b3-6c4af37e65b4" />
    <img width="1280" height="219" alt="image" src="https://github.com/user-attachments/assets/17188732-331a-4ff0-b75c-cd9839d3c984" />
  #  Crie um arquivo.py e abra e terminal e insira:
      pip install pybricks pybricksdev
   - (obs: lembre-se a pasta do python e a pasta dos scripts instalado em sua máquina deve estar no PATH, caso não esteja o PIP, nem o pybricks funcionará!)
   - agora siga as instruções presentes neste repostório e a documentação oficial do Pybricks!
   - Documentação: - https://docs.pybricks.com/en/latest/ -

