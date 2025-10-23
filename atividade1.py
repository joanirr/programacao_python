for raiz in range (32, 100):
    num = raiz * raiz #calcula o número gerado pela raiz
    menor = num % 100 #obtém o número dos algarismos menos significativos
    maior = num // 100 #obtém o número dos algarismos mais significativos

    if (menor + maior) == raiz: #valida se a raiz corresponde a soma
        print (num)
        print(menor)
        print(maior)
        print(raiz)
print('terminou')
print('saiu ', raiz)

