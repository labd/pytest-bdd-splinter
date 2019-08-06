import time
from typing import Union

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of
from selenium.webdriver.support.ui import WebDriverWait
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement
from splinter.element_list import ElementList


def absolute_url(base_url, page):
    if page.startswith(("http://", "https://")):
        return page
    return base_url + page


def find_by_text(browser, text) -> ElementList:
    return browser.find_by_xpath(
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )


def find_by_name_or_id(
    browser: Union[BaseWebDriver, WebDriverElement], name_or_id: str
) -> ElementList:
    """Allow elements to by found by ID and name."""
    # Should not try "find_by_name() or find_by_id()" as this causes 2 slow requests.
    # TODO: A nice addition would be finding form fields by their for-label.
    return browser.find_by_xpath(f'//*[@id="{name_or_id}" or @name="{name_or_id}"]')


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
    # Mainly preserved for backward
    if form_name:
        base_element = find_by_name_or_id(browser, form_name).first
        element = find_by_name_or_id(base_element, field_name).first
    else:
        element = find_by_name_or_id(browser, field_name).first

    fill_text_field(element, value)


def type_slowly(elm, value, *, cps=100):
    for _ in elm.type(value, slowly=True):
        time.sleep(1.0 / cps)
