from selenium.webdriver.common.by import By


class DecoracaoPage:
    URL = 'https://www.vivadecora.com.br/decoracao'

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def all_h1(self):
        h1 = self.browser.find_elements(By.TAG_NAME, 'h1')
        return h1
