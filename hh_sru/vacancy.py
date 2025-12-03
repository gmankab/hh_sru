import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import selenium.webdriver.remote.webelement
import hh_sru.config
import rich.pretty
import rich.repr
from selenium.webdriver.common.by import By


class Vacancy:
    def __init__(
        self,
        element: selenium.webdriver.remote.webelement.WebElement,
    ) -> None:
        self.company: str = element.find_element(
            By.CSS_SELECTOR,
            "[data-qa='vacancy-serp__vacancy-employer-text']"
        ).text
        self.title: str = element.find_element(
            By.CSS_SELECTOR,
            "[data-qa='serp-item__title-text']"
        ).text
        self.url: str = str(
            element.find_element(
                By.CSS_SELECTOR,
                "a[data-qa='serp-item__title']",
            ).get_attribute('href')
        ).removesuffix('?hhtmFrom=vacancy_search_list')


    def __rich_repr__(self) -> rich.repr.Result:
        yield 'company', self.company
        yield 'title', self.title
        yield 'url', self.url


def iterate_vacancies() -> None:
    locator_vacancies = (
        By.CSS_SELECTOR,
        "div[data-qa='vacancy-serp__vacancy']",
    )
    vacancies = hh_sru.config.driver.find_elements(*locator_vacancies)
    for element in vacancies:
        vacancy = Vacancy(element)
        rich.pretty.pprint(vacancy, expand_all=True)
