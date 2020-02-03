# Created by pedro at 1/17/2020
Feature: Adicionar 2 numeros na calculadora
  # Enter feature description here

  Scenario Outline: Add
    Given "<inicial>" and "<secundario>"
    When selected "<operacao>"
    Then result should be "<resultado>"

    Examples:Variveis
      | inicial | secundario| resultado |operacao|
      |   9     |     30    |     39   |     +   |
      |   20    |      2    |      22  |    +     |
      |   60    |      0    |     60   |     +   |



  #Scenario: name
# Given [Initial context] And [some more context]
# When [Event] And [some other event]
# Then [Outcome] And [some other outcome]