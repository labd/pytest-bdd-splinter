from pytest_bdd import given, when, then
from pytest_bdd import parsers
from splinter.driver.webdriver import BaseWebDriver

DEVICES = {
    "extra small device": (320, 600),
    "small device": (768, 1024),
    "medium device": (1024, 768),
    "large device": (992, 558),
    "extra large device": (1200, 650),
}


@given("I am using a <device>")
def resize_browser_format_name(browser, device):
    dimensions = DEVICES.get(device)
    assert dimensions is not None, f"No device with name {device}"
    browser.driver.set_window_size(*dimensions)


@given(parsers.parse("I am using a window size of {width:d}x{height:x}"))
def resize_browser_format_size(browser, width, height):
    browser.driver.set_window_size(width, height)


@given(parsers.re(r"^I am using an? (?P<device>.*)$"))
def resize_browser_format(browser, device):
    dimensions = DEVICES.get(device)
    assert dimensions is not None, f"No device with name {device}"
    browser.driver.set_window_size(*dimensions)


@when(parsers.re(r'^I see "(?P<text>(?:\\.|[^"\\])*)"'))
def then_text_available(browser: BaseWebDriver, text):
    assert browser.is_text_present(text)


@then(parsers.re(r'^I should see "(?P<text>(?:\\.|[^"\\])*)"'))
def then_text_available(browser: BaseWebDriver, text):
    assert browser.is_text_present(text)


@when(parsers.re(r'^I do not see "(?P<text>(?:\\.|[^"\\])*)"'))
def when_text_not_available(browser: BaseWebDriver, text):
    assert browser.is_text_not_present(text)


@then(parsers.re(r'^I should not see "(?P<text>(?:\\.|[^"\\])*)"'))
def then_text_not_available(browser: BaseWebDriver, text):
    assert browser.is_text_not_present(text)
