boiMaisPesado=-1
for i in range(10):
  boi=int(input('Qual o peso do boi? '))
  if boi >boiMaisPesado:
    boiMaisPesado=boi
print('O boi que mais pesa', boiMaisPesado)