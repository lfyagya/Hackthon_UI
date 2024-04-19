import re
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from seleniumbase.base_selenium import SeleniumBase
from config.config import Config
from selenium.webdriver.remote.webdriver import WebDriver


test_config = Config()

class Leapfrogger():

    __release_note = ".releaseNote_module_releaseNoteModal__header_Close__7943ddf4"
    __people = '.flex-fix.nav_module_nav__37ad822e [href="/leapfroggers"]'
    __search_leapfroggers = "employees__search-input"
    __apply_filter = "button ml-10 sm-d-none button--secondary"

    def release_note(self, driver) -> WebElement:
        release_note_element = driver.find_element(By.CLASS_NAME, 'releaseNote_module_releaseNoteModal__header_Close__7943ddf4')
        release_note_element.click()
        return release_note_element

    def search_leapfrogger(self, driver, search_name) -> WebElement:
        driver.get(test_config.BASE_URL + '/leapfroggers?q='+search_name)
        return driver
