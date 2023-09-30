soma = 0.0
while True:
  produto = float(input('informe o valor de um produto, 0 para finalizar o programa: '))
  if produto == 0 :
    break
  soma= soma +produto
print(f'Soma dos produtos R${soma:,.2f}')