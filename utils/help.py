import csv
import pyperclip
from login_page import LoginPage

from pages.tools import Tools


def time_out():
    for i in range(100000000):
        pass

def time_out_1():
    for i in range(10000000):
        pass


def hello():
    print("Hello")


def link_to_file(link_name: str):
    print("Link to file")
    print(pyperclip.paste())

    with open('links.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        row = [link_name, f'{pyperclip.paste()}']
        writer.writerow(row)
    csvFile.close()


def is_element():
    pass


def element_x(elem):
    return elem.location['x']


def element_y(elem):
    return elem.location['y']


def element_width(elem):
    return elem.size['width']


def element_height(elem):
    return elem.size['height']


def share(browser):
    tools = Tools(browser)
    tools.share()
    tools.copy_link()
    tools.close_share()


def share_poi_detail(browser):
    tools = Tools(browser)
    tools.share_on()
    tools.copy_link()
    tools.close_share()


def login(browser):
    handle = browser.window_handles
    browser.switch_to.window(handle[1])

    login = LoginPage(browser)
    login.user("mapytesting10")
    login.password("testingmapy")
