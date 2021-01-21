
import serial
import time
from ubidots import ApiClient

print("Programa inicializado")
api = ApiClient(token ='BBFF-cXDj05t6BmALXFBhbsGzJrfyE90c7w') #update token
patio = api.get_variable('6007acfe1d84725c2ae8d667') #update variable ID)
garaje = api.get_variable('6007b4d41d84726f8c3b2879')
cuarto = api.get_variable('6007ae481d84725e619ea1eb')

ser = serial.Serial('/dev/ttyS1', 9600,timeout=3.0) #update with port for Arduino
while True:
  if (ser.in_waiting>0):
    read_serial = ser.readline().strip()
    cond = read_serial.decode()
    tempReading1 = 0
    tempReading2 = 0
    tempReading3 = 0
    if(cond == 'Patio encendido'):
      tempReading1 = 1 #Patio encendido
      new_value = patio.save_value({'value': tempReading1})
    elif(cond == 'Patio apagado'):
      tempReading1 = 0 #Patio apagado
      new_value = patio.save_value({'value': tempReading1})
    elif(cond == 'Cuarto encendido'):
      tempReading2 = 1 #Cuarto encendido
      new_value2 = cuarto.save_value({'value': tempReading2})
    elif(cond == 'Cuarto apagado'):
      tempReading2 = 0 #Cuarto apagado
      new_value2 = cuarto.save_value({'value': tempReading2})
    elif(cond == 'Garage encendido'):
      tempReading3 = 1 #Garaje encendido
      new_value3 = garaje.save_value({'value': tempReading3})
    elif(cond == 'Garage apagado'):
      tempReading3 = 0 #Garaje apagado
      new_value3 = garaje.save_value({'value': tempReading3}) 
    
    

    print(read_serial) #prints serial reading to python

	#time.sleep(5)
