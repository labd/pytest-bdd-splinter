Feature: Small device
    Background:
        Given I am using a small device

    Scenario: Show index
        Given I am on the homepage
        Then I should be on "/"
        And I should see "Index page"

    Scenario: Test deeplink to page
        Given I am on the homepage
        When I go to "/redirect/"
        Then I should be on "/subpage/"
        And I should see "Subpage only"
