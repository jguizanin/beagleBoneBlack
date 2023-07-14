import sensor_bme
import time
import csv

temperatura = []
humidade = []
pressao = []

#ESSE LOOP PODE SER TROCADO POR UMA LEITURA DE UM BOTÃO PARA PARAR O PROGRAMA
for i in range(0, 100):
  #Faz a leitura dos dados
    show = bme280_sensor.get_all()
    temp1 = bme280_sensor.get_tempf()
    temp2 = bme280_sensor.get_tempc()
    humid = bme280_sensor.get_humidity()
    press = bme280_sensor.get_pressure()

  #Sem a conexão em tempo real com o banco de dados precisamos armazenar os dados
    temperatura.append(temp2) #Foi gravada apenas a temperatura em Celsius por ser a unidade mais utilizada pelos usuários nacionais
    humidade.append(humid)
    pressao.append(press)

  #Mostar os dados, utilizao para debug. Também pode ser utilizado para apresentar a leitura atual na interface
    print(show)
    print("Temp: "+str(temp1)+" F")
    print("Temp: "+str(temp2)+" C")
    print("Humidity: "+str(humid)+" %")
    print("Pressure: "+str(press)+" hPa")
    print(" ")

  #Delay entre uma leitura e outra (20 segundos)
    time.sleep(20)

#Salvar os dados em uma planilha ao encerrar o programa, com a conexão em tempo real essa seção pode ser removida
with open('teste.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    field = ["temperatura (°C)", "humidade (%)", "pressao (hPa)"]
    writer.writerow(field)
    for j in range(0, 100):
        writer.writerow([temperatura[j], humidade[j], pressao[j]])
