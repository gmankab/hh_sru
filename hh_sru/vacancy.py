import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import selenium.webdriver.remote.webelement
import hh_sru.config
import urllib.parse
import rich.pretty
import rich.repr
import pathlib
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
        raw_url: str = str(
            element.find_element(
                By.CSS_SELECTOR,
                "a[data-qa='serp-item__title']",
            ).get_attribute('href')
        )
        parts = urllib.parse.urlsplit(raw_url)
        self.id = pathlib.PurePosixPath(parts.path).name
        self.url = parts._replace(query='', fragment='').geturl()


    def __rich_repr__(self) -> rich.repr.Result:
        yield 'id', self.id
        yield 'url', self.url
        yield 'title', self.title
        yield 'company', self.company


def iterate_vacancies() -> None:
    locator_vacancies = (
        By.CSS_SELECTOR,
        "div[data-qa='vacancy-serp__vacancy']",
    )
    vacancies = hh_sru.config.driver.find_elements(*locator_vacancies)
    for element in vacancies:
        vacancy = Vacancy(element)
        rich.pretty.pprint(vacancy, expand_all=True)
