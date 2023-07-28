import serial
import datetime

# Defina a porta serial e a taxa de transmissão
serial_port = 'COM4'  # Substitua 'x' pelo número da porta serial do Arduino (por exemplo, COM3 no Windows ou /dev/ttyUSB0 no Linux)
baud_rate = 9600

# Nome do arquivo de log
log_file = 'log_temperature.txt'

# Abre a porta serial
ser = serial.Serial(serial_port, baud_rate)

try:
    with open(log_file, 'w') as file:
        while True:
            # Lê uma linha da porta serial (leitura dos dados do Arduino)
            line = ser.readline().decode().strip()

            # Verifica se a linha começa com "Temperatura:"
            if line.startswith("Temperatura:"):
                # Remove a parte do texto e mantém apenas o valor da temperatura
                temperature = line.replace("Temperatura:", "").replace("*C", "").strip()

                # Obter a data e hora atual
                current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Escreve a data, hora e valor da temperatura no arquivo de log
                file.write(f"MAX6675-k, {current_time}, {temperature}°C\n")
                file.flush()

                # Exibe também no console para visualização em tempo real
                print(f"MAX6675-k, {current_time}, Temperatura: {temperature}°C")

except KeyboardInterrupt:
    pass

# Fecha a porta serial ao sair
ser.close()
