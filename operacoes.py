def Adicionar(numero,numero2):

    return numero+numero2

def Subtrair(numero, numero2):
    return numero - numero2


def Dividir(numero, numero2):
    return numero / numero2


def Multiplicar(numero, numero2):
    return numero * numero


class Calculator:
    numero1=0
    numero2=0
    resultado=0
    operacao=""
    def AtribuirValorees(self,numero1,numero2):
        self.numero1=numero1
        self.numero2=numero2

    def UsarOperacao(self,operacao):
        self.operacao=operacao
        if operacao=="+":
            self.resultado= self.numero1+self.numero2
        elif operacao=="-":
            self.resultado= self.numero1-self.numero2
        elif operacao=="*":
            self.resultado= self.numero1*self.numero2
        elif operacao=="/":
            self.resultado= self.numero1/self.numero2

    def Limpar(self):
        self.numero1=0
        self.numero2=0
        self.resultado=0








