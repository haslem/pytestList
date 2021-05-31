from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import help


class SavePage:
    SAVE = (By.XPATH, '//button[@class="save"]')
    # SAVE_TOAST = (By.XPATH, '//ul[@class="notification"]/li[@class="info"]/button')

    # SAVE_TOAST = (By.XPATH, '/html/body/div/div[2]/ul/li/button')
    SAVE_TOAST = (By.XPATH, '//li[@class="info"]/button')

    SAVE_NAME = (By.XPATH, '//input[@class="title"]')

    WHERE_SAVE = (By.XPATH, '//div[@class="maps-select mymap-folders"]')
    FOLDER_TO_SAVE = (By.XPATH, '//span[@class="title"]')


    def __init__(self, browser):
        self.browser = browser

    def save(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE)
        ).click()

    def close_save_toast(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE_TOAST)
        ).click()

    def change_save_name(self, name):
        elem = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE_NAME)
        )
        elem = self.browser.find_element(*self.SAVE_NAME)
        for i in range(20):
            elem.send_keys(u'\ue003')
        elem.send_keys(name)

    def save_to_folder(self, folder_to_save):
        elem = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.WHERE_SAVE)
        ).click()

        elems = self.browser.find_elements(*self.FOLDER_TO_SAVE)

        for el in elems:
            if (el.text == folder_to_save):
                el.click()
                break
