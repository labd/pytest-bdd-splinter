Feature: Multiple device

    Examples:
    | device             |
    | extra small device |
    | small device       |
    | medium device      |
    | large device       |
    | extra large device |

    Scenario Outline: Show index extra small
        Given I am using a <device>
        And I am on the homepage
        Then I should be on "/"
        And I should see "Index page"
