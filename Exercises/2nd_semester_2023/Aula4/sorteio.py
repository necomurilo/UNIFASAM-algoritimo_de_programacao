lista = [5, 7, 3, 6]
pos = 2
for i in range(len(lista)-1, pos-1, -1):
    lista[i] = lista [i-1]
lista[pos-1]=8
print(lista)


# lista = [5, 7, 3, 6]
# lista.append(0)
# pos = 8
#     for i in range(len(lista)-1, pos-1, -1):
#     lista[i] = lista[i-1]
#     lista[pos] = 2
#     print(lista)

# lista = [5, 7, 3, 6]
# lista.count(0)
# pos = 8
#     for i in range(len(lista)-1, pos-1,-1):
#     lista[i] = 