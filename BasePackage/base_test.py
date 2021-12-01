from getgauge.python import before_suite, after_suite
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from step_impl.CasePackage.case_package import CasePage


class BaseTest:
    driver = None
    case_page = None
    wait = None


@before_suite
def setup():
    BaseTest.driver = webdriver.Chrome(ChromeDriverManager().install())
    BaseTest.case_page = CasePage(BaseTest.driver)
    BaseTest.driver.maximize_window()
    BaseTest.driver.implicitly_wait(10)


@after_suite
def closeUp():
    BaseTest.driver.close()
