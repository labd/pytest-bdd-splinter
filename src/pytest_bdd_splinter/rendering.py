from pytest_bdd import given, then, when
from pytest_bdd.parsers import parse
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


@given(parse("I am using a window size of {width:d}x{height:x}"))
def resize_browser_format_size(browser, width, height):
    browser.driver.set_window_size(width, height)


@given(parse("I am using a {device}"))
@given(parse("I am using an {device}"))
def resize_browser_format(browser, device):
    dimensions = DEVICES.get(device)
    assert dimensions is not None, f"No device with name {device}"
    browser.driver.set_window_size(*dimensions)


@when(parse('I see "{text}"'))
def then_text_available(browser: BaseWebDriver, text):
    assert browser.is_text_present(text)


@then(parse('I should see "{text}"'))
def then_text_available(browser: BaseWebDriver, text):
    assert browser.is_text_present(text)


@when(parse('I do not see "{text}"'))
def when_text_not_available(browser: BaseWebDriver, text):
    assert browser.is_text_not_present(text)


@then(parse('I should not see "{text}"'))
def then_text_not_available(browser: BaseWebDriver, text):
    assert browser.is_text_not_present(text)
