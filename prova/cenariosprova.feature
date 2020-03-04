# Created by Pedro at 2/11/2020

Feature: Aprovacao aluno
  # Enter feature description here

      Scenario Outline: some scenario
        Given a <student> with <nota>,<nota1> e<nota2>
        When I <action> 
        Then result should be <result>
      Examples:

        |student|nota|nota1|nota2|result|action|
        |  pedro|    10 |30|40   |aprovado|verifica|

