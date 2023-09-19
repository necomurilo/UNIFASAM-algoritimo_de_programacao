#from re import M
#valor = int(input("Digite um numero: "))

class UtilLerDados :
  def lerNumeroInteiro(self,mensagem) :
    while True :
      try : 
        dado = int(input(mensagem))
      except ValueError:
        print("Número inválido, informar novamente! ")
      else :
        break
    return dado

# Principal
utilLerDados = UtilLerDados()
numero  = utilLerDados.lerNumeroInteiro("Numeros: ")
print("Numero lido ", numero) 
