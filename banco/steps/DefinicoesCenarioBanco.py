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


@given('bank account with variavel" and "valor"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given bank account with variavel" and "valor"')


@when('select"variavel" with "valor"')
def step_impl(context):
    raise NotImplementedError(u'STEP: When select"variavel" with "valor"')


@then('"variavel" should be "valor"')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then "variavel" should be "valor"')