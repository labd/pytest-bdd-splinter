def absolute_url(base_url, page):
    if page.startswith(("http://", "https://")):
        return page
    return base_url + page


def find_by_text(browser, text):
    return browser.find_by_xpath(
        f'//*[@value="{text}" or @id="{text}" or @name="{text}" or text()="{text}"]'
    )
