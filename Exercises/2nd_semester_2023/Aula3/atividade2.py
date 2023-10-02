#Primeira parte
lista_a = [4,2,8,6,5]
lista_b = lista_a
lista_b[3] = 999
print(lista_a)
#Segunda parte
lista_a = [4,2,8,6,5]
lista_b = lista_a[:]
lista_b[3] = 999
print(lista_a)