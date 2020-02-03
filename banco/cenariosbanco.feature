# Created by pedro at 1/28/2020
Feature: Alterando balanca banco


  Scenario Outline: Depositar
    Given a bank account with initial "<variavel>" of "<valor>"
    When we "<metodo>" an amount of "<valor>" into the account
    Then the "<variavel>" of the account should be "<valor>"
    Examples:

   Examples:Variveis
      | valor | metodo   | variavel |
      |   0   | deposit  |  balance |
      |   500 |          |  balance |
      |   500 |          |          |






