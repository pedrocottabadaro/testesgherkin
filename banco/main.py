class BankAccount:
    nome=""
    cpf=""
    email=""
    balance=0
    def __init__(self,nome,cpf,email,balance):
        self.nome=nome
        self.cpf=cpf
        self.email=email
        self.balance=balance
    def depositar(self,valor):
        self.balance+=valor

    def alterarBalance(self,valor):
        self.balance=valor

    def sacar(self,valor):
        self.balance-=valor

    def imprimirValorConta(self):
        print(self.balance)



