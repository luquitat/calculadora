import random
import socket
import sys
import threading
import tkinter as tk
from tkinter import ttk

PUERTO = 3031
SERVIDOR = "127.0.0.1"
DIRECCION = (SERVIDOR, PUERTO)
CHARSET = "utf-8"


# GUI class for the chat
class GUI:
    # constructor method

    def __init__(self):

        self.id = str(random.randint(1, 50000))

        self.Window = tk.Tk()
        self.Window.geometry('250x300')
        self.Window.title('Calculadora')

        self.Window.rowconfigure(0, weight=7)
        self.Window.rowconfigure(1, weight=3)
        self.Window.rowconfigure(2, weight=3)
        self.Window.rowconfigure(3, weight=3)
        self.Window.rowconfigure(4, weight=3)
        self.Window.rowconfigure(5, weight=3)

        self.Window.columnconfigure(0, weight=2)
        self.Window.columnconfigure(1, weight=2)
        self.Window.columnconfigure(2, weight=2)
        self.Window.columnconfigure(3, weight=7)

        self.expresion = ''
        self.entradaTexto = tk.StringVar()

        self.entradaG = ttk.Entry(self.Window, width=30, justify=tk.RIGHT,
                                  textvariable=self.entradaTexto, state=tk.DISABLED)
        self.entradaG.grid(row=0, columnspan=4, sticky='NSEW')

        self.botonPotencia = ttk.Button(self.Window, text='^', cursor='hand2',
                                        command=lambda: self._evento_click('^'))
        self.botonPotencia.grid(row=1, column=0, sticky='NSEW')
        self.botonPAbre = ttk.Button(self.Window, text='(', cursor='hand2',
                                     command=lambda: self._evento_click('('))
        self.botonPAbre.grid(row=1, column=1, sticky='NSEW')
        self.botonPCierra = ttk.Button(self.Window, text=')', cursor='hand2',
                                     command=lambda: self._evento_click(')'))
        self.botonPCierra.grid(row=1, column=2, sticky='NSEW')
        self.botonDivido = ttk.Button(self.Window, text='/', cursor='hand2',
                                     command=lambda: self._evento_click('/'))
        self.botonDivido.grid(row=1, column=3, sticky='NSEW')

        self.botonSiete = ttk.Button(self.Window, text='7', cursor='hand2',
                                     command=lambda: self._evento_click('7'))
        self.botonSiete.grid(row=2, column=0, sticky='NSWE')
        self.botonOcho = ttk.Button(self.Window, text='8', cursor='hand2',
                                     command=lambda: self._evento_click('8'))
        self.botonOcho.grid(row=2, column=1, sticky='NSWE')
        self.botonNueve = ttk.Button(self.Window, text='9', cursor='hand2',
                                     command=lambda: self._evento_click('9'))
        self.botonNueve.grid(row=2, column=2, sticky='NSWE')
        self.botonMultiplicacion = ttk.Button(self.Window, text='*', cursor='hand2',
                                     command=lambda: self._evento_click('*'))
        self.botonMultiplicacion.grid(row=2, column=3, sticky='NSWE')

        self.botonCuatro = ttk.Button(self.Window, text='4', cursor='hand2',
                                     command=lambda: self._evento_click('4'))
        self.botonCuatro.grid(row=3, column=0, sticky='NSWE')
        self.botonCinco = ttk.Button(self.Window, text='5', cursor='hand2',
                                     command=lambda: self._evento_click('5'))
        self.botonCinco.grid(row=3, column=1, sticky='NSWE')
        self.botonSeis = ttk.Button(self.Window, text='6', cursor='hand2',
                                     command=lambda: self._evento_click('6'))
        self.botonSeis.grid(row=3, column=2, sticky='NSWE')
        self.botonMenos = ttk.Button(self.Window, text='-', cursor='hand2',
                                     command=lambda: self._evento_click('-'))
        self.botonMenos.grid(row=3, column=3, sticky='NSWE')

        self.botonUno = ttk.Button(self.Window, text='1', cursor='hand2',
                                     command=lambda: self._evento_click('1'))
        self.botonUno.grid(row=4, column=0, sticky='NSWE')
        self.botonDos = ttk.Button(self.Window, text='2', cursor='hand2',
                                     command=lambda: self._evento_click('2'))
        self.botonDos.grid(row=4, column=1, sticky='NSWE')
        self.botonTres = ttk.Button(self.Window, text='3', cursor='hand2',
                                     command=lambda: self._evento_click('3'))
        self.botonTres.grid(row=4, column=2, sticky='NSWE')
        self.botonMas = ttk.Button(self.Window, text='+', cursor='hand2',
                                     command=lambda: self._evento_click('+'))
        self.botonMas.grid(row=4, column=3, sticky='NSWE')

        self.botonBorrar = ttk.Button(self.Window, text='C', command=self._evento_borrar)
        self.botonBorrar.grid(row=5, column=0, sticky='NSWE')
        self.botonCero = ttk.Button(self.Window, text='0', cursor='hand2',
                                     command=lambda: self._evento_click('0'))
        self.botonCero.grid(row=5, column=1, sticky='NSWE')
        self.botonPunto = ttk.Button(self.Window, text='.', cursor='hand2',
                                     command=lambda: self._evento_click('.'))
        self.botonPunto.grid(row=5, column=2, sticky='NSWE')
        self.botonIgual = ttk.Button(self.Window, text='=', cursor='hand2',
                                     command=self._evento_calcular)
        self.botonIgual.grid(row=5, column=3, sticky='NSWE')

    def _evento_borrar(self):
        self.expresion = ''
        self.entradaTexto.set(self.expresion)

    def _evento_click(self, elemento):
        self.expresion = f'{self.expresion}{elemento}'
        self.entradaTexto.set(self.expresion)

    def _evento_calcular(self):
        aux = self.expresion.replace('^', '**')
        resultado = str(eval(aux))
        self.expresion = ''
        self.entradaTexto.set(resultado)

    def conectar(self):
        self.Window.mainloop()
        # try:
        #     self.client = socket.socket(socket.AF_INET,
        #                                 socket.SOCK_STREAM)
        #     self.client.connect(DIRECCION)
        #     msg = str(self.id)
        #     self.client.send(msg.encode(CHARSET))
        #     # Iniciamos el thread
        #     rcv = threading.Thread(target=self.recibir)
        #     rcv.start()
        #     self.Window.mainloop()
        # except:
        #     print("No se encuentra cona conexión con el servidor")

    def enviar(self):
        msg = self.expresion
        while True:
            self.client.send(msg.encode(CHARSET))
            break

    def pantallaPrincipal(self, name):
        self.client = socket.socket(socket.AF_INET,
                                    socket.SOCK_STREAM)
        self.client.connect(DIRECCION)
        msg = "identificarme " + name
        self.client.send(msg.encode(CHARSET))
        # Iniciamos el thread
        rcv = threading.Thread(target=self.recibir)
        rcv.start()

    # Layout del la pantalla principal

    # Función del boton de enviar mensaje
    def sendButton(self, msg):
        self.boxComandos.config(state=DISABLED)
        self.msg = msg
        self.inputComandos.delete(0, END)
        snd = threading.Thread(target=self.enviarMensaje)
        snd.start()

    # Función del boton de salir
    def salir(self):
        self.Window.destroy()
        self.client.close()
        sys.exit()

    # Funcion que recibe el mensaje
    def recibir(self):
        while True:
            try:
                message = self.client.recv(1024).decode(CHARSET)
                print(message)
                # Magia pura
                if message == 'ID':
                    self.client.send(self.id.encode(CHARSET))
                else:
                    # agrego mensaje en el box
                    print(message)
            except:
                print("Oh no! Algo anduvo mal")
                self.client.close()
                break

    def enviarMensaje(self):
        # self.boxComandos.config(state=DISABLED)
        self.boxComandos.config(state=NORMAL)
        self.boxComandos.insert(END,
                                f"{self.name}: {self.msg}\n")

        self.boxComandos.config(state=DISABLED)
        self.boxComandos.see(END)
        while True:
            # message = (f"{self.name}: {self.msg}")

            self.client.send(self.msg.encode(CHARSET))
            break


g = GUI()

g.conectar()
