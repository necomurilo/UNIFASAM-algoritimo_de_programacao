canal1=0
canal2=0
canal3=0
for i in range(10):
  canal= int(input('Vote em um dos canais 1, 2 ou 3: '))
  if canal ==1:
    canal1= canal1 +1
  if canal ==2:
    canal2= canal2 +1
  if canal3 ==3:
    canal3= canal3+3
print('Votos para canal 1:', canal1)
print('Votos para canal 2:', canal2)
print('Votos para canal 3:', canal3)