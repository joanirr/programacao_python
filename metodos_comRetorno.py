# Métodos com retorno
# serve para validar o estado de um objeto
class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:      # Valida se existe saldo para o saque
            return False
        else:
            self.saldo -= valor
            return True
        
    def gerar_extrato(self):
        print(f"Número: {self.numero} \n CPF: {self.cpf} \n Saldo: {self.saldo}")

def main():
    conta1 = Conta(1, 123, 'João', 1000)

    valor_saque = 200
    resultado_saque = conta1.sacar(valor_saque)

    # Validando o retorno para verificar se o saque foi realizado
    if resultado_saque:
        print(f"Saque de R${valor_saque} realizado com sucesso!")
        print(f"saldo atual: R${conta1.saldo}")
    else:
        print("Saldo insuficiente para realizar o saque.")

if __name__ == "__main__":
    main()