# Utilizando métodos decorados

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0 # Note o uso de somente um _ indicando atributo que
                        # deve ser manipulado apenas internamente

    # Utilizando o decorator @property, podemos proteger os atributos
    # e acessá-los somente por meio de métodos "decorados"
    @property   # definindo método decorado
    def saldo(self):
        return self._saldo
    
    # o decorador @setter força todas alterações de valor dos
    # atributos privados a passar por esses métodos

    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo inválido")
        else:
            self._saldo = saldo