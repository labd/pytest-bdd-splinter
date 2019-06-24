import time

from pytest_bdd import parsers, when
from splinter.driver.webdriver import BaseWebDriver


@when(parsers.parse("I wait for {seconds:f} seconds"), converters={"seconds": float})
def when_wait_x_seconds(browser: BaseWebDriver, seconds=1.0):
    time.sleep(seconds)


@when("I wait for 1 second")
def when_wait_1_second(browser: BaseWebDriver):
    time.sleep(1)
