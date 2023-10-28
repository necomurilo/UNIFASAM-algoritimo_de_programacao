# Gerador de números primos
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primos = [n for n in range(2, 1001) if eh_primo(n)]
print(primos)

#quantidade de numeros gerados

len(primos)