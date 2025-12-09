import selenium.webdriver.support.expected_conditions
import hh_sru.config
import hh_sru.vacancy
import rich
from selenium.webdriver.common.by import By


def load_next_page() -> None:
    url = f'https://hh.ru/search/vacancy?page={hh_sru.config.page}'
    rich.print('󰖟 loading page', url)
    hh_sru.config.driver.get(url)
    hh_sru.config.page += 1


def pages() -> None:
    while hh_sru.config.page < 40:
        vacancies()
        load_next_page()


def vacancies() -> None:
    locator_vacancies = (
        By.CSS_SELECTOR,
        "div[data-qa='vacancy-serp__vacancy']",
    )
    vacancies = hh_sru.config.driver.find_elements(*locator_vacancies)
    for index_on_page, element in enumerate(vacancies):
        vacancy = hh_sru.vacancy.Vacancy(
            element=element,
            index_on_page=index_on_page,
        )
        vacancy.write()
        vacancy.log()

        exit()


def parse_vacancy(vacancy: hh_sru.vacancy.Vacancy) -> None:
    rich.print('󰖟 loading page', vacancy.url)
    hh_sru.config.driver.get(vacancy.url)
    button = hh_sru.config.driver_wait.until(
        selenium.webdriver.support.expected_conditions
        .presence_of_all_elements_located((
            By.CSS_SELECTOR,
            'span.magritte-button__label___zplmt_7-0-4',
        ))
    )
    button.click()
