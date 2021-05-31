from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class LoginPage():

    USER = (By.ID, 'login-username')
    PASSWORD = (By.ID, 'login-password')
    SIGNIN = (By.XPATH, '//button[@type="submit"]')

    LOGOUT = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div[3]/button')
    LOGOUT_MESSAGE = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div/div/h2')


    def __init__(self, browser):
        self.browser = browser

    def user(self, user: str):
        elem = self.browser.find_element(*self.USER)
        elem.send_keys(user)
        elem.send_keys(u'\ue007')

    def password(self, password: str):
        elem = self.browser.find_element(*self.PASSWORD)
        elem.send_keys(password)
        elem.send_keys(u'\ue007')

    def signin(self):
        # element = WebDriverWait(self.browser, 2).until(
        #     EC.element_to_be_clickable(self.SIGNIN)
        # )
        # for _ in range(1000000000):
        #     pass
        elem = self.browser.find_element(*self.SIGNIN).click()

