import hh_sru.config
import selenium.webdriver.support.ui
import selenium.webdriver
from pathlib import Path


def firefox() -> None:
    profile_path = list(Path(hh_sru.config.firefox_profile).expanduser().glob('*.default-release'))[0]
    options = selenium.webdriver.FirefoxOptions()
    options.add_argument("-profile")
    options.add_argument(str(profile_path))
    hh_sru.config.driver = selenium.webdriver.Firefox(options=options)
    hh_sru.config.driver_wait = selenium.webdriver.support.ui.WebDriverWait(
        hh_sru.config.driver,
        10,
    )

def chromium():
    profile_path = Path(hh_sru.config.chromium_profile).expanduser()
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={profile_path}')
    hh_sru.config.driver = selenium.webdriver.Chrome(options=options)
    hh_sru.config.driver_wait = selenium.webdriver.support.ui.WebDriverWait(
        hh_sru.config.driver,
        10,
    )


def select_engine():
    match hh_sru.config.engine_to_use:
        case 'firefox':
            firefox()
        case 'chromium':
            chromium()
