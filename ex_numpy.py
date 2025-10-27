# Utilizando o numpy para calcular raízes
# importando o numpy
import numpy as np

# Função para calcular as raízes da equação de segundo grau
def calcular_raizes(a, b, c):
    # Coeficientes da equação
    coeficientes = [a, b, c]

    # Usando numpy.roots para calcular as raízes
    raizes = np.roots(coeficientes)
    return raizes
# Solicitando os coeficientes ao usuário
a = float(input("Digite o coeficiente a: "))
b = float(input("Digite o coeficiente b: "))
c = float(input("Digite o coeficiente c: "))

# Calculando as raízes
raizes = calcular_raizes(a, b, c)

# imprimindo os resultados
print(f"As raízes da equação são: {raizes[0]} e {raizes[1]}.")
