from .utils import find_by_text

from pytest_bdd import given, when, then
from pytest_bdd import parsers
from splinter.driver.webdriver import BaseWebDriver


def absolute_url(base_url, page):
    if page.startswith(("http://", "https://")):
        return page
    return base_url + page


@given("I am on the homepage")
def given_on_the_homepage(browser: BaseWebDriver, browser_base_url):
    browser.visit(absolute_url(browser_base_url, "/"))


@given(parsers.re(r'I am on "(?P<page>[^"]+)"$'))
def given_browse_to_page(browser, browser_base_url, page):
    browser.visit(absolute_url(browser_base_url, page))


@when("I am on the homepage")
def when_on_the_homepage(browser, browser_base_url):
    browser.visit(absolute_url(browser_base_url, "/"))


@when(parsers.re(r'^I go to "(?P<page>[^"]+)"$'))
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


@when(parsers.re(r'I press "(?P<button>(?:\\.|[^"\\])*)"'))
def when_press_button(browser: BaseWebDriver, button):
    elm = find_by_text(browser, button)
    elm.click()


@then(parsers.re(r'I should be on "(?P<page>[^"]+)"$'))
def should_be_on_page(browser, browser_base_url, page):
    assert browser.url == absolute_url(browser_base_url, page)
