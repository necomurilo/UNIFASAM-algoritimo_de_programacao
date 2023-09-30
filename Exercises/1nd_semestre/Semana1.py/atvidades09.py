n = int(input('Informe um numero '))
ac=1
while True :
    ac= ac * n
n = n-1
if n < 1:
    break
print('Fatorial',ac)