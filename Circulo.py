# Atributo de classe
# Usado para controlar valores associados à classe, e não aos objetos

class Circulo:
    totalCirculos = 0   # Atributo da classe fora do init

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo.totalCirculos += 1
