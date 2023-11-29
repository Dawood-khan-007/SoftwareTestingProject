Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to Home Page
    When I enter valid product "HP" into he search box field
    And I click on Search Button
    Then Valid product should get displayed in the search results
  @search
  Scenario: Search for invalid product
    Given I got navigated to Home Page
    When I enter invalid product "Honda" into the search box field
    And I click on Search Button
    Then Message should be displayed in Search Results
  @search
  Scenario: Search without entering anything
    Given I got navigated to Home Page
    When I enter nothing into he search box field
    And I click on Search Button
    Then Message should be displayed in Search Results
