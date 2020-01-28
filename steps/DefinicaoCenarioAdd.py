from behave import *

import operacoes
from operacoes import Calculator
c1=Calculator
use_step_matcher("re")



@given('"(?P<inicial>.+)" and "(?P<secundario>.+)"')
def step_impl(context, inicial, secundario):
    c1.AtribuirValorees(float(inicial),float(secundario))


@when('selected "(?P<operacao>.+)"')
def step_impl(context, operacao):

    c1.UsarOperacao(operacao)


@then('result should be "(?P<resultado>.+)"')
def step_impl(context, resultado):

    print(resultado)
