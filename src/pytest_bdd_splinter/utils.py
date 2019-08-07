from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from splinter.driver.webdriver import BaseWebDriver


def absolute_url(base_url, page):
    if page.startswith(("http://", "https://")):
        return page
    return base_url + page


def find_by_text(browser, text):
    return browser.find_by_xpath(
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )


def form_field_fill(
    browser: BaseWebDriver, field_name: str, value: str, form_name=None
):
    if form_name:
        base_element = browser.find_by_name(form_name)
        element = base_element.find_by_name(field_name).first
    else:
        element = browser.find_by_name(field_name).first

    if form_name:
        WebDriverWait(browser.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (
                    By.XPATH,
                    "//form[@name='%s']/*/input[@name='%s']" % (form_name, field_name),
                )
            )
        )

    else:
        WebDriverWait(browser.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.NAME, field_name))
        )

    if element.value != "":
        element.double_click()
        active_element = browser.driver.switch_to.active_element
        active_element.send_keys(Keys.BACKSPACE)
    else:
        element.click()
    element._element.send_keys(value)
