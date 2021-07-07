Feature: Login
    As someone who is not Mario
    I would like to try to login with Mario's account
    For finding out what he has been buying

  Scenario: Login fail
    Given the hacker is on the Login Page
    When the hacker tries to login with email "hackertpotato_test_com" and password "potato123"
    Then the hacker should not be able to login
