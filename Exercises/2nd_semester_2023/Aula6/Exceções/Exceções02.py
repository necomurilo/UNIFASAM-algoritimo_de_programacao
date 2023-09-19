class UtilLerDados :
 def lerNumeroDecimal(self,mensagem):
  while True :
   try :
    dado = float(input(mensagem))
   except ValueError:
    print("Número inválido, informar novamente!")
   else :
    break
  return dado

# Principal
utilLerDados = UtilLerDados()
numero = utilLerDados.lerNumeroDecimal("Numero:")
print("Numero lido ", numero)