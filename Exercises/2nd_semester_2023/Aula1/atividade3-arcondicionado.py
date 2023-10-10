# Arcondicionado
class ArCondicionado:
    
    def __init__(self) :
        self.temperatura = 21
        self.ligado = False
    def ligar(self) :
        self.ligado = True
    def desligar(self) :
        self.ligado = False
    def aumentarTemperatura(self) :
        if self.ligado == False :
            self.ligar()
        self.temperatura += 1
        if self.temperatura >= 26 :
            self.temperatura = 26
    def diminuirTemperatura(self) :
        if self.ligado == False :
            self.ligar()
        self.temperatura -= 1
        if self.temperatura <= 16 :
            self.temperatura = 16
    def mostrarDados(self) :
        if self.ligado == False :
            print('Ar condicionado está desligado! ')
        else :
            print('Temperatura do ar condicionado: ', self.temperatura)
pass
# a partir daqui começa o programa principal

opcao = 0
arCondicionado = ArCondicionado()
arCondicionado.mostrarDados()

while True :
    print('Escolha uma opção: ')
    print('0 - Sair' )
    print('1 - Ligar ar condicionado ')
    print('2 - Desligar ar condicionado ')
    print('3 - Diminuir temperatura ')
    print('4 - Aumentar temperatura ')
    opcao = int(input('> '))
    if opcao == 0:
        break
    elif opcao == 1:
        arCondicionado.ligar()
    elif opcao == 2:
        arCondicionado.desligar()
    elif opcao == 3:
        arCondicionado.diminuirTemperatura()
    elif opcao == 4:
        arCondicionado.aumentarTemperatura()
    else :
        print('Opção invalida! Digite novamente! ')
    arCondicionado.mostrarDados()
Print('Obrigado por utilizar o nosso sistema! ')    

