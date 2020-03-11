from behave import *
from main import Apples

use_step_matcher("re")


@given("there are (?P<start>.+) apples")
def step_impl(context, start):
    global apples
    apples=Apples(start)

@when("I eat (?P<eat>.+) apples")
def step_impl(context, eat):
    apples.eat(eat)


@then("I should have (?P<left>.+) apples")
def step_impl(context, left):
    left=int(left)
    assert apples.apples==left




####PAGINA 30 SUNIL