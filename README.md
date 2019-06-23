# pytest-bdd-splinter

[//]: # start-no-pypi
[![codecov](https://codecov.io/gh/labd/pytest-bdd-splinter/branch/master/graph/badge.svg)](https://codecov.io/gh/labd/pytest-bdd-splinter)
[![pypi](https://img.shields.io/pypi/v/pytest-bdd-splinter.svg)](https://pypi.python.org/pypi/pytest-bdd-splinter/)
[![readthedocs](https://readthedocs.org/projects/pytest-bdd-splinter/badge/)](https://pytest-bdd-splinter.readthedocs.io/en/latest/)
[//]: # end-no-pypi

This module provides a number of common `given`, `when`, `then` steps for
[pytest-splinter](https://github.com/pytest-dev/pytest-splinter) in
[pytest-bdd](https://github.com/pytest-dev/pytest-bdd)

## Installation

```shell
pip install pytest-bdd-splinter
```

## Number of examples
```gherkin
Scenario: Fill in a form
    Given I am using a large device
    And I am on the homepage
    When I go to "/my-contact-form/"
    And I fill in the following:
        | first_name | John  |
        | last_name  | Doe  |
        | username   | johndoe  |
        | password   | mysecret |
    And I press "agree-tos"
    And I press "submit"
    Then I should be on "/thank-you/"
    And I should see "Thank you for creating an account"
```

## More information
Please see [the documentation](https://pytest-bdd-splinter.readthedocs.io/en/latest/)
to read more about installation, configuration and an overview of all the
available steps.
