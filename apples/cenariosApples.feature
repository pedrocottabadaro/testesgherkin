Feature: counting test

Scenario Outline: eating
  Given there are <start> apples
  When I eat <eat> apples
  Then I should have <left> apples

  Examples:
    | start | eat | left |
    |    12 |   5 |    7 |

