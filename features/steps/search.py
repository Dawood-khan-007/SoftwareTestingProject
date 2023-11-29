from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from features.pages.HomePage import HomePage
from features.pages.SearchPage import SearchPage


@given(u'I got navigated to Home Page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    assert context.home_page.check_homepage_title.__eq__("Your Store")


@when(u'I enter valid product "{product}" into he search box field')
def step_impl(context,product):
    context.home_page.enter_product_into_search_box_field(product)


@when(u'I click on Search Button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_buton()


@then(u'Valid product should get displayed in the search results')
def step_impl(context):
    assert context.search_page.display_status_of_product()


@when(u'I enter invalid product "{product}" into the search box field')
def step_impl(context,product):
    context.home_page.enter_product_into_search_box_field(product)


@then(u'Message should be displayed in Search Results')
def step_impl(context):
    assert context.search_page.display_status_of_message("There is no product that matches the search criteria.")


@when(u'I enter nothing into he search box field')
def step_impl(context):
    context.home_page.enter_product_into_search_box_field("")
