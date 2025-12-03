from pathlib import Path
from typing import Literal
import selenium.webdriver.remote.webdriver
import selenium.webdriver.support.ui
import os


engine_to_use: Literal['chromium'] | Literal['firefox'] = 'chromium'
# for using chromium, install it via sudo dnf install chromium
# for using firefox, install it via sudo dnf install firefox

# hh.ru is known to have better performance on chromium
# especially when using developer tools (ctrl+shift+i)

xdg_state_home = Path(
    os.getenv(
        'XDG_STATE_HOME',
        Path.home() / '.local' / 'state',
    )
)
hh_state_dir = xdg_state_home / 'hh_sru'
chromium_dir = hh_state_dir / 'chromium'
firefox_dir = hh_state_dir / 'firefox'
driver: selenium.webdriver.remote.webdriver.WebDriver
driver_wait: selenium.webdriver.support.ui.WebDriverWait

os.environ['SE_AVOID_BROWSER_DOWNLOAD'] = 'true'
# prevents automatic downloading of propretary chromium binary
# instead please install open-source chromium builds via package manager
