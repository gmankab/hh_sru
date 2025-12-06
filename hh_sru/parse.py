import hh_sru.config
import hh_sru.vacancy
import rich.pretty
from selenium.webdriver.common.by import By


def iterate_vacancies() -> None:
    locator_vacancies = (
        By.CSS_SELECTOR,
        "div[data-qa='vacancy-serp__vacancy']",
    )
    vacancies = hh_sru.config.driver.find_elements(*locator_vacancies)
    for element in vacancies:
        vacancy = hh_sru.vacancy.Vacancy(element)
        if vacancy.id in hh_sru.config.history_list:
            rich.print('skipping vacancy', vacancy.id)
        else:
            rich.print('responding to vacancy')
            rich.pretty.pprint(vacancy, expand_all=True)
            vacancy.write()
