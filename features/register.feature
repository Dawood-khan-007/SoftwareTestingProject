Feature: Register Account Functionality
  @register @run
  Scenario: Register With Mandatory fields
    Given I navigate to register page
    When I Enter Mandatory fields
         |first_name|last_name|telephone|password|
         |dawood    |khan     |2311647  |12345   |
    And I select privacy policy option
    And I press on Continue button
    Then Account should be created

  @register
  Scenario: Register With All fields
    Given I navigate to register page
    When I Enter details in All fields
         |first_name|last_name|telephone|password|
         |dawood    |khan     |2311647  |12345   |
    And I select privacy policy option
    And I press on Continue button
    Then Account should be created

  @register
  Scenario: Register With duplicate email
    Given I navigate to register page
    When I Enter details in All fields except email field
         |first_name|last_name|telephone|password|
         |dawood    |khan     |2311647  |12345   |
    And I enter already registered email in email field
    And I select privacy policy option
    And I press on Continue button
    Then Proper Warning message should be displayed about duplicate email

  @register
  Scenario: Register With empty fields
    Given I navigate to register page
    When I write nothing in the fields
    And I press on Continue button
    Then Warning message should be displayed in every mandatory field

