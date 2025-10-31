# Métodos estáticos podem ser chamados sem uma
# referência a um objeto da classe
class MinhaClasse:
    @staticmethod  # Definindo método estático
    def metodo_estatico(x, y):
        return x + y

# Usando o método estático
resultado = MinhaClasse.metodo_estatico(3, 5)
print(resultado)   # Saída: 8

# Note que você não precisa criar uma instância da classe
# para usar o método estático
obj = MinhaClasse()
resultado = obj.metodo_estatico(10, 20)
print(resultado)    # Saída: 30