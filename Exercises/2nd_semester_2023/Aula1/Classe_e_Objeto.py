""""
Classes e objetos
    Classe é a receita do bolo
        Começa sempre com letra maiuscula
    Objeto é o bolo


pass - é um marcador
construtor - definir os atributos na fabricação
"""

class Aluno:

    def __init__(self):
        print('Classe foi instanciada...')
        self.matricula = 0
        self.nome = ''
        valorMensalidade = 0.0
        self.p1 = 5.0
        self.p2 = 7.0
        self.media = 0.0

    def getMedia(self) :
        self.media = (self.p1 + self.p2) / 2
        return self.media


    pass

aluno = Aluno()
aluno.getMedia()