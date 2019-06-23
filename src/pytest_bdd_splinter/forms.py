import time

from .utils import find_by_text

from pytest_bdd import when, then
from pytest_bdd import parsers
from splinter.driver.webdriver import BaseWebDriver


@then(
    parsers.re(
        r'the checkbox "(?P<field>(?:\\.|[^"\\])*)" is (?P<state>not checked|checked)$'
    )
)
def checkbox_state(browser: BaseWebDriver, field, state):
    elm = find_by_text(browser, field)
    if state == "checked":
        assert elm.checked
    else:
        assert not elm.checked


@then(
    parsers.re(
        r'the radiobutton "(?P<field>(?:\\.|[^"\\])*)" is (?P<state>not checked|checked)$'
    )
)
def radiobutton_state(browser: BaseWebDriver, field, state):
    elm = find_by_text(browser, field)
    if state == "checked":
        assert elm.checked
    else:
        assert not elm.checked


@when(
    parsers.re(
        r'^I enter "(?P<value>(?:\\.|[^"\\])*)" in the "(?P<field>(?:\\.|[^"\\])*)" field$'
    )
)
def when_enter_value_in_field(browser: BaseWebDriver, field, value):
    browser.fill(field, value)


@when(
    parsers.re(
        r'^I enter "(?P<value>(?:\\.|[^"\\])*)" in the "(?P<field>(?:\\.|[^"\\])*)" field in form "(?P<form>(?:\\.|[^"\\])*)"$'
    )
)
def when_enter_value_in_field_form(browser: BaseWebDriver, field, value, form):
    """I enter "<value>" in the "<field>" field in form "<form>" """
    browser.fill_form({field: value}, name=form)


@when(
    parsers.re(
        r'^I type "(?P<value>(?:\\.|[^"\\])*)" in field "(?P<field>(?:\\.|[^"\\])*)"$'
    )
)
@when(
    parsers.re(
        r'^I type in field "(?P<field>(?:\\.|[^"\\])*)" the value "(?P<value>(?:\\.|[^"\\])*)"$'
    )
)
def when_type_value_in_field(browser: BaseWebDriver, field, value):
    browser.type(field, value)


@when(
    parsers.re(
        r'^I type "(?P<value>(?:\\.|[^"\\])*)" in field "(?P<field>(?:\\.|[^"\\])*)" with (?P<cps>\d+) characters? per second$'
    )
)
@when(
    parsers.re(
        r'^I type in field "(?P<field>(?:\\.|[^"\\])*)" the value "(?P<value>(?:\\.|[^"\\])*)" with (?P<cps>\d+) characters? per second$'
    )
)
def when_slowly_type_value_in_field(browser: BaseWebDriver, field, value, cps):
    cps = int(cps)
    for i in browser.type(field, value, slowly=True):
        time.sleep(1.0 / cps)


@when(parsers.parse("I fill in the following:\n{text}"))
def when_fill_multiple_fields(browser: BaseWebDriver, text):
    data = {}
    for line in text.split("\n"):
        values = [i.strip() for i in line.strip().strip("|").split("|")]
        data[values[0]] = values[1]
    browser.fill_form(data)


@then(
    parsers.re(
        r'the "(?P<field>(?:\\.|[^"\\])*)" field should contain "(?P<value>(?:\\.|[^"\\])*)"$'
    )
)
def then_field_contains(browser: BaseWebDriver, field, value):
    assert browser.find_by_name(field).value == value

@then(
    parsers.re(
        r'the "(?P<field>(?:\\.|[^"\\])*)" field in "(?P<form>(?:\\.|[^"\\])*)" should contain "(?P<value>(?:\\.|[^"\\])*)"$'
    )
)
def then_form_field_contains(browser: BaseWebDriver, field, value, form):
    """the "<field>" field in form "<form>" should contain "<value>" """
    form_elm = browser.find_by_name(form)
    assert form_elm.find_by_name(field).value == value
