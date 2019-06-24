import time

from pytest_bdd import then, when
from pytest_bdd.parsers import parse
from splinter.driver.webdriver import BaseWebDriver

from .utils import find_by_text


@then(parse('the checkbox "{field}" is checked'))
def checkbox_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field)
    assert elm.checked


@then(parse('the checkbox "{field}" is not checked'))
def checkbox_not_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field)
    assert not elm.checked


@then(parse('the radiobutton "{field}" is checked'))
def radiobutton_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field)
    assert elm.checked


@then(parse('the radiobutton "{field}" is not checked'))
def radiobutton_not_checked(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field)
    assert not elm.checked


@when(parse('I enter "{value}" in the "{field}" field'))
def when_enter_value_in_field(browser: BaseWebDriver, field, value):
    browser.fill(field, value)


@when(parse('I enter "{value}" in the "{field}" field in form "{form}"'))
def when_enter_value_in_field_form(browser: BaseWebDriver, field, value, form):
    browser.fill_form({field: value}, name=form)


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
    data = {}
    for line in text.split("\n"):
        values = [i.strip() for i in line.strip().strip("|").split("|")]
        data[values[0]] = values[1]
    browser.fill_form(data)


@then(parse('the "{field}" field should contain "{value}"'))
def then_field_contains(browser: BaseWebDriver, field, value):
    assert browser.find_by_name(field).value == value


@then(parse('the "{field}" field in "{form}" should contain "{value}"'))
def then_form_field_contains(browser: BaseWebDriver, field, value, form):
    form_elm = browser.find_by_name(form)
    assert form_elm.find_by_name(field).value == value
