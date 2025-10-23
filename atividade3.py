def maior_elemento(lista):
    # Caso base: se a lista tiver apenas um elemento, ele é o maior
    if len(lista) == 1:
        return lista[0]
    
    # Passo recursivo: compara o primeiro elemento com o maior do restante da lista
    maior_restante = maior_elemento(lista[1:])
    
    # Retorna o maior entre o primeiro e o maior do restante
    return lista[0] if lista[0] > maior_restante else maior_restante


# Exemplo de uso:
numeros = [5, 2, 9, 1, 7, 3]
print(maior_elemento(numeros))  # Saída