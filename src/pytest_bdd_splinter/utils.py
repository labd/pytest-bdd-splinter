import time
from typing import List, Union

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.ui import WebDriverWait
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from splinter.element_list import ElementList


def absolute_url(base_url, page):
    if page.startswith(("http://", "https://")):
        return page
    return base_url + page


def find_by_text(
    base_element: Union[BaseWebDriver, WebDriverElement], text: str
) -> ElementList:
    assert '"' not in text, f"Unsupported text element: {text!r}"
    return base_element.find_by_xpath(
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )


def find_by_name_or_id(
    base_element: Union[BaseWebDriver, WebDriverElement], name_or_id: str
) -> ElementList:
    """Allow elements to by found by ID and name."""
    assert '"' not in name_or_id, f"Unsupported element name: {name_or_id!r}"
    return base_element.find_by_xpath(
        f'//*[@id="{name_or_id}" or @name="{name_or_id}"]'
    )


def find_child_by_text(browser: BaseWebDriver, parent: str, text: str) -> ElementList:
    # Find by child with text() appears to be broken in selenium webdrivers,
    # so select in a single path:
    assert '"' not in parent, f"Unsupported element name: {parent!r}"
    assert '"' not in text, f"Unsupported text element: {text!r}"
    return browser.find_by_xpath(
        f'//*[@id="{parent}" or @name="{parent}"]'
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )


def find_option(field, value: str):
    """Find the option for a ``<select>`` field."""
    return field.find_by_xpath(f'//option[@value="{value}" or text()="{value}"]')


def fill_text_field(element: WebDriverElement, value: str):
    """Fill a form field using human-like typing.

    When splinter runs with a Selenium WebDriver, this method clears the
    input field using backspaces first. This is a workaround for
    https://github.com/SeleniumHQ/selenium/issues/6741. As React restores the state,
    the existing input value will not cleared, and new text would be appended instead.
    """
    # Can't perform isinstance(browser.driver, ..) check because there is no common base class.
    try:
        # Directly access selenium web driver element
        raw_element = element._element
    except AttributeError:
        # No selenium driver, doesn't support send_keys, nor needs it.
        # These drivers don't run advanced JavaScript or React.
        element.value = value
        return

    # Clear in React-supported way
    current_value = element["value"]  # retrieve once
    if current_value != "":
        backspaces = Keys.BACK_SPACE * len(current_value)
        keys = f"{Keys.END}{backspaces}{value}"
    else:
        keys = value

    # For delayed visibility on same page, give some time to appear
    WebDriverWait(element.parent.driver, 5).until(visibility_of(raw_element))
    raw_element.send_keys(keys)


def form_field_fill(
    browser: BaseWebDriver, field_name: str, value: str, form_name=None
):
    # Mainly preserved for backward compatibility
    if form_name:
        base_element = find_by_name_or_id(browser, form_name).first
        element = find_by_name_or_id(base_element, field_name).first
    else:
        element = find_by_name_or_id(browser, field_name).first

    fill_text_field(element, value)


def parse_table(text) -> List[List[str]]:
    data = []
    for line in text.split("\n"):
        values = [i.strip() for i in line.strip().strip("|").split("|")]
        data.append(values)
    return data


def type_slowly(elm, value, *, cps=100):
    for _ in elm.type(value, slowly=True):
        time.sleep(1.0 / cps)
