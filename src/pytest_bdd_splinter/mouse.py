from pytest_bdd import when
from pytest_bdd.parsers import parse
from splinter.driver.webdriver import BaseWebDriver

from .utils import find_by_text


@when(parse('I move my mouse to "{field}"'))
def then_move_mouse_on(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field).first
    elm.mouse_over()


@when(parse('I click on the link "{text}"'))
def then_move_mouse_on(browser: BaseWebDriver, text):
    elm = find_by_text(browser, text).first
    elm.click()
