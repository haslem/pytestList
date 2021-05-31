from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import help


class PlanningPage:
    ROUTE_ITEM = (By.XPATH, '//div[@class="cont"]/input')
    ROUTE_ITEM_TEXT = (By.XPATH, '//div[@class="cont"]/h4')
    PLANNING_TAB = (By.XPATH, '/html/body/div/div[2]/div[1]/div/button[2]')

    TOLLS = (By.XPATH, '//div[@class="toll"]')
    TOLLS_CHECKBOXES = (By.XPATH, '//li[@class="checkbox-item"]')
    TOLLS_AVOID_ALL = (By.XPATH, '//div[@class="avoid-all checkbox-item"]')

    TYPES = (By.XPATH, '//div[@class="route-buttons"]/button[@type="button"]')
    # TYPE = (By.XPATH, '//div[@class="params-select-label"]')
    TYPE = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div[1]/div[2]/div[4]/div')
    SHORT_TOURIST = (By.XPATH, '//ul[@class="params-select-popup"]/li')

    TRIP_DISTANCE = (By.XPATH, '//span[@class="circuit-bar-button"]')
    # TRIP_DISTANCE = (By.XPATH, '//*[@id="layout-body"]/div[1]/div[2]/div[1]/div/div[1]/div/span')
    TRIP_DISTANCE_PLUS = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div[1]/button[2]')
    CANCEL_TRIP = (By.XPATH, '//button[@class="cancel"]')

    ROUTE_ACTIONS = (By.XPATH, '//div[@class="route-actions"]')

    def __init__(self, browser):
        self.browser = browser

    def set_start(self, start):
        # el = WebDriverWait(self.browser, 2).until(
        #     EC.visibility_of_element_located(self.ROUTE_ITEM)
        # )

        els = self.browser.find_elements(*self.ROUTE_ITEM)

        els[0].send_keys(start)
        els[0].send_keys(u'\ue007')

        el = WebDriverWait(self.browser, 4).until(
            EC.visibility_of_all_elements_located(self.ROUTE_ITEM_TEXT)
        )

    def set_end(self, end):
        els = self.browser.find_elements(*self.ROUTE_ITEM)

        els[-1].send_keys(end)
        els[-1].send_keys(u'\ue007')

        el = WebDriverWait(self.browser, 4).until(
            EC.visibility_of_all_elements_located(self.ROUTE_ITEM_TEXT)
        )

    def is_route_planned(self):
        try:
            el = WebDriverWait(self.browser, 4).until(
                EC.visibility_of_all_elements_located(self.ROUTE_ACTIONS)
            )
            return True
        except:
            return False

    def is_trip_planned(self):
        try:
            el = WebDriverWait(self.browser, 4).until(
                EC.element_to_be_clickable(self.CANCEL_TRIP)
            )
            return True
        except:
            return False

    def avoid_second_country(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TOLLS)
        ).click()

        els = self.browser.find_elements(*self.TOLLS_CHECKBOXES)
        els[1].click()
        if self.is_route_planned():
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TOLLS)
            ).click()

    def avoid_third_country(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TOLLS)
        ).click()

        els = self.browser.find_elements(*self.TOLLS_CHECKBOXES)
        els[2].click()
        if self.is_route_planned():
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TOLLS)
            ).click()

    def avoid_all(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TOLLS)
        ).click()

        els = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TOLLS_AVOID_ALL)
        ).click()
        if self.is_route_planned():
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TOLLS)
            ).click()

    def walk_short(self):
        els = self.browser.find_elements(*self.TYPES)
        els[3].click()

        if self.is_route_planned():
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TYPE)
            ).click()

            els = self.browser.find_elements(*self.SHORT_TOURIST)
            els[0].click()

    def walk_tourist(self):
        els = self.browser.find_elements(*self.TYPES)
        els[3].click()

        if self.is_route_planned():
            el = WebDriverWait(self.browser, 2).until(
                EC.visibility_of_element_located(self.TYPE)
            ).click()

            els = self.browser.find_elements(*self.SHORT_TOURIST)
            els[1].click()

    def trip_bike(self):
        els = self.browser.find_elements(*self.TYPES)
        els[1].click()

        el = WebDriverWait(self.browser, 4).until(
            EC.visibility_of_element_located(self.TRIP_DISTANCE)
        )

        # print(help.element_x(el), "x")
        # print(help.element_y(el), "y")
        # print(help.element_width(el), "width")
        # print(help.element_height(el), "height")

        help.time_out()

    def trip_max_distance(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TRIP_DISTANCE)
        )
        el1 = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TRIP_DISTANCE_PLUS)
        )

        ActionChains(self.browser).drag_and_drop(el, el1).perform()
        #ActionChains(self.browser).move_to_element_with_offset(el1, -100, 0).click().perform()
        #ActionChains(self.browser).move_to_element_with_offset(el, 100, 10).context_click().perform()
        #ActionChains(self.browser).move_to_element(el).context_click().perform()
        # ActionChains(self.browser).drag_and_drop_by_offset(el, 1000, 1000).perform()
        # print("try max")
        #
        # help.time_out()
