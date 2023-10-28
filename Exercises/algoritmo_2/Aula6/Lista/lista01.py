lista = [0.0]
del lista[0]
while True :
  if len (lista) > 0 :
    print ("elementos da lista")
    for elemento in lista :
      print(elemento)
  else :
    print ("Lista está vazia!")
  opcao = float(input(" 1 - Inserir\n 2 - Remover\n 3 - Finalizar app\n -->"))
  if opcao == 1 :
    num = float(input("Informe o número a inserir:"))
    lista.append(num)
  elif opcao == 2 :
    num = float(input("Informe um número a excluir:"))
    try :
      lista.remove(num)
    except :
      print("Elemento inexistente!")
  elif opcao == 3 :
    break
  else :
    print("Opção inválida!")

print("Obrigado por usar nosso app")