from selenium.webdriver.common.by import By

from pages import BasePage
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from pages.vivadecora.decoracao import DecoracaoPage
import time


def test_basic_duckduckgo_search(browser):
    # Set up test case data
    PHRASE = 'panda'

    # Search for the phrase
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()
    search_page.search(PHRASE)

    # Verify that results appear
    result_page = DuckDuckGoResultPage(browser)
    assert result_page.link_div_count() > 0
    assert result_page.phrase_result_count(PHRASE) > 0
    assert result_page.search_input_value() == PHRASE


def test_decoracao_page(browser):
    decoracao_page = DecoracaoPage(browser)
    decoracao_page.load()
    h1 = decoracao_page.all_h1()
    assert h1 is not None
    assert len(h1) == 1


def test_products_list_page(browser):
    products_page = BasePage(browser=browser, url='https://www.vivadecora.com.br/produtos/sofas')
    products_page.load()
    time.sleep(2)
    products_box = products_page.find_elements(by=By.CLASS_NAME, identifier='product-box')
    assert len(products_box) == 64
