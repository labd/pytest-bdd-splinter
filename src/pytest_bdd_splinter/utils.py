def find_by_text(browser, text):
    return browser.find_by_xpath(
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )
