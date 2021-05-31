from context_page import ContextPage
from planning_page import PlanningPage

from utils import help

from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_login(browser):
    main_page = MainPage(browser)
    main_page.login()

    handle = browser.window_handles
    browser.switch_to.window(handle[1])

    login = LoginPage(browser)
    login.user("mapytesting10")
    login.password("testingmapy")

    browser.switch_to.window(handle[0])


def test_search(browser):
    main_page = MainPage(browser)
    main_page.search("golf")


def test_measure(browser):
    mainpage = MainPage(browser)
    toolspage = mainpage.tools()
    toolspage.measure()

    mainpage.create_measure()

    mainpage.save_star()
    help.time_out()

    # save = SavePage(browser)
    # save.change_name("My measure")
    # save.save()
    #
    # browser.refresh()
    # mainpage.my_maps()
    #
    # utils.delay()
    #
    # assert "My measure" in mymaps.get_last_item()
    #
    # mymaps.delete_item()

def test_delete_all_poi(browser):
    test_login(browser)

    main_page = MainPage(browser)
    mymaps_page = main_page.mymaps()

    mymaps_page.delete_all_elements()


def test_delete_all_poi(browser):
    test_login(browser)

    main_page = MainPage(browser)
    help.time_out_1()
    mymaps_page = main_page.mymaps()

    mymaps_page.delete_all_elements()

def test_delete_all_folders(browser):
    test_login(browser)

    main_page = MainPage(browser)
    mymaps_page = main_page.mymaps()

    mymaps_page.delete_all_folders()

def test_create_folder(browser):
    test_login(browser)

    main_page = MainPage(browser)
    mymaps_page = main_page.mymaps()

    mymaps_page.create_folder("New folder")

def test_panorama(browser):

    main_page = MainPage(browser)
    main_page.load()
    main_page.panorama()

    help.time_out()


def test_poi_to_folder(browser):
    test_create_folder(browser)


    #poi to folder
    main_page = MainPage(browser)
    main_page.poi_hover_detail()

    # save change name
    save_page = main_page.save_star()
    save_page.change_save_name("POI renamed")
    save_page.save_to_folder("New folder")
    save_page.save()
    save_page.close_save_toast()


    #marks to folder
    mainpage = MainPage(browser)
    toolspage = mainpage.tools()
    toolspage.marks()

    mainpage.create_marks()
    # save
    save_page = mainpage.save_star()
    help.time_out()
    save_page.save_to_folder("New folder")
    save_page.save()
    save_page.close_save_toast()




    #measure to folder
    mainpage = MainPage(browser)
    toolspage = mainpage.tools()
    toolspage.measure()

    mainpage.create_measure()

    # save
    save_page = mainpage.save_star()
    help.time_out()
    save_page.save_to_folder("New folder")
    save_page.save()
    save_page.close_save_toast()



    #coor to folder
    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.what()

    # save
    save_page = main_page.save_star()
    help.time_out()
    save_page.save_to_folder("New folder")
    save_page.save()




    #route to folder
    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Mlada Boleslav")

    if planning_page.is_route_planned():
        planning_page.walk_short()

    if planning_page.is_route_planned():
        # save
        save_page = main_page.save_star()
        help.time_out()
        save_page.save_to_folder("New folder")
        save_page.save()
        save_page.close_save_toast()



    #trip to folder
    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.trip()

    planning_page = PlanningPage(browser)
    if planning_page.is_route_planned():


        # save
        save_page = main_page.save_star()
        help.time_out()
        save_page.save_to_folder("New folder")
        save_page.save()
        save_page.close_save_toast()





