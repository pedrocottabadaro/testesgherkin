class Aluno:
    nome=""
    media=0

    def __init__(self, nome, nota1, nota2, nota3):

        self.nome=nome
        self.media=float((float(nota1)+float(nota2)+float(nota3))/3)

    def verifica(self):
        if(self.media>60):
            print("aluno aprovado")
        else:
            print("recuperacao")