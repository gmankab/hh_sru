import selenium.webdriver.remote.webdriver
import selenium.webdriver.support.ui
from pathlib import Path
import typing
import os


engine_to_use: typing.Literal['chromium'] | typing.Literal['firefox'] = 'chromium'
xdg_state_home = Path(
    os.getenv(
        'XDG_STATE_HOME',
        Path.home() / '.local' / 'state',
    )
)
hh_state_dir = xdg_state_home / 'hh_sru'
chromium_profile = hh_state_dir / 'chromium'
firefox_profile = hh_state_dir / 'firefox'
driver: selenium.webdriver.remote.webdriver.WebDriver
driver_wait: selenium.webdriver.support.ui.WebDriverWait
os.environ['SE_AVOID_BROWSER_DOWNLOAD'] = 'true'
