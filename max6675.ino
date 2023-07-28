#include "max6675.h" //INCLUSÃO DE BIBLIOTECA

int ktcSO = 11; //PINO DIGITAL (SO)
int ktcCS = 12; //PINO DIGITAL (CS)
int ktcCLK = 13; //PINO DIGITAL (CLK / SCK)

MAX6675 ktc(ktcCLK, ktcCS, ktcSO); //CRIA UMA INSTÂNCIA UTILIZANDO OS PINOS (CLK, CS, SO)
  
void setup(){
  Serial.begin(9600); //INICIALIZA A SERIAL
  delay(500); //INTERVALO DE 500 MILISSEGUNDOS
}

void loop(){
   Serial.print("Temperatura: "); //IMPRIME O TEXTO NO MONITOR SERIAL
   Serial.print(ktc.readCelsius()); //IMPRIME NO MONITOR SERIAL A TEMPERATURA MEDIDA
   Serial.println("*C"); //IMPRIME O TEXTO NO MONITOR SERIAL
   delay(60000); //INTERVALO DE 500 MILISSEGUNDOS
}