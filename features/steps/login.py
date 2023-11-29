from datetime import datetime

from behave import *


from features.pages.AccountPage import AccountPage
from features.pages.HomePage import HomePage
from features.pages.LoginPage import LoginPage


@given(u'I navigate to login page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.login_page = context.home_page.select_login_option()


@when(u'I enter valid email as "{email}" and password as "{password}" in the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I press on login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()


@then(u'I should get Logged in')
def step_impl(context):
    assert context.account_page.display_status_of_edit_your_account_information_option()


@when(u'I enter invalid email and valid password "{password}" in the fields')
def step_impl(context,password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M-%S")
    invalid_email = "khanahhmad002" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@then(u'Warning Message should be displayed')
def step_impl(context):
    assert context.login_page.display_status_of_warning_message("Warning: No match for E-Mail Address and/or Password.")


@when(u'I enter valid email "{email}" and invalid password "{password}" in the fields')
def step_impl(context,email,password):
    context.login_page.enter_email_address(email)
    context.login_page.enter_password(password)


@when(u'I enter invalid email and invalid password "{password}" in the fields')
def step_impl(context,password):
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M-%S")
    invalid_email = "khanahhmad002" + time_stamp + "@gmail.com"
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password(password)


@when(u'I enter nothing in the fields')
def step_impl(context):
    context.login_page.enter_email_address("")
    context.login_page.enter_password("")
