from save_page import SavePage
from planning_page import PlanningPage
from mymaps_page import MyMapsPage
from pages.tools import Tools

from utils import help

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.locators import *


class MainPage:
    LOGIN = main_page["login"]
    # LOGIN = (By.XPATH, '/html/body/div/div[2]/div[1]/div/button[3]')

    SEARCH_TAB = (By.XPATH, '/html/body/div/div[2]/div[1]/div/button[1]')
    SEARCH = (By.ID, 'input-search')
    SEARCH_RESULTS = (By.ID, 'search-results')

    PLANNING_TAB = (By.XPATH, '/html/body/div/div[2]/div[1]/div/button[2]')

    MYMAPS_TAB = (By.XPATH, '/html/body/div/div[2]/div[1]/div/button[3]')

    MAP = (By.ID, 'map')
    SAVE_MYMARKS = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/div[2]/div[1]/div[1]/button')
    QUIT_MEASURE = (By.XPATH, '//button[@class="cancel-btn"]')
    SAVE_LAST_MARK = (By.XPATH, '//li[@class="item edit-mode active"]/div[@class="view-cont"]/div[@class="buttons"]/button[@class="save-btn"]')
    LAST_MARK_NAME = (By.XPATH,
                      '//li[@class="item edit-mode active"]/div[@class="view-cont"]/input[@class="title-input"]')

    #SAVE_STAR = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[1]')
    SAVE_STAR = (By.XPATH, '//div[@title="Save"]')
    #SHARE = (By.XPATH, '/html/body/div/div[2]/div[2]/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div[2]')
    SHARE = (By.XPATH, '//div[@title="Share"]')
    SHARE_UNSAVED = (By.XPATH, '//div[@title="Share"]')

    POI_DETAIL = (By.XPATH, '//div[@id="detail"]')
    HOVER_POI_DETAIL = (By.XPATH, '//div[@class="card-body"]//span[@class="info-part"]')

    CONTEXT_MENU = (By.XPATH, '//div[@class="context-menu"]')

    TOOLS = (By.XPATH, '//button[@class="icon tools"]')
    URL = "https://en.mapy.cz/zakladni?x=14.4030680&y=50.0717916&z=16"
    URL_9 = "https://en.mapy.cz/zakladni?x=14.4030680&y=50.0717916&z=9"

    PROFILE = (By.XPATH, '//button[@class="icon profile"]')

    ZOOM_IN = (By.XPATH, '//button[@title="Zoom in"]')
    ZOOM_OUT = (By.XPATH, '//button[@title="Zoom out"]')

    PANORAMA = (By.XPATH, '//button[@title="Panorama"]')
    D3 = (By.XPATH, '//button[@title="3D view"]')
    D3_COMPAS = (By.XPATH, '//div[@class="basic-compass noprint"]')

    CHANGE_MAP = (By.XPATH, '//button[@title="Choose another map"]')
    AERIAL = (By.XPATH, '//li[@class="letecka"]')
    AERIAL_MAP_BUTTON = (By.XPATH, '//button[@class="Aerial Map"]')
    HISTORIC = (By.XPATH, '//li[@class="19stoleti"]')
    TRAFFIC = (By.XPATH, '//li[@class="dopravni"]')

    # URL = "https://en.mapy.test.dszn.cz/zakladni?x=14.4030680&y=50.0717916&z=16"

    def __init__(self, browser):
        self.browser = browser
        self.browser.get(self.URL)

    def load(self):
        self.browser.get(self.URL_9)

    def login(self):
        self.browser.find_element(*self.LOGIN).click()

    def mymaps(self):
        self.browser.find_element(*self.MYMAPS_TAB).click()
        return MyMapsPage(self.browser)

    def zoom_in(self):
        el = self.browser.find_element(*self.ZOOM_IN).click()

    def zoom_in_1(self):
        el = self.browser.find_element(*self.ZOOM_IN)
        for _ in range(8):
            help.time_out_1()
            el.click()

    def zoom_out(self):
        self.browser.find_element(*self.ZOOM_OUT).click()

    def choose_aerial(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CHANGE_MAP)
        ).click()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.AERIAL)
        ).click()

    def choose_aerial_button(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.AERIAL_MAP_BUTTON)
        ).click()

    def d3(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.D3)
        ).click()
        el = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.D3_COMPAS)
        ).click()

    def choose_historic(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CHANGE_MAP)
        ).click()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.HISTORIC)
        ).click()

    def choose_traffic(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.CHANGE_MAP)
        ).click()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TRAFFIC)
        ).click()


    def search(self, search_text):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SEARCH_TAB)
        ).click()
        search_input = self.browser.find_element(*self.SEARCH)
        search_input.send_keys(search_text)
        search_input.send_keys(u'\ue007')

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SEARCH_RESULTS)
        )

    def planning_click(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PLANNING_TAB)
        ).click()

        return PlanningPage(self.browser)

    def tools(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.TOOLS)
        ).click()

        return Tools(self.browser)

    def create_measure(self):
        elem = self.browser.find_element(*self.MAP)
        ActionChains(self.browser).move_to_element_with_offset(elem, help.element_x(elem) + help.element_width(
            elem) / 2,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).perform()

        for i in range(10):
            ActionChains(self.browser).move_by_offset(-10, 0).click().perform()

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.QUIT_MEASURE)
        ).click()


    def create_marks(self):
        elem = self.browser.find_element(*self.MAP)
        ActionChains(self.browser).move_to_element_with_offset(elem, help.element_x(elem) + help.element_width(
            elem) / 2,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).perform()

        for i in range(10):
            ActionChains(self.browser).move_by_offset(-10, 0).click().perform()

        elem = self.browser.find_element(*self.LAST_MARK_NAME)
        for i in range(20):
            elem.send_keys(u'\ue003')
        elem.send_keys('Last mark')

        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE_LAST_MARK)
        ).click()





    def save_star(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SAVE_STAR)
        ).click()

        return SavePage(self.browser)

    def share_poi_detail(self):
        el = WebDriverWait(self.browser, 4).until(
            EC.visibility_of_element_located(self.SHARE)
        ).click()

        return Tools(self.browser)

    def share_unsaved_poi_detail(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.SHARE_UNSAVED)
        ).click()

        return Tools(self.browser)

    def panorama(self):
        el = WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(self.PANORAMA)
        ).click()
        help.time_out()
        elem = self.browser.find_element(*self.MAP)
        ActionChains(self.browser).move_to_element_with_offset(elem,
                                                               help.element_x(elem) + help.element_width(elem) / 2,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).click().perform()
        help.time_out()

    def poi_hover_detail(self):
        elem = self.browser.find_element(*self.MAP)
        ActionChains(self.browser).move_to_element_with_offset(elem,
                                                               help.element_x(elem) + help.element_width(elem) / 2,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).perform()

        element = WebDriverWait(self.browser, 2).until(
            EC.presence_of_element_located(self.HOVER_POI_DETAIL)
        ).click()

    def cursor_to_right_edge(self):
        elem = self.browser.find_element(*self.MAP)

        ActionChains(self.browser).move_to_element_with_offset(elem, help.element_x(elem) + help.element_width(
            elem) - 40,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).perform()

    def cursor_to_left_edge(self):
        elem = self.browser.find_element(*self.MAP)

        ActionChains(self.browser).move_to_element_with_offset(elem, help.element_x(elem) + help.element_width(
            elem) - 40,
                                                               help.element_y(elem) + help.element_height(
                                                                   elem) / 2).perform()

    def context_menu(self):
        ActionChains(self.browser).context_click().perform()

        element = WebDriverWait(self.browser, 2).until(
            EC.presence_of_element_located(self.CONTEXT_MENU)
        )

    def is_logged(self):
        try:
            element = WebDriverWait(self.browser, 1).until(
                EC.element_to_be_clickable(self.PROFILE)
            )
            return True
        except:
            #print("not logged")
            return False


