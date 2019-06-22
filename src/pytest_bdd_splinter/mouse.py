from .utils import find_by_text

from pytest_bdd import when
from pytest_bdd import parsers
from splinter.driver.webdriver import BaseWebDriver


@when(parsers.re(r'I move my mouse to "(?P<field>(?:\\.|[^"\\])*)"'))
def then_move_mouse_on(browser: BaseWebDriver, field):
    elm = find_by_text(browser, field)
    elm.mouse_over()
