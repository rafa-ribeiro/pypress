from pypress.tasks import execute_all_validations

scenarios = [
    {
        'description': 'Valida que só tem 1 tag h1 na página /decoracao',
        'setup': {
            'visit': 'https://www.vivadecora.com.br/decoracao',
        },
        'action': {
            'collect_elements': 'TAG_NAME=h1',
        },
        'check': {
            'count_elements_equal_to': 1,
        },
    },
    {
        'description': 'Valida que existem 64 produtos exibidos na primeira página',
        'setup': {
            'visit': 'https://www.vivadecora.com.br/produtos/sofas',
        },
        'action': {
            'wait_for': 4,
            'collect_elements': 'CLASS=product-box',
        },
        'check': {
            'count_elements_equal_to': 64,
        },
    },
    {
        'description': 'Valida que existe 60 produtos exibidos na página 2',
        'setup': {
            'visit': 'https://www.vivadecora.com.br/produtos/sofas/pagina/2',
        },
        'action': {
            'wait_for': 3,
            'collect_elements': 'CLASS=product-box',
        },
        'check': {
            'count_elements_equal_to': 60,
        },
    },
]


def create_task():
    task = execute_all_validations.delay(scenarios=scenarios)
    return task
