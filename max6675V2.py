import serial
import datetime

# Defina a porta serial e a taxa de transmissão
serial_port = 'COM4'  # Substitua 'x' pelo número da porta serial do Arduino (por exemplo, COM3 no Windows ou /dev/ttyUSB0 no Linux)
baud_rate = 9600

# Obter a data e hora atual
data_inicio_log = datetime.datetime.now()

# Nome do arquivo de log
nome_arquivo = data_inicio_log.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"

# Abre a porta serial
ser = serial.Serial(serial_port, baud_rate)

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

except KeyboardInterrupt:
    pass

# Fecha a porta serial ao sair
ser.close()
