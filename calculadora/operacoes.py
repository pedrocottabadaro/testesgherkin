

class Calculator:
    numero1=0
    numero2=0
    resultado=0
    operacao=""
    def __init__(self,numero1,numero2):
        self.numero1=float(numero1)
        self.numero2=float(numero2)

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



