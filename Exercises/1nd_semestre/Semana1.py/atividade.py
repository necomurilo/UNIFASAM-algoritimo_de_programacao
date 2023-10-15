#atividade slide
#está linha foi adicionada no linux
#refazer exercicios
bezerroMleve=9999999
for i in range(10):
  bezerro = int(input('Informe o peso do bezerro: '))
  if bezerro < bezerroMleve:
    bezerroMleve = bezerro
print('O bezerro mais leve pesa: ', bezerroMleve)