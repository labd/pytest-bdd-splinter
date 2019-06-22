Feature: focus

    Scenario: Mouse over
        Given I am on "/animations"
        When I move my mouse to "Move mouse here"
        Then I should see "Content - 2"

    Scenario: Mouse over
        Given I am on "/animations"
        When I move my mouse to "Move mouse here"
        And I move my mouse to "button-with-id"
        Then I should not see "Content - 2"
