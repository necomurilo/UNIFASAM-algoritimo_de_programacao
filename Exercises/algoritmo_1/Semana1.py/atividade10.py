soma = 0.0
while True :
    produto = float(input('Valor do produto ou 0:'))
    if produto == 0 :
        break
soma = soma + produto
print('Sub-total é ', soma)
print('O total da compra é ' , soma)