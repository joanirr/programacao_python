# Métodos de classe
# Servem para manipular os atributos de classe

class Circulo2:
    __totalCirculos = 0    # Atributo privado

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        type(self).__totalCirculos += 1  # incrementa o  contador

    # @classmethod criar o método de classe
    @classmethod
    def get_totalCirculos(cls):
        return cls.__totalCirculos
    
