import time

from pytest_bdd import parsers, when
from splinter.driver.webdriver import BaseWebDriver


@when(parsers.parse("I wait for {seconds:f} seconds"), converters={"seconds": float})
def when_wait_x_seconds(seconds=1):
    time.sleep(seconds)


@when(parsers.parse("I wait for {seconds:d} seconds"), converters={"seconds": int})
def when_wait_x_seconds_int(seconds=1):
    time.sleep(seconds)


@when("I wait for 1 second")
def when_wait_1_second(browser: BaseWebDriver):
    time.sleep(1)
