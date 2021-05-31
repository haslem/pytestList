from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContextPage:
    BIRD = (By.XPATH, '/html/body/div[3]/a[5]')
    PANORAMA = (By.XPATH, '/html/body/div[3]/a[4]')
    D3 = (By.XPATH, '/html/body/div[3]/a[6]')
    ROUTE_FROM = (By.XPATH, '/html/body/div[3]/a[1]')
    ROUTE_TO = (By.XPATH, '/html/body/div[3]/a[2]')
    TRIP = (By.XPATH, '/html/body/div[3]/a[3]')
    WHAT = (By.XPATH, '/html/body/div[3]/a[10]')

    def __init__(self, browser):
        self.browser = browser

    def bird_eye(self):
        elem = self.browser.find_element(*self.BIRD).click()

    def panorama(self):
        elem = self.browser.find_element(*self.PANORAMA).click()

    def d3(self):
        elem = self.browser.find_element(*self.D3).click()

    def route_to(self):
        elem = self.browser.find_element(*self.ROUTE_TO).click()

    def route_from(self):
        elem = self.browser.find_element(*self.ROUTE_FROM).click()

    def trip(self):
        elem = self.browser.find_element(*self.TRIP).click()

    def what(self):
        elem = self.browser.find_element(*self.WHAT).click()
