from pytest_bdd import parsers, then, when
from pytest_bdd.parsers import parse
from splinter.driver.webdriver import BaseWebDriver

from .utils import (
    fill_text_field,
    find_by_name_or_id,
    find_by_text,
    find_child_by_name_or_id,
    find_child_by_text,
    find_option,
    parse_table,
    type_slowly,
)


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
    element = find_by_name_or_id(browser, field).first
    fill_text_field(element, value)


@when(parse('I enter "{value}" in the "{field}" field in form "{form}"'))
def when_enter_value_in_field_form(browser: BaseWebDriver, field, value, form):
    element = find_child_by_name_or_id(browser, form, field).first
    fill_text_field(element, value)


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
    elm = find_by_name_or_id(browser, field).first
    type_slowly(elm, value, cps=int(cps))


@when(parse('I type "{value}" in field "{field}" with 1 character per second'))
@when(
    parse('I type in field "{field}" the value "{value}" with 1 character per second')
)
def when_slowly_type_value_in_field_1cps(browser: BaseWebDriver, field, value):
    when_slowly_type_value_in_field(browser, field, value, cps=1)


@when(
    parse(
        'I type "{value}" in the "{field}" field in "{form}"'
        " with {cps:d} characters per second"
    )
)
def when_slowly_type_value_in_form_field(
    browser: BaseWebDriver, field, form, value, cps
):
    elm = find_child_by_text(browser, form, field).first
    type_slowly(elm, value, cps=cps)


@when(
    parse(
        'I type "{value}" in the "{field}" field in "{form}"'
        " with 1 character per second"
    )
)
def when_slowly_type_value_in_form_field_1cps(
    browser: BaseWebDriver, field, form, value
):
    when_slowly_type_value_in_form_field(
        browser, field=field, value=value, form=form, cps=1
    )


@when(parse("I fill in the following:\n{table}"), converters={"table": parse_table})
def when_fill_multiple_fields(browser: BaseWebDriver, table):
    for name, value in table:
        field = find_by_name_or_id(browser, name).first
        fill_text_field(field, value)


@when(
    parse('I fill in the following in "{form}":\n{table}'),
    converters={"table": parse_table},
)
def when_fill_multiple_fields_form(browser: BaseWebDriver, form, table):
    for name, value in table:
        field = find_child_by_name_or_id(browser, form, name).first
        fill_text_field(field, value)


# too greedy: @when(parse('I select the option "{value}" from "{field}"'))
@when(parsers.re(r'^I select the option "(?P<value>.+?)" from "(?P<field>[^\"]+)"$'))
def when_form_option_select(browser: BaseWebDriver, field, value):
    """Select an option in a <select> field, either by name or value.
    The field can be found by name or ID.
    """
    # First find the <select> box so developers don't have to debug whether
    # the <select> box doesn't exist, or the <option> doesn't exist.
    field = find_by_name_or_id(browser, field).first
    option = find_option(field, value).first
    option.click()


@when(parse('I select the option "{value}" from "{field}" in form "{form}"'))
def when_form_option_select_form(browser: BaseWebDriver, field, value, form):
    """Select an option in a <select> field, either by name or value.
    The field can be found by name or ID.
    """
    # First find the <select> box so developers don't have to debug whether
    # the <select> box doesn't exist, or the <option> doesn't exist.
    field = find_child_by_name_or_id(browser, form, field)
    option = find_option(field, value).first
    option.click()


@then(parse('the "{field}" field should contain "{value}"'))
def then_field_contains(browser: BaseWebDriver, field, value):
    elm = find_by_name_or_id(browser, field).first
    found_text = elm.value  # takes .text for non-input fields.
    assert found_text == value, f'Text "{value}" not equal {found_text!r} in "{field}"'


@then(parse('the "{field}" field in "{form}" should contain "{value}"'))
def then_form_field_contains(browser: BaseWebDriver, field, value, form):
    elm = find_child_by_name_or_id(browser, form, field)
    found_text = elm.value  # takes .text for non-input fields.
    assert (
        found_text == value
    ), f'Text "{value}" not equal {found_text!r} in "{field}" of form "{form}"'


@then(parse('the "{field}" field should be empty'))
def then_field_is_empty(browser: BaseWebDriver, field):
    elm = find_by_name_or_id(browser, field).first
    found_text = elm.value  # takes .text for non-input fields.
    assert found_text == "", f'Field "{field}" is not empty, found "{found_text!r}"'


@then(parse('the "{field}" field in "{form}" should be empty'))
def then_form_field_empty(browser: BaseWebDriver, field, form):
    elm = find_child_by_name_or_id(browser, form, field).first
    found_text = elm.value  # takes .text for non-input fields.
    assert (
        found_text == ''
    ), f'Field "{field}" of form "{form}" is not empty, found "{found_text!r}"'


# too greedy: @then(parse('the option "{value}" should be selected in "{field}"'))
@then(
    parsers.re('^the option "(?P<value>.+?)" should be selected in "(?P<field>[^"]+)"$')
)
def then_form_option_selected(browser: BaseWebDriver, value, field):
    """The field can be selected as name or ID."""
    elm = find_by_name_or_id(browser, field).first
    _assert_selected(field, elm, value)


@then(parse('the option "{value}" should be selected in "{field}" in form "{form}"'))
def then_form_option_selected_form(browser: BaseWebDriver, value, field, form):
    elm = find_child_by_name_or_id(browser, form, field).first
    _assert_selected(field, elm, value)


def _assert_selected(name, elm, value):
    # The following selenium-specific code is really slow on large lists
    # because it iterates over all options:
    #   option = Select(elm._element).first_selected_option
    #
    # Hence taking advantage of the classic 'selectedIndex' attribute instead:
    selected_index = int(elm["selectedIndex"])
    assert int(selected_index) >= 0, f'Field "{name}" has no option selected'

    options = elm.find_by_xpath(f"(option)[{selected_index + 1}]")
    assert options, f'No selected option found for field "{name}"'
    option = options.first
    assert (
        option.text == value or option["value"] == value
    ), f'Selected option of "{name}" is "{option.text}", not "{value}"'
