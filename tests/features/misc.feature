Feature: Misc

    Scenario: Test wait for less then 1 second
        Given I am on the homepage
        When I wait for 0.1 seconds
        Then I should see "Index page"

    Scenario: Test wait for less 1 second
        Given I am on the homepage
        When I wait for 1 second
        Then I should see "Index page"
