from behave import *
from banco.main import BankAccount
b1=BankAccount("pe","1","@",3)

use_step_matcher("re")




@given('bank account with (?P<variavel>.+)" and "(?P<valor>.+)"')
def step_impl(context, variavel, valor):
   b1.alterarBalance(valor)

@then('"(?P<variavel>.+)" should be "(?P<valor>.+)"')
def step_impl(context, variavel, valor):
    b1.depositar(valor)

@when('select"(?P<variavel>.+)" with "(?P<valor>.+)"')
def step_impl(context, variavel, valor):
    b1.imprimirValorConta()
    print(valor)

