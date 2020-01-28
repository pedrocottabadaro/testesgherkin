# Created by pedro at 1/28/2020
Feature: #Enter feature name here
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here
  
  
  Scenario Outline: deposit money to empty account
 Given a bank account with initial "<acao>" of "<valor>"
 When we "<acao>" an amount of "<valor>" into the account
 Then the "<acao>" of the account should be "<valor>"

   Examples:Variveis
      | valor | acao|
      |   0     |     deposit    |
      |   100    |    balance            |
      |   100    |    balance            |





