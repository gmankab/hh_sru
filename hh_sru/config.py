from pathlib import Path
from typing import Literal
import selenium.webdriver.remote.webdriver
import selenium.webdriver.support.ui
import os


engine_to_use: Literal['chromium'] | Literal['firefox'] = 'chromium'
# see readme.md for explanation why defaults to chromium

os.environ['SE_AVOID_BROWSER_DOWNLOAD'] = 'true'
# prevents automatic downloading of propretary chromium binary
# instead please install open-source chromium builds via package manager

xdg_state_home = Path(
    os.getenv(
        'XDG_STATE_HOME',
        Path.home() / '.local' / 'state',
    )
)
hh_state_dir = xdg_state_home / 'hh_sru'
chromium_dir = hh_state_dir / 'chromium'
firefox_dir = hh_state_dir / 'firefox'
history_path = hh_state_dir / 'history.txt'
history_list: list[int] = []

driver: selenium.webdriver.remote.webdriver.WebDriver
driver_wait: selenium.webdriver.support.ui.WebDriverWait
page: int = 0
