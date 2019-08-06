import time

from pytest_bdd import then, when
from pytest_bdd.parsers import parse
from splinter.driver.webdriver import BaseWebDriver

from .utils import find_by_text, form_field_fill


@then(parse('the checkbox "{field}" is checked'))
def checkbox_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field).first
    assert elm.checked, f"Checkbox {field} is not checked"


@then(parse('the checkbox "{field}" is not checked'))
def checkbox_not_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field).first
    assert not elm.checked, f"Checkbox {field} is checked"


@then(parse('the radiobutton "{field}" is checked'))
def radiobutton_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field).first
    assert elm.checked, f"Radiobutton {field} is not checked"


@then(parse('the radiobutton "{field}" is not checked'))
def radiobutton_not_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field).first
    assert not elm.checked, f"Radiobutton {field} is checked"


@when(parse('I enter "{value}" in the "{field}" field'))
def when_enter_value_in_field(browser: BaseWebDriver, field, value):
    form_field_fill(browser, field, value)


@when(parse('I enter "{value}" in the "{field}" field in form "{form}"'))
def when_enter_value_in_field_form(browser: BaseWebDriver, field, value, form):
    form_field_fill(browser, field, value, form_name=form)


@when(parse('I type "{value}" in field "{field}"'))
@when(parse('I type in field "{field}" the value "{value}"'))
def when_type_value_in_field(browser: BaseWebDriver, field, value):
    browser.type(field, value)


@when(parse('I type "{value}" in field "{field}" with {cps:d} characters per second'))
@when(
    parse(
        'I type in field "{field}" the value "{value}" with {cps:d} characters per second'
    )
)
def when_slowly_type_value_in_field(browser: BaseWebDriver, field, value, cps):
    cps = int(cps)
    for i in browser.type(field, value, slowly=True):
        time.sleep(1.0 / cps)


@when(parse('I type "{value}" in field "{field}" with 1 character per second'))
@when(
    parse('I type in field "{field}" the value "{value}" with 1 character per second')
)
def when_slowly_type_value_in_field_1cps(browser: BaseWebDriver, field, value):
    for i in browser.type(field, value, slowly=True):
        time.sleep(1)


@when(parse("I fill in the following:\n{text}"))
def when_fill_multiple_fields(browser: BaseWebDriver, text):
    for line in text.split("\n"):
        values = [i.strip() for i in line.strip().strip("|").split("|")]
        form_field_fill(browser, values[0], values[1])


@when(parse('I select the option "{value}" from "{field}"'))
def when_form_option_select(browser: BaseWebDriver, field, value):
    browser.select(field, value)


@then(parse('the "{field}" field should contain "{value}"'))
def then_field_contains(browser: BaseWebDriver, field, value):
    assert browser.find_by_name(field).value == value


@then(parse('the "{field}" field in "{form}" should contain "{value}"'))
def then_form_field_contains(browser: BaseWebDriver, field, value, form):
    form_elm = browser.find_by_name(form).first
    assert form_elm.find_by_name(field).value == value


@then(parse('the option "{value}" should be selected in "{field}"'))
def then_form_option_selected(browser: BaseWebDriver, field, value):
    assert browser.find_by_name(field).value == value
