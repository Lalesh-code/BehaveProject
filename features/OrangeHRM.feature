Feature: OrangeHRM Logo
  Scenario: Logo presence on OrangeHRM home page
    Given Launch Chrome browser
    When open OrangeHRM home page
    Then verify that the logo is present on the page
    And close browser