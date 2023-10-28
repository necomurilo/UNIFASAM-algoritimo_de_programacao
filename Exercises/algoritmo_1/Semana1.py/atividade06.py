produto1 = 0
produto2 = 0
produto3 = 0
produto4 = 0
produto =-1
while produto!=0:
  produto=int(input('Vote em um dos produtos 1,2,3 ou 4 (digite 0 para finalizar)'))
  if produto ==1:
    produto1 =produto1 +1
  if produto ==2:
    produto2 =produto2 +1
  if produto ==3:
    produto3 =produto3 +1
  if produto4 ==4:
    produto4 =produto4 +1
print('Votos para o produto 1: ', produto1)
print('Votos para o produto 2: ', produto2)
print('Votos para o produto 3: ', produto3)
print('Votos para o produto 4: ', produto4)