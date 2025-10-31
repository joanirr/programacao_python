# Classe conta

from Contadec import Contadec
def main():
    conta = Contadec(1)
    conta.saldo = 1000  # usando o @saldo.setter
    print(f'Saldo da conta = {conta.saldo}')   # usando o @property


if __name__ == "__main__":
    main()