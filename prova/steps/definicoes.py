from behave import *

from prova.main import Aluno

use_step_matcher("re")


@given("a (?P<student>.+) with (?P<nota>.+),(?P<nota1>.+) e(?P<nota2>.+)")
def step_impl(context, student, nota, nota1, nota2):
    global aluno
    aluno=Aluno(student,nota,nota1,nota2)


@when("I (?P<action>.+)")
def step_impl(context, action):
    aluno.verifica()


@then("result should be (?P<result>.+)")
def step_impl(context, result):
    print("media=")
    print(aluno.media)
    assert aluno.media