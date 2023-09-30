soma = 0.0
while True :
   produto= float(input('Informe o valor de um produto ou 0 para finalizar o programa '))
   if produto == 0 :
     break
   quantidade= float(input('Informe a qualidade ou 0 para finalizar o programa '))
   if quantidade == 0 :
      break
   soma = soma + (produto * quantidade)
print(f'Soma dos produtos R${soma:,.2f}')