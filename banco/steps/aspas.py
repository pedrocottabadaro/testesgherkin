from behave import *

use_step_matcher("re")




@then('the result page will include "success"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Then the result page will include "success"')


@given('I search for a valid "book"')
def step_impl(context):

    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I search for a valid "book"')


@given("I search for a valid <book>")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I search for a valid <book>')


@given("I search \[for\] a valid \{book\}")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I search [for] a valid {book}')


@given('I search \[for\] a valid "\{book\}"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: Given I search [for] a valid "{book}"')


@when('i click "enter"')
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    raise NotImplementedError(u'STEP: When i click "enter"')