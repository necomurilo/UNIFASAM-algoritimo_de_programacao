class Carro :

# definindo o construtor da classe
# construtor : o bloco de código que será executado no momento que eu declarar o uso da minha classe

  def __init__(self) :
    self.velocidade = 0
    self.marcha = 0
    self.andando = False

# Se o carro já está andando... aumente a velocidade em 10
# se o carro estiver parado, comece a andar
  def comecarAndar(self) :
    if self.andando == False :
      self.andando = True
      self.marcha = 1
      self.velocidade = 10
    else :
      self.velocidade = self.velocidade + 10
 
# Alterar todos os atributos do carro para definir o real estado de parado
  def parar(self) :
    self.velocidade = 0
    self.marcha = 0
    self.andando = False

# Aumentando a velocidade do carro, mas caso o carro esteja parado irei colocar ele em movimento.
  def acelerar(self) :
    if self.andando == False :
      self.comecarAndar()
    else :
      self.velocidade += 10

# Este metodo desacelera o carro em 10, mas caso o carro já esteja na velocidade mínima, então o carro para.
  def desacelerar(self) :
    if self.velocidade == 10 :
      self.parar()
    else :
      self.velocidade -= 10 
      # o comando acima equivale a ao mesmo commando self.velocidade = self.velocidade - 10

  def mostrarDados(self) :
    print('\nVelocidade: ', self.velocidade)
    print('\nMarchas: ', self.marcha)
    print('\nAndando: ', self.andando)
    # O comando \n salta uma linha

  def atualizarMarcha(self) :
    if self.velocidade == 0 :
      self.marcha = 0
    elif self.velocidade > 0 and self.velocidade < 20 :
      self.marcha = 1  
    elif self.velocidade >= 20 and self.velocidade < 40 :
      self.marcha = 2
    elif self.velocidade >= 40 and self.velocidade < 50 :
      self.marcha = 3
    elif self.velocidade >= 50 and self.velocidade < 60 :
      self.marcha = 4
    else :
      if self.velocidade >= 60 :
        self.marcha = 5
      

    if self.velocidade >= 180 :
      self.velocidade = 180
      print('\nVelocidade limite atingida!!!\n')

pass

# Início do meu programa principal
opcao = 0
carro = Carro()
carro.mostrarDados

while True :
  print('Escolha uma opção: ')
  print('0 - Sair ')
  print('1 - Começar a andar ')
  print('2 - Parar ')
  print('3 - Acelerar ')
  print('4 - Desacelerar ')
  opcao = int(input('>> '))
  if opcao == 0 :
    break
  elif opcao == 1 :
    carro.comecarAndar()
  elif opcao == 2 :
    carro.parar()
  elif opcao == 3 :
    carro.acelerar()
  elif opcao == 4 :
    carro.desacelerar()
  else :
    print('Opção inválidade, digite novamente\n')

  carro.atualizarMarcha()
  carro.mostrarDados()

# Fim do programa!