from cliente import Cliente
from _thread import *
import socket


def inicializarCliente(socket):
    print("Cliente inicializado")
    cliente = Cliente(socket)
    while True:
        mensajeRecibido = socket.recv(1024)
        expresion = mensajeRecibido.decode("utf-8")
        resultado = ejecutar_calculo(expresion)

        cliente.enviarResultado(resultado)


def iniciarServidor():
    puerto = 3031
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("", puerto))
    sock.listen(100)
    print("Esperando conexiones")
    while True:
        cliente, direccionCliente = sock.accept()
        start_new_thread(inicializarCliente, (cliente, direccionCliente))
    sock.close()


def ejecutar_calculo(expresion):
    return eval(expresion)


iniciarServidor()
