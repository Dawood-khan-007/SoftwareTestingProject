from datetime import datetime

from behave import *


from features.pages.AccountSuccessPage import AccountSuccessPage
from features.pages.HomePage import HomePage
from features.pages.RegisterPage import RegisterPage


@given(u'I navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.register_page = context.home_page.select_register_option()

@when(u'I Enter Mandatory fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M-%S")
        new_email = "khanahhmad002" + time_stamp + "@gmail.com"
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])




@when(u'I select privacy policy option')
def step_impl(context):
    context.register_page.select_privacy_policy()

@when(u'I press on Continue button')
def step_impl(context):
   context.account_success_page =  context.register_page.click_on_continue_button()



@then(u'Account should be created')
def step_impl(context):

    assert context.account_success_page.display_status_of_account_created_heading("Your Account Has Been Created!")


@when(u'I Enter details in All fields')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M-%S")
        new_email = "khanahhmad002" + time_stamp + "@gmail.com"
        context.register_page.enter_email(new_email)
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_radio_option()


@when(u'I Enter details in All fields except email field')
def step_impl(context):
    for row in context.table:
        context.register_page.enter_first_name(row["first_name"])
        context.register_page.enter_last_name(row["last_name"])
        context.register_page.enter_telephone(row["telephone"])
        context.register_page.enter_password(row["password"])
        context.register_page.enter_password_confirm(row["password"])
        context.register_page.select_yes_radio_option()

@when(u'I enter already registered email in email field')
def step_impl(context):
    context.register_page.enter_email("khanahhmad002@gmail.com")


@then(u'Proper Warning message should be displayed about duplicate email')
def step_impl(context):
    assert context.register_page.display_status_of_duplicate_email_warning("Warning: E-Mail Address is already registered!")


@when(u'I write nothing in the fields')
def step_impl(context):
    context.register_page.enter_first_name("")
    context.register_page.enter_last_name("")
    context.register_page.enter_email("")
    context.register_page.enter_telephone("")
    context.register_page.enter_password("")
    context.register_page.enter_password_confirm("")


@then(u'Warning message should be displayed in every mandatory field')
def step_impl(context):
    expected_privacy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_error = "First Name must be between 1 and 32 characters!"
    expected_last_name_error = "Last Name must be between 1 and 32 characters!"
    expected_email_error = "E-Mail Address does not appear to be valid!"
    expected_phone_error = "Telephone must be between 3 and 32 characters!"
    expected_password_error = "Password must be between 4 and 20 characters!"
    assert context.register_page.display_status_of_all_warning_messages(expected_privacy_warning,expected_first_name_error
                                                                 ,expected_last_name_error
                                                                 ,expected_email_error
                                                                 ,expected_phone_error
                                                                 ,expected_password_error)
