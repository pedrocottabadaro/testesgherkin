

from behave import *
from banco.main import BankAccount
b1 = BankAccount("pedro", "3", "ed", 0)
use_step_matcher("re")


@given('a bank account with initial "(?P<variavel>.+)" of "(?P<valor>.+)"')
def step_impl(context, variavel, valor):

   b1.alterarBalance(valor)


@when('we "(?P<metodo>.+)" an amount of "(?P<valor>.+)" into the account')
def step_impl(context, metodo, valor):

    b1.depositar(valor)



@then('the "(?P<variavel>.+)" of the account should be "(?P<valor>.+)"')
def step_impl(context, variavel, valor):

    b1.imprimirValorConta()