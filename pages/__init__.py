class BasePage:

    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def load(self):
        self.browser.get(self.url)
        # pass

    def find_elements(self, by, identifier):
        elements = self.browser.find_elements(by=by, value=identifier)
        return elements


class PageHandler(object):

    @staticmethod
    def load(page: BasePage):
        page.load()

    @staticmethod
    def find_elements(page: BasePage, by, identifier):
        return page.find_elements(by=by, identifier=identifier)
