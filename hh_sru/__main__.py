import hh_sru.config
import hh_sru.setup
import hh_sru.login
import hh_sru.parse


def main():
    hh_sru.setup.load_history()
    hh_sru.setup.select_engine()
    hh_sru.login.wait_for_login()
    hh_sru.parse.iterate_vacancies()
    hh_sru.config.driver.quit()


if __name__ == '__main__':
    main()
