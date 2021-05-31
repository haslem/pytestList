from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import help


class MyMapsPage:
    FOLDER_OPTS = (By.XPATH, '//li[@class="folder"]/div/div[@class="bar"]/span[@class="opts"]')
    ELEMENT_OPTS = (By.XPATH, '//li[@class="item"]/div[@class="inner"]/span[@class="opts"]')
    ELEMENT_CONTEXT = (By.XPATH, '//ul[@class="mymap-contextmenu places"]/li[@class="contextmenu-item"]')
    SELECT_ALL_ELEMENT = (By.XPATH, '//label[@title="Select all"]')
    DELETE = (By.XPATH, '//button[@class="delete"]')
    DELETE_FOLDER = (By.XPATH, '/html/body/div[2]/div[2]/div[2]/button[1]')
    DELETE_DIALOG = (By.XPATH, '//div[@class="buttons"]/button[@class="save"]')
    DELETE_NOTIFICATION = (By.XPATH, '//li[@class="info"]/button')
    QUIT_MEASURE = (By.XPATH, '//button[@class="cancel-btn"]')

    CREATE_FOLDER = (By.XPATH, '//button[@class="make-folder-btn"]')
    FOLDER_NAME = (By.XPATH, '//input[@class="value"]')
    SAVE_FOLDER = (By.XPATH, '//button[@class="save"]')



    def __init__(self, browser):
        self.browser = browser

    def multiple_actions_items(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.ELEMENT_OPTS)
        )

        els = self.browser.find_elements(*self.ELEMENT_OPTS)
        els[0].click()

        els = self.browser.find_elements(*self.ELEMENT_CONTEXT)
        els[2].click()


    def delete_all_elements(self):
        self.multiple_actions_items()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SELECT_ALL_ELEMENT)
        ).click()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.DELETE)
        ).click()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.DELETE_DIALOG)
        ).click()


    def delete_all_folders(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_all_elements_located(self.FOLDER_OPTS)
        )

        els = self.browser.find_elements(*self.FOLDER_OPTS)

        while len(els) > 0:

            els[0].click()

            els = self.browser.find_elements(*self.ELEMENT_CONTEXT)
            els[3].click()

            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.DELETE_FOLDER)
            ).click()

            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.DELETE_NOTIFICATION)
            ).click()

            help.time_out_1()
            els = self.browser.find_elements(*self.FOLDER_OPTS)


    def create_folder(self, folder_name):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CREATE_FOLDER)
        ).click()

        el = self.browser.find_element(*self.FOLDER_NAME).send_keys(folder_name)
        el = self.browser.find_element(*self.SAVE_FOLDER).click()