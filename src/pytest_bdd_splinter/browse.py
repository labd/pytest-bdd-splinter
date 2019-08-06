from pytest_bdd import given, then, when
from pytest_bdd.parsers import parse
from selenium.common.exceptions import WebDriverException
from splinter.driver.webdriver import BaseWebDriver

from .utils import absolute_url, find_by_text


@given("I am on the homepage")
def given_on_the_homepage(browser: BaseWebDriver, browser_base_url):
    browser.visit(absolute_url(browser_base_url, "/"))


@given(parse('I am on "{page}"'))
def given_browse_to_page(browser, browser_base_url, page):
    browser.visit(absolute_url(browser_base_url, page))


@when("I am on the homepage")
def when_on_the_homepage(browser, browser_base_url):
    browser.visit(absolute_url(browser_base_url, "/"))


@when(parse('I go to "{page}"'))
def when_browse_to_page(browser, browser_base_url, page):
    browser.visit(absolute_url(browser_base_url, page))


@when("I move backward one page")
def when_browser_back_button(browser):
    browser.back()


@when("I move forward one page")
def when_browser_forward_button(browser):
    browser.forward()


@when("I reload the page")
def when_reload_the_page(browser):
    browser.reload()


@when(parse('I press "{button}"'))
def when_press_button(browser: BaseWebDriver, button):
    elm = find_by_text(browser, button)
    elm.click()


@then(parse('I should be on "{page}"'))
def should_be_on_page(browser, browser_base_url, page):
    assert browser.url == absolute_url(browser_base_url, page)


@then("I print the current url")
def print_current_url(browser: BaseWebDriver):
    """Dump the current URL"""
    print("      Current URL:", browser.driver.current_url)

    try:
        browser_console = browser.driver.get_log("browser")
    except WebDriverException:
        pass  # not supported on Firefox webdriver.
    else:
        print("      Browser console:")
        for entry in browser_console:
            print("        {level:7} {source}:\t{message}".format(**entry))
