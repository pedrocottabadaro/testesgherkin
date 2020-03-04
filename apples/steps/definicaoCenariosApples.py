from behave import *

use_step_matcher("re")


@given("there are (?P<start>.+) apples")
def step_impl(context, start):
    """
    :type context: behave.runner.Context
    :type start: str
    """
    raise NotImplementedError(u'STEP: Given there are <start> apples')


@when("I eat (?P<eat>.+) apples")
def step_impl(context, eat):
    """
    :type context: behave.runner.Context
    :type eat: str
    """
    raise NotImplementedError(u'STEP: When I eat <eat> apples')


@then("I should have (?P<left>.+) apples")
def step_impl(context, left):
    """
    :type context: behave.runner.Context
    :type left: str
    """
    raise NotImplementedError(u'STEP: Then I should have <left> apples')


@then('I should have (?P<left>.+) "apples"')
def step_impl(context, left):
    """
    :type context: behave.runner.Context
    :type left: str
    """
    raise NotImplementedError(u'STEP: Then I should have <left> "apples"')