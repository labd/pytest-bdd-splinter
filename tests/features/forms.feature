Feature: Forms

    Scenario: Unchecked state
        Given I am on "/forms"
        When I press "checkbox1-2"
        Then the checkbox "checkbox1-1" is not checked
        And the checkbox "checkbox1-2" is checked

    Scenario: Radio button
        Given I am on "/forms"
        When I press "Radio 1"
        Then the radiobutton "radio1-1" is checked
        And the radiobutton "radio1-2" is not checked

    Scenario: Radio button in form 2
        Given I am on "/forms"
        When I press "Radio 2" in "form-2"
        Then the radiobutton "radio2-2" is checked
        But the radiobutton "radio1-1" is not checked
        But the radiobutton "radio1-2" is not checked
        But the radiobutton "radio2-1" is not checked

    Scenario: Type text in field simple
        Given I am on "/forms"
        When I enter "some new text" in the "prefilled" field
        Then the "prefilled" field should contain "some new text"

    Scenario: Type text in field alias
        Given I am on "/forms"
        When I type "foobar" in field "username"
        Then the "username" field should contain "foobar"

    Scenario: Type text in field alias 2
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

    Scenario: Slowly type text in field of form 2
        Given I am on "/forms"
        When I type "x" in the "username" field in "form-2" with 1 character per second
        Then the "username" field in "form-2" should contain "x"

    Scenario: Faster type text in field of form 2
        Given I am on "/forms"
        When I type "foobar" in the "username" field in "form-2" with 8 characters per second
        Then the "username" field in "form-2" should contain "foobar"

    Scenario: Multifield input
        Given I am on "/forms"
        When I fill in the following:
            | username | johndoe  |
            | password | mysecret |
        Then the "username" field should contain "johndoe"
        And the "password" field should contain "mysecret"

    Scenario: Multifield input in form 2
        Given I am on "/forms"
        When I fill in the following in "form-2":
            | username | johndoe  |
            | password | mysecret |
        Then the "username" field in "form-2" should contain "johndoe"
        And the "password" field in "form-2" should contain "mysecret"

    Scenario: Select item in dropdown
        Given I am on "/forms"
        When I select the option "Nederland" from "country"
        Then the option "NL" should be selected in "country"

    Scenario: Select item in dropdown of form 2
        Given I am on "/forms"
        When I select the option "Nederland" from "country" in form "form-2"
        Then the option "NL" should be selected in "country" in form "form-2"

    Scenario: Type text in field for specific form
        Given I am on "/forms"
        When I enter "foobar" in the "username" field in form "form-2"
        Then the "username" field in "form-2" should contain "foobar"
