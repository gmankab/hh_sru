import hh_sru.config
import hh_sru.vacancy
import rich
from selenium.webdriver.common.by import By


def load_next_page() -> None:
    rich.print(
        '󰖟 loading page',
        hh_sru.config.page,
    )
    hh_sru.config.driver.get(f'https://hh.ru/search/vacancy?page={hh_sru.config.page}')
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
