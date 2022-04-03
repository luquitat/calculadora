
class Cliente:

    id = None

    def __init__(self, socket):
        self.id = None
        self.socket = socket

    def establecerId(self, id):
        self.id = id

    def enviarResultado(self, resultado):
        self.socket.send(str(resultado).encode())

    def estaIdentificado(self):
        return self.id is not None
