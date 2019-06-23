# Examples
```gherkin
Scenario: Move the mouse to a div to trigger a javascript event
    Given I am on "/animations"
    When I move my mouse to "Move mouse here"
    And I move my mouse to "button-with-id"
    Then I should not see "Content - 2"
```
```gherkin
Scenario: fill multiple form fields in one step
    Given I am on "/forms"
    When I fill in the following:
        | username | johndoe  |
        | password | mysecret |
    And I type in field "first_name" the value "Foo"
    Then the "username" field should contain "johndoe"
    And the "password" field should contain "mysecret"
```

```gherkin
Scenario: Setting a radio button and checking the state
    Given I am on "/forms"
    When I press "Radio 1"
    Then the radiobutton "radio-1" is checked
    And the radiobutton "radio-2" is not checked
```

## Screen resolutions
Using a `Scenario Outline` in combination with screen resolutions
is helpful when testing multiple browser states. By default
the resolutions are used for which [Bootstrap 4 defines media queries](https://getbootstrap.com/docs/4.3/layout/overview/#responsive-breakpoints).
See the [pytest bdd documentation](https://pytest-bdd.readthedocs.io/en/latest/#scenario-outlines)
for more information.
```gherkin
Scenario Outline: Show index extra small
    Given I am using a <device>
    And I am on the homepage
    Then I should be on "/"
    And I should see "Index page"

Examples:
| device             |
| extra small device |
| small device       |
| medium device      |
| large device       |
| extra large device |
```
