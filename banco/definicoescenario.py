from behave import *

use_step_matcher("re")


@given('a bank account with initial "(?P<acao>.+)" of "(?P<valor>.+)"')
def step_impl(context, acao, valor):
    """
    :type context: behave.runner.Context
    :type acao: str
    :type valor: str
    """
    raise NotImplementedError(u'STEP: Given a bank account with initial "<acao>" of "<valor>"')


@when('we "(?P<acao>.+)" an amount of "(?P<valor>.+)" into the account')
def step_impl(context, acao, valor):
    """
    :type context: behave.runner.Context
    :type acao: str
    :type valor: str
    """
    raise NotImplementedError(u'STEP: When we "<acao>" an amount of "<valor>" into the account')


@then('the "(?P<acao>.+)" of the account should be "(?P<valor>.+)"')
def step_impl(context, acao, valor):
    """
    :type context: behave.runner.Context
    :type acao: str
    :type valor: str
    """
    raise NotImplementedError(u'STEP: Then the "<acao>" of the account should be "<valor>"')