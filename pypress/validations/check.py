from typing import Dict, List

from pages import BasePage


def count_elements_equal_to(page, to_check, expected_count, *args, **kwargs):
    result = {
        'count_elements_equal_to': len(to_check) == expected_count,
        'page_under_test': page.url,
        'calculated_count': len(to_check),
        'expected_count': expected_count,
    }
    return result


available_functions = {
    'count_elements_equal_to': count_elements_equal_to,
}


def execute_stage(page: BasePage, scenario: Dict, result) -> List:
    checks_results = list()
    check_step = scenario.get('check', None)
    if check_step:
        for key, value in check_step.items():
            func_to_exec = available_functions[key]
            check_result = func_to_exec(page, result, value)
            checks_results.append(check_result)
    return checks_results
