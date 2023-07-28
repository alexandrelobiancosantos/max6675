import serial
import datetime
import matplotlib.pyplot as plt

# Defina a porta serial e a taxa de transmissão
serial_port = 'COM4'  # Atenção ao número da porta serial do Arduino (por exemplo, COM4 no Windows ou /dev/ttyUSB0 no Linux)
baud_rate = 9600

# Obter a data e hora atual
data_inicio_log = datetime.datetime.now()

# Nome do arquivo de log
nome_arquivo = data_inicio_log.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

# Abre a porta serial
ser = serial.Serial(serial_port, baud_rate)

# Listas para armazenar os dados para o gráfico
tempos = []
temperaturas = []
max_pontos_grafico = 25  # Limite de pontos exibidos no gráfico

try:
    with open(nome_arquivo, 'w') as file:
        while True:
            # Lê uma linha da porta serial (leitura dos dados do Arduino)
            line = ser.readline().decode().strip()

            try:
                # Separa o valor lido para tratamento de erro
                line1 = line.index(': ')
                line2 = line.index('*')
                # Remove a parte do texto e mantém apenas o valor da temperatura
                value = float(line[line1 + 2:line2].strip())
            except ValueError:
                value = 0.0

            # Trata erro de leitura = 0
            if line.startswith("Temperatura:"):
                if value == 0.0:
                    temperature = "sensor off\n"
                else:
                    temperature = f"{value}°C\n"

                # Obter a data e hora atual
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Escreve a data, hora e valor da temperatura no arquivo de log
                file.write(f"MAX6675-k, {current_time}, {temperature}")
                file.flush()

                # Exibe também no console para visualização em tempo real
                print(f"MAX6675-k, {current_time}, Temperatura: {temperature}")

                # Adiciona os valores às listas para o gráfico
                tempos.append(current_time)
                temperaturas.append(value)

                # Limitar a quantidade de pontos exibidos no gráfico
                if len(tempos) > max_pontos_grafico:
                    tempos.pop(0)
                    temperaturas.pop(0)

                # Plota o gráfico em tempo real
                plt.clf()  # Limpa o gráfico anterior para evitar sobreposição
                plt.plot(tempos, temperaturas, 'b-o')
                plt.xlabel('Tempo')
                plt.ylabel('Temperatura (°C)')
                plt.title('MAX6675 - k')
                plt.xticks(rotation=45, ha='right')  # Rotação e alinhamento dos rótulos do eixo x
                plt.tight_layout()  # Ajusta o espaçamento das legendas
                plt.pause(0.1)  # Atualiza o gráfico a cada 0.1 segundo

except KeyboardInterrupt:
    pass

# Fecha a porta serial ao sair
ser.close()

