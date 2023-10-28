# Exercícios
# Utilizar para estudar para prova

class Avião: # a minha classe começa aqui
  # Construtor, código que será executado assim que o obj. da classe for criado
  # Início do código do construtor
  def __init__(self):
    self.voando = False
    self.altitude = 0
  # Fim do código do construtor

  # Método/Função decolar
  def Decolar(self) :
    if self.voando == False : #comparar com self.voando
      self.voando = True
      self.altitude = 100 
    else : 
      self.altitude = self.altitude + 100
      #self.altitude += 100 # faz a mesma coisa que a linha de cima

  # Método/Função aterrissar
  def Aterrisar(self) :
    self.voando = False
    self.altitude = 0

  def Subir(self) :
    if self.voando == False :
      self.Decolar()
    else :
      self.altitude += 100
   
  # Método/Função descer
  def Descer(self) :
    if self.altitude <= 100 :
      self.aterrissar ()
    else :
      self.altitude -= 100

  # Método/ Função para mostrar os dados do avião
  def MostrarDados(self) :
    print('\nVoando: ', self.voando)
    print('Altitude: ', self.altitude , '\n')


  pass # a minha classe finaliza aqui

# Daqui em diante começa o programa principal

#Declaração das variáveis/objetos
Opcao = 0
aviao = Avião()
aviao.MostrarDados()

# Menu para interação do usuário
while True :
  print('Escolha uma opção: ')
  print('0 - Fechar programa (sair) ')
  print('1 - Decolar' )
  print('2 - Aterrissar ')
  print('3 - Subir ')
  print('4 - Descer ')
  opcao = int(input('>> '))
  if opcao == 0 :
    break
  elif opcao == 1 :
    aviao.Decolar()
  elif opcao == 2 :
    aviao.Aterrisar()
  elif opcao == 3 :
    aviao.Subir()
  elif opcao == 4 :
    aviao.Descer()
  else : 
    print('\nOpção inválida !!!\n')
  aviao.MostrarDados()

# Fim do While e também fim do programa.
print('Obrigado por usar o nosso sistema! ')