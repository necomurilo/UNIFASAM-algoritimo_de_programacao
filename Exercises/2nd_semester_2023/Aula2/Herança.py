"""
Poder de reaproveitar códigos;
Definimos uma classe filha que herda dados da superclasse;
"""
class Conta :
  def __init__(self) :
    self.nomeBanco = ''
    self.agencia = 0
    self.numeroConta = 0
    self.nomeCliente = ''
    self.saldo = 0.0

  def depositar(self,valorDeposito) :
    self.saldo = self.saldo + valorDeposito

  def sacar(self,valorSaque) :
    if valorSaque > self.saldo :
      print('Saldo insuficiente para saque!')
    else :
      self.saldo = self.saldo - valorSaque
      print('Saque realizado com sucesso!')

  def mostrarDadosConta(self) :
    print('\nNome banco: ' , self.nomeBanco)
    print('Agencia: ' , self.agencia)
    print('Número conta: ' , self.numeroConta)
    print('Nome cliente: ' , self.nomeCliente)
    print('Saldo :' , self.saldo)

  pass

class ContaPoupanca(Conta) :
  def __init__(self) :
    super().__init__()
    self.diaAniversario = 0
    self.taxaRendimento = 0.01

  def aplicarRendimento(self) :
    self.saldo = self.saldo + self.saldo * self.taxaRendimento

  def mostrarDadosConta(self) :
    super().mostrarDadosConta()
    print('Dia Aniverário: ', self.diaAniversario)
    print('Taxa Rendimento: ' , self.taxaRendimento , '\n')

  pass

class ContaEspecial(Conta) :
  def __init__(self) :
    super().__init__()
    self.valorLimite = 1000.0

  def sacar(self,valorSaque) :
    if valorSaque > self.saldo + self.valorLimite:
      print('Saldo insuficiente para saque!')
    else :
      self.saldo = self.saldo - valorSaque
      print('Saque realizado com sucesso!')

  pass

conta = Conta()
contaPoupanca = ContaPoupanca()
contaEspecial = ContaEspecial()

while True :
  print('Escolha o tipo de conta a usar: ')
  print('1 - Conta corrente')
  print('2 - Conta poupança')
  print('3 - Conta especial')
  tipoConta = int(input('> '))
  if tipoConta == 1 :
    print('Conta corrente selecionada!')
    break
  elif tipoConta == 2 :
    print('Conta poupança selecionada!')
    break
  elif tipoConta == 3 :
    print('Conta especial selecionada!')
    break
  else :
    print('Opção inválida! Digite novamente!')

opcao = 0
while True :
  print('0 - Finaliza o programa')
  if tipoConta == 1 :
    # início tratar opcões da conta corrente
    print('Conta corrente...')
    print('1 - Sacar \n2 - Depositar')
    opcao = int(input('> '))
    if opcao == 1 :
      valorSaque = float(input('Valor saque:'))
      conta.sacar(valorSaque)
    elif opcao == 2 :
      valorDeposito = float(input('Valor deposito:'))
      conta.depositar(valorDeposito)
    else :
      print('Opção Inválida!')
    conta.mostrarDadosConta()
    # fim tratar opcões da conta corrente
  elif tipoConta == 2 :
    # início tratar opcões da conta poupança
    print('Conta poupança...')
    print('1 - Sacar \n2 - Depositar \n3 - Rendimento')
    opcao = int(input('> '))
    if opcao == 1 :
      valorSaque = float(input('Valor saque:'))
      contaPoupanca.sacar(valorSaque)
    elif opcao == 2 :
      valorDeposito = float(input('Valor deposito:'))
      contaPoupanca.depositar(valorDeposito)
    elif opcao == 3 :
      contaPoupanca.aplicarRendimento()
    else :
      print('Opção Inválida!')
    contaPoupanca.mostrarDadosConta()
    # fim tratar opcões da conta poupança
  else :
    # início tratar opcões da conta especial
    print('Conta especial')
    print('1 - Sacar \n2 - Depositar')
    opcao = int(input('> '))
    if opcao == 1 :
      valorSaque = float(input('Valor saque:'))
      contaEspecial.sacar(valorSaque)
    elif opcao == 2 :
      valorDeposito = float(input('Valor deposito:'))
      contaEspecial.depositar(valorDeposito)
    else :
      print('Opção Inválida!')
    conta.mostrarDadosConta()
    # fim tratar opcões da conta especial
  if opcao == 0 :
      break





