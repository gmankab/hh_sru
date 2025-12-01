import hh_sru.config
import hh_sru.setup
import hh_sru.login
import hh_sru.vacancy


def main():
    hh_sru.setup.select_engine()
    hh_sru.login.wait()
    hh_sru.config.driver.quit()


if __name__ == '__main__':
    main()
