import selenium.webdriver.support.expected_conditions
import selenium.webdriver.support.ui
import selenium.webdriver.remote.webdriver
import selenium.common.exceptions
import hh_sru.config
import typing
import rich
from selenium.webdriver.common.by import By


def wait_for_login() -> None:
    while True:
        rich.print('󰀖 checking login status')
        result = hh_sru.config.driver_wait.until(find_buttons)
        match result:
            case 'login':
                rich.print('󰍂 please login, after that press <enter> in the terminal to continue')
                input()
            case 'chat':
                rich.print('󰍂 you are logged in')
                break


def find_buttons(
    driver: selenium.webdriver.remote.webdriver.WebDriver,
) -> typing.Literal['login'] | typing.Literal['chat'] | typing.Literal[False]:
    if driver.find_elements(
        By.CSS_SELECTOR,
        '[data-qa="mainmenu_profile-link"]',
    ):
        return 'login'
    if driver.find_elements(
        By.CSS_SELECTOR,
        '[data-qa="chatik-activator"]',
    ):
        return 'chat'
    return False
