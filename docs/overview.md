# All steps

Most of these steps should be self explanatory. On the [examples
page](examples.md) you can see more information about the steps.

All form elements can be targeted using their "name" or "id" field.
The select options can be targeted using their "value" or "text" field.

## Given
- `#!gherkin Given I am on the homepage`
- `#!gherkin Given I am on "<path>"`
- `#!gherkin Given I am using a <device>`
- `#!gherkin Given I am using a window size of <height>x<width>`
- `#!gherkin Given I am using an extra small device`
- `#!gherkin Given I am using a small device`
- `#!gherkin Given I am using a medium device`
- `#!gherkin Given I am using a large small device`
- `#!gherkin Given I am using an extra large device`

## When
- `#!gherkin When I go to the homepage`
- `#!gherkin When I go to "<path>"`
- `#!gherkin When I reload the page`
- `#!gherkin When I move backward one page`
- `#!gherkin When I move forward one page`
- `#!gherkin When I move my mouse to "<element-id>"`
- `#!gherkin When I click on the link "<text>"`
- `#!gherkin When I wait for 1 second`
- `#!gherkin When I wait for <number> seconds`
- `#!gherkin When I wait for <decimal> seconds`
- `#!gherkin When I wait for <number> milliseconds`
- `#!gherkin When I press "<button-with-id/title/text>"`
- `#!gherkin When I press "<button-with-id/title/text>" in "<element-name/id>"`
- `#!gherkin When I enter "<value>" in the "<field-name>" field"`
- `#!gherkin When I enter "<value>" in the "<field-name>" field in form "<form-name>"`
- `#!gherkin When I type in field "<field-name>" the value "<value>"`
- `#!gherkin When I type "<value>" in field "<field-name>"`
- `#!gherkin When I type "<value>" in field "<field-name>" in "<form-name>"`
- `#!gherkin When I type in field "<field-name>" the value "<value>" with <number> characters per second`
- `#!gherkin When I type "<value>" in field "<field-name>" with <number> characters per second"`
- `#!gherkin When I type "<value>" in field "<field-name>" in "<form-name>" with <number> characters per second"`
- `#!gherkin When I fill in the following:` (multi-line, see examples)
- `#!gherkin When I fill in the following in "<form>":` (multi-line, see examples)
- `#!gherkin When I select the option "<value>" from "<field-name>"`
- `#!gherkin When I select the option "<value>" from "<field-name>" in "<form-name>"`

## Then
- `#!gherkin Then I print the current url`
- `#!gherkin Then I should be on "/path/"`
- `#!gherkin Then I should see "Content - 1"`
- `#!gherkin Then the checkbox "checkbox-1" is checked`
- `#!gherkin Then the checkbox "checkbox-1" is not checked`
- `#!gherkin Then the radiobutton "radio-1" is checked`
- `#!gherkin Then the radiobutton "radio-2" is not checked`
- `#!gherkin Then the "<field>" field should contain "<value>"`
- `#!gherkin Then the "<field>" field in form "<form>" should contain "<value>"`
- `#!gherkin Then the "<field>" field should be empty`
- `#!gherkin Then the "<field>" field in form "<form>" should be empty`
- `#!gherkin Then the option "<value>" should be selected in "<field-name>"`
- `#!gherkin Then the option "<value>" should be selected in "<field-name>" in "<form>"`
