Feature: OrangeHRM Login

  Scenario: Login to OrangeHRM with valid login parameter
    Given I launch a Chrome browser
    When I open a OrangeHRM home page
    And enter a Username "Admin" and Password "admin123"
    And click on the login button
    Then User must successfully login to Dashboard page

  Scenario Outline: Login to OrangeHRM with multiple parameter
    Given I launch a Chrome browser
    When I open a OrangeHRM home page
    And enter a Username "<UserName>" and Password "<Password>"
    And click on the login button
    Then User must successfully login to Dashboard page

    Examples:
    | UserName | Password |
    | admin    | admin123 |
    | admin123 | admin    |
    | adminxyz | admin123 |
    | admin    | adminxyz |
