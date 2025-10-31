# Método privado
# São indicados por um (_) ou dois underscores (__) no início do nome


class MinhaClasse:
    def __init__(self):
        self._atributo_privado = 42

    def _metodo_privado1(self):
        print("Este é um método privado.")

    def metodo_publico1(self):
        print("Este é um método público 1.")
        self._metodo_privado1()

    def __metodo_privado2(self):
        print("Este é um método fortemente privado.")

    def metodo_publico2(self):
        print("Este é um método público 2.")
        self.__metodo_privado2()

obj = MinhaClasse()
obj.metodo_publico1()

obj._metodo_privado1()

obj.metodo_publico2()

obj._MinhaClasse__metodo_privado2()


