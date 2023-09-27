# DAO
# Data Access Object
# Acesso aos dados dos Objeto
# Entidade (aquilo que quero representar no sist.)
# Aluno -> Entidade , Cao -> Entidade , Professor
# AlunoDao , CaoDao , ProfessorDao
# CRUD - Create (criar/inserir), Read (consulta/ler)
# Update (atualizar), Delete (apagar/excluir)

# Gerenciar uma agenda de contatos

# Definindo a minha classe contato (objeto de estudo)
class Contato:
  def __init__(self,nome,telefone):
    self.nome = nome
    self.telefone = telefone

# Melhorando o projeto
class ContatoDao:
  def __init__(self):
    self.agenda = []

  def inserir(self,contato):
    self.agenda.append(contato)

  def excluir(self,nome):
    for contato in self.agenda :
      if contato.nome == nome :
        print("Contato encontrado... Excluindo...")
        self.agenda.remove(contato)
        break

  def buscar(self,nome):
    for contato in self.agenda :
      if contato.nome == nome :
        print("Contato encontrado!")
        print("Nome: " , contato.nome)
        print("Telefone" , contato.telefone)
        print()

  def atualizar(self,nome):
    for contato in self.agenda :
      if contato.nome == nome :
        print("Contato encontrado!")
        contato.telefone = input("Favor informar o novo telefone:")

  def listarContatos(self):
    if len(self.agenda) > 0 :
    # len -> length (comprimento, quant. itens)
      print("\nListagem de contatos ------->")
      for contato in self.agenda :
        print("Nome: ",contato.nome)
        print("Telefone: ",contato.telefone)
        print()
      print("-------> Fim listagem contatos\n")

class View:
  def __init__(self):
    self.contatoDao = ContatoDao()

  def listarContatos(self):
    self.contatoDao.listarContatos()

  def inserirContato(self):
    print("Cadastrando novo contato:")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contato = Contato(nome,telefone)
    self.contatoDao.inserir(contato)

  def excluirContato(self):
    print("Excluindo contato...")
    nome = input("Informe o nome a excluir: ")
    self.contatoDao.excluir(nome)

  def buscarContato(self):
    print("Buscando contato...")
    nome = input("Informe o nome que deseja buscar:")
    self.contatoDao.buscar(nome)

  def atualizarContato(self):
    print("Operação atualizar...")
    nome = input("Informe o nome que deseja atualizar:")
    self.contatoDao.atualizar(nome)

  def mostrarMenu(self):
    opcao = int(input(" 0 - Finalizar \n 1 - Inserir \n 2 - Excluir \n 3 - Buscar \n 4 - Atualizar: "))
    return opcao

  def mostrarOpcaoInvalida(self):
    print("Opção Inválida!")

# Programa principal

# criar uma agenda vazia
#agenda = []
#contatoDao = ContatoDao()
view = View()

while True :
  #contatoDao.listarContatos()
  view.listarContatos()

  #opcao = int(input(" 0 - Finalizar \n 1 - Inserir \n 2 - Excluir \n 3 - Buscar \n 4 - Atualizar: "))
  opcao = view.mostrarMenu()
  if opcao == 0 :
    break
  elif opcao == 1:
    #print("Cadastrando novo contato:")
    #nome = input("Nome: ")
    #telefone = input("Telefone: ")
    #contato = Contato(nome,telefone)
    #contatoDao.inserir(contato)
    view.inserirContato()
  elif opcao == 2 :
    #print("Excluindo contato...")
    #nome = input("Informe o nome a excluir: ")
    #contatoDao.excluir(nome)
    view.excluirContato()
  elif opcao == 3 :
    #nome = input("Informe o nome que deseja buscar:")
    #contatoDao.buscar(nome)
    view.buscarContato()
  elif opcao == 4 :
    #print("Operação atualizar...")
    #nome = input("Informe o nome que deseja atualizar:")
    #contatoDao.atualizar(nome)
    view.atualizarContato()
  else :
    #print("Opção Inválida!")
    view.mostrarOpcaoInvalida()