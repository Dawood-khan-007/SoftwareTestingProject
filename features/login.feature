Feature: Login functionality
  @login
  Scenario Outline: login with valid credentials
    Given I navigate to login page
    When I enter valid email as "<email>" and password as "<password>" in the fields
    And I press on login button
    Then I should get Logged in
    Examples:
    |email                    |password     |
    |khanahhmad002@gmail.com  |12345        |
    |dawood123@gmail.com      |123456       |

  @login
  Scenario: login with invalid email and valid password
    Given I navigate to login page
    When I enter invalid email and valid password "12345" in the fields
    And I press on login button
    Then Warning Message should be displayed
  @login
  Scenario: login with valid email and invalid password
    Given I navigate to login page
    When I enter valid email "khanahhmad002@gmail.com" and invalid password "1234543577" in the fields
    And I press on login button
    Then Warning Message should be displayed
  @login
  Scenario: login with invalid credentials
    Given I navigate to login page
    When I enter invalid email and invalid password "1234543577" in the fields
    And I press on login button
    Then Warning Message should be displayed
  @login
  Scenario: login with blank credentials
    Given I navigate to login page
    When I enter nothing in the fields
    And I press on login button
    Then Warning Message should be displayed


