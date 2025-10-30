# Métodos de classes
# Definem as ações que o objeto pode realizar
class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def depositar(self, valor):
    self.saldo += valor

def sacar(self, valor):
    self.saldo -= valor

def gerar_extrato(self):
    print(f"Número: {self.numero} \n CPF: {self.cpf} \n Saldo: {self.saldo}")


    def main():
        c1 = Conta(1, 1, "João", 0)
        c1.depositar(300)   # Chamando o método depositar para c1
        c1.gerar_extrato()  # Chamando o método gerar extrato para c1
        c1.sacar(100)       # Chamando o método sacar para c1
        c1.gerar_extrato()  # Chamando no método gerar extrato para c1


        if __name__ == "__main__":
            main()