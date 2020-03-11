from behave import *

from calculadora.operacoes import Calculator

use_step_matcher("re")



@given('"(?P<inicial>.+)" and "(?P<secundario>.+)"')
def step_impl(context, inicial, secundario):
    global c1
    c1=Calculator(inicial,secundario)
    print("operadores=")
    print(inicial)
    print(secundario)


@when('selected "(?P<operacao>.+)"')
def step_impl(context, operacao):
    c1.UsarOperacao(operacao)
    print("operacao=")
    print(operacao)


@then('result should be "(?P<resultado>.+)"')
def step_impl(context, resultado):
    resultado=float(resultado)
    print("resultado=")
    print(resultado)
    assert c1.resultado==resultado


