# Burlando atributos privados
# Python não possui atributos privados reais.
# Acesso pode ser obtido
from Conta import Conta

conta = Conta(1, 1000)
saldo1 = conta._Conta__saldo
print (saldo1)

#saldo2 = conta.saldo
#print (saldo2)