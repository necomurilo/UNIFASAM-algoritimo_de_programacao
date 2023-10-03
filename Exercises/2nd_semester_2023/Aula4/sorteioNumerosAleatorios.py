import random # gera números aleatórios
numeros = []  # inicia uma lista vazia
while len(numeros) < 10: #permitir que seja sorteado 10 numeros
    numero = random.randint(1,1000) # gera um numero dentro do intervalo
    if numero not in numeros: # usa se o numero nao estiver na lista
        numeros.append(numero)
        print(sorted(numeros))