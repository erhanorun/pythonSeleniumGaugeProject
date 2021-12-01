import configparser
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element_by_xpath(self, xpath):
        return self.driver.find_element_by_xpath(xpath)

    def find_element_by_id(self, id):
        return self.driver.find_element_by_id(id)

    def click_element_by_xpath(self, xpath):
        self.driver.find_element_by_xpath(xpath).click()

    def click_element_by_id(self, id):
        self.driver.find_element_by_id(id).click()

    def read_props(self):
        config = configparser.ConfigParser()
        config.read(os.path.abspath("config.properties"))
        return config

    def verify_element_not_exist_by_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            not_found = False
        except:
            not_found = True

        assert not_found
