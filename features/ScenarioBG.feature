Feature: OrangeHRM Login

  Background: common steps
    Given Open a Chrome browser
    When Hit OrangeHRM home page
    And Put a Username and Password
    And Hit the login button

  Scenario: Login to OrangeHRM with valid login parameter
    Then User able to successfully login to Dashboard page

  Scenario: Search User
    When navigate to Search page
    Then Search page should be displayed

  Scenario: Advance Search User
    When navigate to Advance Search page
    Then Advanced Search page should be displayed