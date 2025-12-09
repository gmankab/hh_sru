import selenium.webdriver.support.ui
import selenium.webdriver
import hh_sru.config
import rich


def load_history() -> None:
    if not hh_sru.config.history_path.exists():
        return
    with hh_sru.config.history_path.open() as f:
        for line in f.readlines():
            hh_sru.config.history_set.add(
                int(line)
            )
    rich.print(
        '[blue]󰙡 will skip[/]',
        len(hh_sru.config.history_set),
        'vacancies from',
        hh_sru.config.history_path,
    )


def firefox() -> None:
    rich.print('󰈹 loading firefox data from', hh_sru.config.firefox_dir)
    hh_sru.config.firefox_dir.mkdir(parents=True, exist_ok=True)
    options = selenium.webdriver.FirefoxOptions()
    options.add_argument(f'-profile={hh_sru.config.firefox_dir}')
    hh_sru.config.driver = selenium.webdriver.Firefox(options=options)
    hh_sru.config.driver_wait = selenium.webdriver.support.ui.WebDriverWait(
        hh_sru.config.driver,
        10,
    )

def chromium():
    rich.print('󰊯 loading chromium data from', hh_sru.config.chromium_dir)
    options = selenium.webdriver.ChromeOptions()
    options.add_argument(f'--user-data-dir={hh_sru.config.chromium_dir}')
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
