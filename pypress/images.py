import json

import falcon

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from tests.conftest import run_browser


class Resource:

    def on_get(self, req, resp):
        doc = {
            'images': [
                {
                    'href': '/images/1eaf6ef1-7f2d-4ecc-a8d5-6e8adba7cc0e.png'
                }
            ]
        }

        # Create a JSON representation of the resource
        resp.text = json.dumps(doc, ensure_ascii=False)

        # The following line can be omitted because 200 is the default
        # status returned by the framework, but it is included here to
        # illustrate how this may be overridden as needed.
        resp.status = falcon.HTTP_200


class TestExecutorAPI:

    def on_get(self, req, resp):
        _browser = run_browser(config_browser='chrome', config_wait_time=10)

        try:
            search_page = DuckDuckGoSearchPage(browser=_browser)
            search_page.load()
            search_page.search('vivadecora')

            result_page = DuckDuckGoResultPage(browser=_browser)

            result_test = {
                'tests': [
                    {
                        'has_result_for_phrase': result_page.phrase_result_count('vivadecora') > 0,
                        'result': result_page.phrase_result_count('vivadecora'),
                        'expected': 'result should be bigger than 0'
                    },
                    {
                        'searched_by_correct_phrase': result_page.search_input_value() == 'vivadecora',
                        'result': result_page.search_input_value(),
                        'expected': 'vivadecora',
                    },
                    {
                        'is_in_first_result': result_page.link_first_result() == 'www.vivadecora.com.br',
                        'result': result_page.link_first_result(),
                        'expected': 'www.vivadecora.com.br',
                    }
                ]
            }

            resp.text = json.dumps(result_test, ensure_ascii=False)
            resp.status = falcon.HTTP_200
        finally:
            _browser.quit()
