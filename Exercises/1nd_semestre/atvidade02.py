for i in range(10):
  dolares= float(input('Por favor informe o valor do produto em dolares: '))
  reais= dolares *4.90
  if reais >= 3000:
    reais = reais*1.6
  print(f'Valor a pagar: R${reais:,.2f}')