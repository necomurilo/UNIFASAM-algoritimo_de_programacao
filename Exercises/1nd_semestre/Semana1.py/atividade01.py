for i in range(3):
  admissao= int(input('Por favor informe o ano de admissão: '))
  demissao= int(input('Por favor informe o ano de demissão: '))
  tempoServico= demissao - admissao
  print('Você trabalhou' , tempoServico, 'anos na empresa')