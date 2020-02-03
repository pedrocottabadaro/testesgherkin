# Created by pedro at 1/17/2020
Feature: Adicionar 2 numeros na calculadora
  # Enter feature description here

  Scenario Outline: Add
    Given bank account with <variavel>" and "<valor>"
    When select"<variavel>" with "<valor>"
    Then "<variavel>" should be "<valor>"

    Examples:Variveis
      | variavel    |    valor   |
      |   balance   |    0       |
      |   depositar |   500      |
      |    balance  |   500      |




