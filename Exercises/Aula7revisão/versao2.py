import sqlite3
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
    # deste ponto em diante e sqlite
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('CREATE TABLE IF NOT EXISTS contatos (id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT , telefone TEXT)')
    self.conexao.close()

  def sqliteInserir(self,contato):
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('INSERT INTO contatos (nome,telefone) VALUES (?,?)', (contato.nome,contato.telefone))
    self.conexao.commit()
    self.conexao.close()

  def sqliteBuscar(self,nome):
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('SELECT * FROM contatos WHERE nome=?',(nome,))
    self.conexao.commit()
    return self.cursor.fetchone()
    self.conexao.close()

  def sqliteListar(self):
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('SELECT nome,telefone FROM contatos')
    self.conexao.commit()
    return self.cursor.fetchall()
    self.conexao.close()
    

  def sqliteAtualizar(self,nome,novoTelefone):
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('UPDATE contatos SET telefone=? WHERE nome=?',(novoTelefone,nome))
    self.conexao.commit()
    self.conexao.close()

  def sqliteRemover(self,nome):
    self.conexao = sqlite3.connect("agenda.db")
    self.cursor = self.conexao.cursor()
    self.cursor.execute('DELETE FROM contatos WHERE nome=?',(nome,))
    self.conexao.commit()
    self.conexao.close()

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
    #self.contatoDao.listarContatos()
    contatos = self.contatoDao.sqliteListar()
    print(contatos)

  def inserirContato(self):
    print("Cadastrando novo contato:")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    contato = Contato(nome,telefone)
    #self.contatoDao.inserir(contato)
    self.contatoDao.sqliteInserir(contato)

  def excluirContato(self):
    print("Excluindo contato...")
    nome = input("Informe o nome a excluir: ")
    #self.contatoDao.excluir(nome)
    self.contatoDao.sqliteRemover(nome)

  def buscarContato(self):
    print("Buscando contato...")
    nome = input("Informe o nome que deseja buscar:")
    #self.contatoDao.buscar(nome)
    contato = self.contatoDao.sqliteBuscar(nome)
    print(contato)

  def atualizarContato(self):
    print("Operação atualizar...")
    nome = input("Informe o nome que deseja atualizar:")
    novoTelefone = input("Favor informar o novo telefone:")
    #self.contatoDao.atualizar(nome)
    self.contatoDao.sqliteAtualizar(nome,novoTelefone)

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
  view.listarContatos()

  opcao = view.mostrarMenu()
  if opcao == 0 :
    break
  elif opcao == 1:
    view.inserirContato()
  elif opcao == 2 :
    view.excluirContato()
  elif opcao == 3 :
    view.buscarContato()
  elif opcao == 4 :
    view.atualizarContato()
  else :
    view.mostrarOpcaoInvalida()