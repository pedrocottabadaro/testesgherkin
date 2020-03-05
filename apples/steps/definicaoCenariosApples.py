from behave import *
from main import Apples

use_step_matcher("re")


@given("there are (?P<start>.+) apples")
def step_impl(context, start):

    #apples=Apples(start)

@when("I eat (?P<eat>.+) apples")
def step_impl(context, eat):
    #apples.eat(eat)


@then("I should have (?P<left>.+) apples")
def step_impl(context, left):
    #print(apples.apples)
    #print(left)


def eating():
    apples=Apples(12)
    apples.eat(5)


####PAGINA 30 SUNIL