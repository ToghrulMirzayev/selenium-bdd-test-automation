Feature: Login functionality

Scenario: User logs in with valid credentials
    Given the user is on the login page
    When the user enters valid username and password
    And clicks on the login button
    Then the user should see title text

Scenario: User logs in with invalid credentials
    Given the user is on the login page
    When the user enters invalid username and password
    And clicks on the login button
    Then the user should see an error message
