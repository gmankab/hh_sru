import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import selenium.webdriver.remote.webelement
import hh_sru.config
import urllib.parse
import rich.repr
import pathlib
from selenium.webdriver.common.by import By


class Vacancy:
    def __init__(
        self,
        element: selenium.webdriver.remote.webelement.WebElement,
        index_on_page: int,
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
        self.id: int = int(pathlib.PurePosixPath(parts.path).name)
        self.url: str = parts._replace(query='', fragment='').geturl()
        self.index_on_page: int = index_on_page
        self.page: int = hh_sru.config.page
        self.skip: bool = self.id in hh_sru.config.history_list

    def write(self) -> None:
        if not self.skip:
            with hh_sru.config.history_path.open(mode='a') as f:
                f.write(f'{self.id}\n')

    def log(self) -> None:
        if self.skip:
            action = '   [blue]skip[/]'
        else:
            action = '[green]respond[/]'
        rich.print(
            action,
            f'vacancy={self.index_on_page:02d}/49',
            f'page={self.page:02d}/39',
        )

    def __rich_repr__(self) -> rich.repr.Result:
        yield 'id', self.id
        yield 'url', self.url
        yield 'title', self.title
        yield 'company', self.company
        yield 'index_on_page', self.index_on_page
        yield 'page', self.page
