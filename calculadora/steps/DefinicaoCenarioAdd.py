from behave import *

from calculadora.operacoes import Calculator
c1=Calculator
use_step_matcher("re")



@given('"(?P<inicial>.+)" and "(?P<secundario>.+)"')
def step_impl(context, inicial, secundario):

    print(inicial)
    print(secundario)
    c1.inicia(c1,float(inicial),float(secundario))



@when('selected "(?P<operacao>.+)"')
def step_impl(context, operacao):
    print(operacao)
    c1.UsarOperacao(c1,operacao)



@then('result should be "(?P<resultado>.+)"')
def step_impl(context, resultado):
    print("resultado obtido= ")
    print(c1.resultado)
    print("resultado esperado=")
    print(resultado)


