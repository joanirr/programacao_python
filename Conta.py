import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, clientes, numero, saldo=0.0):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.dataabertura = datetime.datetime.today()
        self.extrato = Extrato()  # ✅ agora a conta tem um extrato próprio

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPÓSITO", valor, "Conta", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente!")
            return False
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Conta", datetime.datetime.today()])
            return True

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            print("Não existe saldo suficiente")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERÊNCIA", valor, "Conta", datetime.datetime.today()])
            print("Transferência realizada com sucesso!")

    def gerarsaldo(self):
        print(f"Conta número: {self.numero} | Saldo: R$ {self.saldo:.2f}")
