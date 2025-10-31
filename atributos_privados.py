# Como evitar a alteração indevida?
# Definindo atributos públicos e privados
# o uso de __ indica que um atributo é privado, ou seja,
# somente pode ser alterado por um método da classe

class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero        #atributo privado
        self.__saldo = saldo            #atributo privado
def main():
    conta = Conta(1, 1000)
    saldo = conta.saldo
    print(saldo)

if __name__ == "__main__":
    main()