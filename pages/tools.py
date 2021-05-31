from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import help


class Tools:
    SHARE = (By.XPATH, '//span[@class="share-item-title sht-link"]')
    COPY_LINK = (By.XPATH, '//button[@class="copy"]')
    CLOSE_SHARE = (By.XPATH, '//button[@class="close"]')

    MEASURE = (By.XPATH, '//div[@class="shitem si-distanceMeter"]')
    MARKS = (By.XPATH, '//div[@class="shitem si-usermarks"]')

    #SHARE_TOGGLE = (By.XPATH, '//span[@class="share-switch"]')
    SHARE_TOGGLE = (By.CLASS_NAME, 'share-slider')
    NEW_SHARE = (By.XPATH, '/html/body/div[2]/div[2]/div[1]/span[2]')
    #SHARE_TOGGLE = (By.XPATH, '//div[@class="switch-container not-shared"]//label//span')



    def __init__(self, browser):
        self.browser = browser


    def share(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SHARE)
        ).click()

    def copy_link(self):
        #print("try to click copy")
        # el = WebDriverWait(self.browser, 2).until(
        #     EC.visibility_of_element_located(self.COPY_LINK)
        # ).click()
        el = WebDriverWait(self.browser, 2).until(
            EC.element_to_be_clickable(self.COPY_LINK)
        ).click()
        #print("copy clicked")

    def share_on(self):
        # print("try to toggle on click")
        # #el = self.browser.find_element(*self.SHARE_TOGGLE)
        # el = WebDriverWait(self.browser, 2).until(
        #     EC.visibility_of_element_located(self.SHARE_TOGGLE)
        # ).click()
        # print("Share on click")
        try:
            #print("try to toggle on click")
            #el = self.browser.find_element(*self.SHARE_TOGGLE).click()
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.SHARE_TOGGLE)
            ).click()
            #print("Share on click")
            help.time_out()
        except:
            #print("Share already on")
            pass

    def close_share(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CLOSE_SHARE)
        ).click()

    def measure(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.MEASURE)
        ).click()

    def marks(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.MARKS)
        ).click()
