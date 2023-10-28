lista = [""]
del lista[0]
while True :
  if len (lista) > 0 :
    print ("elementos da lista")
    for elemento in lista :
      print(elemento)
  else :
    print ("Lista está vazia!")
  opcao = int(input(" 1 - Inserir\n 2 - Remover\n 3 - Finalizar app\n -->"))
  if opcao == 1 :
    while True :
      palavra = input("Informe o palavra a inserir (não):")
      if palavra == "não" :
        break
      lista.append(palavra)
  elif opcao == 2 :
    palavra = input("Informe um palavra a excluir:")
    try :
      lista.remove(palavra)
    except :
      print("Elemento inexistente!")
  elif opcao == 3 :
    break
  else :
    print("Opção inválida!")

print("Obrigado por usar nosso app")