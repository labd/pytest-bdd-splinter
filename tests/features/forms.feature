Feature: Forms

    Scenario: Unchecked state
        Given I am on "/forms"
        When I press "checkbox-2"
        Then the checkbox "checkbox-1" is not checked
        And the checkbox "checkbox-2" is checked

    Scenario: Radio button
        Given I am on "/forms"
        When I press "Radio 1"
        Then the radiobutton "radio-1" is checked
        And the radiobutton "radio-2" is not checked

    Scenario: Type text in field
        Given I am on "/forms"
        When I enter "foobar" in the "username" field
        Then the "username" field should contain "foobar"

    Scenario: Type text in field alias
        Given I am on "/forms"
        When I type "foobar" in field "username"
        Then the "username" field should contain "foobar"

    Scenario: Type text in field
        Given I am on "/forms"
        When I type in field "username" the value "foobar"
        Then the "username" field should contain "foobar"

    Scenario: Slowly type text in field
        Given I am on "/forms"
        When I type in field "username" the value "x" with 1 character per second
        Then the "username" field should contain "x"

    Scenario: Faster type text in field
        Given I am on "/forms"
        When I type in field "username" the value "foobar" with 8 characters per second
        Then the "username" field should contain "foobar"

    Scenario: Faster type text in field alias
        Given I am on "/forms"
        When I type "foobar" in field "username" with 8 characters per second
        Then the "username" field should contain "foobar"

    Scenario: Multifield input
        Given I am on "/forms"
        When I fill in the following:
            | username | johndoe  |
            | password | mysecret |
        Then the "username" field should contain "johndoe"
        And the "password" field should contain "mysecret"
