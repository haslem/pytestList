from context_page import ContextPage

from utils import help
from main_page import MainPage
from planning_page import PlanningPage

from testCases import test_my_maps


def is_logged(browser):
    main_page = MainPage(browser)
    if main_page.is_logged():
        pass
    else:
        test_my_maps.test_login(browser)

def test_login(browser):
    test_my_maps.test_login(browser)


def test_search_link(browser):
    main_page = MainPage(browser)
    main_page.search("golf")

    main_page.tools()
    help.share(browser)
    help.link_to_file("search")


def test_measure_link(browser):
    #test_my_maps.test_login(browser)

    mainpage = MainPage(browser)
    toolspage = mainpage.tools()
    toolspage.measure()

    mainpage.create_measure()
    mainpage.share_unsaved_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved measure")


    #save
    save_page = mainpage.save_star()
    save_page.save()
    save_page.close_save_toast()
    mainpage.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved measure")


def test_marks_link(browser):
    #test_my_maps.test_login(browser)

    mainpage = MainPage(browser)
    toolspage = mainpage.tools()
    toolspage.marks()

    mainpage.create_marks()
    mainpage.share_unsaved_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved marks")


    #save
    save_page = mainpage.save_star()
    save_page.save()
    save_page.close_save_toast()
    mainpage.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved marks")


def test_poi_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.poi_hover_detail()


    main_page.share_unsaved_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved poi")


    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved poi")


def test_poi_renamed_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.poi_hover_detail()

    # save change name
    save_page = main_page.save_star()
    save_page.change_save_name("POI renamed")
    help.time_out()
    save_page.save()
    save_page.close_save_toast()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved poi")



# def test_poi_renamed_to_folder(browser):
#     test_my_maps.test_login(browser)
#
#     main_page = MainPage(browser)
#     main_page.poi_hover_detail()
#
#     # save change name
#     save_page = main_page.save_star()
#     save_page.change_save_name("POI renamed")
#     save_page.save_to_folder("4")
#     help.time_out()
#     save_page.save()



def test_coor_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.what()

    main_page.share_unsaved_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved coor")


    #save
    save_page = main_page.save_star()
    save_page.save()

    #save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved coor")



def test_coor_renamed_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.what()

    # save change name
    save_page = main_page.save_star()
    save_page.change_save_name("Coor renamed")
    help.time_out()
    save_page.save()
    save_page.close_save_toast()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved poi")


def test_one_point_route(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    main_page.tools()
    help.share(browser)
    help.link_to_file("one_point_route")

def test_two_point_route(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Ostrava")


    if planning_page.is_route_planned():
        main_page.share_poi_detail()
        help.share_poi_detail(browser)
        help.link_to_file("unsaved_two_point_route")

    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_two_point_route")


def test_two_point_route_1(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Mlada Boleslav")


    if planning_page.is_route_planned():
        planning_page.walk_short()

    if planning_page.is_route_planned():
        main_page.share_poi_detail()
        help.share_poi_detail(browser)
        help.link_to_file("Prague Mlada Boleslav walk short")

    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("Prague Mlada Boleslav walk short")



def test_two_point_route_several_country(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Budapest")


    if planning_page.is_route_planned():
        main_page.share_poi_detail()
        help.share_poi_detail(browser)
        help.link_to_file("unsaved_two_point_route_several_country")


    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_two_point_route_several_country")


def test_two_point_route_avoid_country(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Budapest")


    if planning_page.is_route_planned():
        planning_page.avoid_second_country()

    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved_two_point_route_avoid_country")


    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_two_point_route_avoid_country")



def test_two_point_route_avoid_SK_no_pay_HUN(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Budapest")


    if planning_page.is_route_planned():
        planning_page.avoid_second_country()

    if planning_page.is_route_planned():
        planning_page.avoid_third_country()

    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved_route_avoid_SK_no_pay_HUN")


    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_route_avoid_SK_no_pay_HUN")



def test_two_point_route_avoid_all(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    planning_page = main_page.planning_click()
    planning_page.set_start("Prague")

    planning_page.set_start("Budapest")


    if planning_page.is_route_planned():
        planning_page.avoid_all()

    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("unsaved_two_point_route_avoid_all")


    #save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_two_point_route_avoid_all")


def test_vylet_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.trip()

    planning_page = PlanningPage(browser)
    if planning_page.is_route_planned():
        #planning_page.trip_bike()
        main_page.share_poi_detail()
        help.share_poi_detail(browser)
        help.link_to_file("unsaved_trip_foot_short")


    # save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_trip_foot_short")


def test_vylet_bike_max_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    main_page.cursor_to_right_edge()
    main_page.context_menu()

    context = ContextPage(browser)
    context.trip()

    planning_page = PlanningPage(browser)
    if planning_page.is_trip_planned():
        planning_page.trip_bike()
    if planning_page.is_trip_planned():
        planning_page.trip_max_distance()
    if planning_page.is_trip_planned():
        main_page.share_poi_detail()
        help.share_poi_detail(browser)
        help.link_to_file("unsaved_trip")

    # save
    save_page = main_page.save_star()
    save_page.save()
    save_page.close_save_toast()
    help.time_out()
    main_page.share_poi_detail()
    help.share_poi_detail(browser)
    help.link_to_file("saved_trip")


def test_base_map_link(browser):
    #test_my_maps.test_login(browser)

    main_page = MainPage(browser)
    for _ in range(15):
        main_page.zoom_in()


    main_page.tools()
    help.share(browser)
    help.link_to_file("base_map")


def test_aerial_map_link(browser):

    main_page = MainPage(browser)
    # for _ in range(15):
    #     main_page.zoom_in()

    main_page.zoom_in_1()

    help.time_out()

    main_page.choose_aerial()

    help.time_out()

    main_page.tools()
    help.share(browser)
    help.link_to_file("aerial_map")


def test_aerial_map_button_link(browser):

    main_page = MainPage(browser)
    # for _ in range(8):
    #     main_page.zoom_in()
    main_page.zoom_in_1()

    help.time_out()

    main_page.choose_aerial()

    help.time_out()

    main_page.tools()
    help.share(browser)
    help.link_to_file("aerial_map_button")


def test_historic_map_link(browser):

    main_page = MainPage(browser)

    main_page.zoom_in_1()

    help.time_out()

    main_page.choose_historic()

    help.time_out()

    main_page.tools()
    help.share(browser)
    help.link_to_file("historic_map")


def test_traffic_map_link(browser):

    main_page = MainPage(browser)

    main_page.zoom_in_1()

    help.time_out()

    main_page.choose_traffic()

    help.time_out()

    main_page.tools()
    help.share(browser)
    help.link_to_file("traffic_map")


def test_panorama_link(browser):

    main_page = MainPage(browser)
    main_page.load()
    main_page.panorama()

    help.time_out()

    main_page.tools()
    help.share(browser)
    help.link_to_file("panorama")


def test_3d_link(browser):

    main_page = MainPage(browser)
    main_page.d3()


    main_page.tools()
    help.share(browser)
    help.link_to_file("3D")


