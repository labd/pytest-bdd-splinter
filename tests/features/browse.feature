Feature: Browse

    Scenario: Test basic browse functionality
        Given I am on the homepage
        Then I should be on "/"
        And I should see "Index page"

    Scenario: Test deeplink to page
        Given I am on the homepage
        When I go to "/redirect/"
        Then I should be on "/subpage/"
        And I should see "Subpage only"

    Scenario: Test reload to page
        Given I am on "/subpage/"
        When I reload the page
        Then I should be on "/subpage/"

    Scenario: Test history back
        Given I am on the homepage
        When I go to "/subpage/"
        And I move backward one page
        Then I should be on "/"

    Scenario: Test history forward
        Given I am on the homepage
        When I go to "/subpage/"
        And I go to "/subpage/nested/"
        And I move backward one page
        And I move backward one page
        And I move forward one page
        Then I should be on "/subpage/"

    Scenario: Test press button with id
        Given I am on "/animations"
        When I do not see "Content - 1"
        And I press "button-with-id"
        Then I should see "Content - 1"

    Scenario: Test press button with text
        Given I am on "/animations"
        When I do not see "Content - 1"
        And I press "Show content - 1"
        Then I should see "Content - 1"

    Scenario: Test click on link with text
        Given I am on the homepage
        When I click on the link "go to subpage"
        Then I should be on "/subpage/"
