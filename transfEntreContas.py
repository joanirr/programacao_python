# Transferência entre contas
# Criamos um método para a transferência de valores
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def gerar_extrato(self):
        print(f"Número: {self.numero} \n CPF: {self.cpf} \n Saldo: {self.saldo}")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ("Transferência realizada!")
        

def main():
    conta1 = Conta(1, 123, 'João', 1000)
    conta2 = Conta(2, 456, 'Maria', 500)

    print('Saldo antes da transferência.')
    print(f"Saldo da conta 1: R${conta1.saldo}")
    print(f"Saldo da conta 2: R${conta2.saldo}")

    conta1.transfereValor(conta2, 300)
    print('Saldo após a transferência')
    print(f"Saldo da conta 1: R${conta1.saldo}")
    print(f"Saldo da conta 2: R${conta2.saldo}")


if __name__ == "__main__":
    main()
