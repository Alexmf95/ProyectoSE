################################
##Generated with a lot of love##
##    with   EasyPython       ##
##Web site: easycoding.tn     ##
################################
import serial
import time

from http.server import BaseHTTPRequestHandler, HTTPServer

atmega = serial.Serial('/dev/ttyS1',9600)   #para raspberry '/dev/ttyS0'
print("\nConectado por serial")

Request = None

class RequestHandler_httpd(BaseHTTPRequestHandler):
  def do_GET(self):
    global Request
    messagetosend = bytes('Solicitando conexion',"utf")
    self.send_response(200)
    self.send_header('Content-Type', 'text/plain')
    self.send_header('Content-Length', len(messagetosend))
    self.end_headers()
    self.wfile.write(messagetosend)
    Request = self.requestline
    Request = Request[5 : int(len(Request)-9)]
    
    
    #print(Request)
    if Request == 'on1':
      comando = "A"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode())      
      print('\nEl patio ahora se encuentra encendido\n')      
    if Request == 'off1':
      comando = "B"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode())  
      print('\nEl patio ahora se encuentra apagado\n')
    if Request == 'on2':
      comando = "C"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode()) 
      print('\nEl cuarto ahora se encuentra encendido\n')
    if Request == 'off2':
      comando = "D"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode()) 
      print('\nEl cuarto ahora se encuentra apagado\n')
    if Request == 'on3':
      comando = "E"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode()) 
      print('\nEl garaje ahora se encuentra encendido\n')
    if Request == 'off3':
      comando = "F"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode()) 
      print('\nEl garaje ahora se encuentra apagado\n')
    if (Request == 'navidad'):
      comando = "N"
      atmega.write(comando.encode())
      atmega.write('\r\n'.encode()) 
      print('FELIZ NAVIDAD!!!')
    return


server_address_httpd = ('192.168.1.16',8080)
httpd = HTTPServer(server_address_httpd, RequestHandler_httpd)
print('\nConexion al servidor exitosa\n\n')
httpd.serve_forever()
