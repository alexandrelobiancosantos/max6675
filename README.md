# Sensor de Temperatura MAX6675

Este é um projeto simples que permite fazer o log dos dados de temperatura de um sensor MAX6675 em um arquivo TXT usando Python.

## Descrição

O projeto utiliza um Arduino com um sensor MAX6675 para medir a temperatura. O Arduino lê os dados do sensor e envia-os pela porta serial para o computador. Em seguida, um programa Python é executado no computador para receber os dados pela porta serial e gravá-los em um arquivo de log em formato TXT.

## Requisitos

- Arduino Nano
- Sensor MAX6675
- Cabo USB para conectar o Arduino ao computador
- Computador com Python instalado

## Bibliotecas Necessárias

### python
- `serial`: Para comunicação serial entre o Arduino e o computador.
- `datetime`: Para manipulação de data e hora no Python.

### arduino
MAX6675-library-master.zip

## Instalação

1. Conecte o sensor MAX6675 ao Arduino de acordo com o esquema de pinagem do projeto.

SO = 11; //PINO DIGITAL (SO)
CS = 12; //PINO DIGITAL (CS)
CLK = 13; //PINO DIGITAL (CLK / SCK)

2. Carregue o código Arduino fornecido para ler os dados do sensor MAX6675 e enviá-los pela porta serial.
3. No computador, certifique-se de ter Python instalado.

## Execução

1. No terminal ou prompt de comando, navegue até o diretório onde você salvou o script Python do projeto.
2. Execute o script Python

## Formato do Arquivo de Log

O arquivo `temperature_log.txt` conterá uma linha para cada leitura de temperatura realizada pelo sensor MAX6675. Cada linha terá o seguinte formato:


Isso significa que a leitura foi feita em 28 de julho de 2023, às 15:30:45, e a temperatura registrada foi de 25.5 graus Celsius.

## Personalização

Você pode modificar o código do Arduino e/ou do Python para atender às suas necessidades específicas. Por exemplo, é possível alterar o intervalo de leitura do sensor ou adicionar mais informações ao arquivo de log, como identificadores do sensor ou localização.

## Notas

- Certifique-se de ter os drivers USB do Arduino instalados corretamente no seu computador antes de executar o projeto.
- Mantenha o Arduino conectado ao computador via USB durante a execução do script Python para garantir a comunicação adequada entre os dispositivos.
-adicionada vrificação para problema de falha nas leituras

## Autores

Lo Bianco

## Licença

Copia e cola a vontade!!!