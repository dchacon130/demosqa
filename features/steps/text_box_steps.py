from behave import *
from pages.text_box_pages import TextBoxPages


@given(u'I am on the "{url}" page')
def step_open_demoqa(context, url):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.open_web_page(url)


@when(u'I enter "{name}" in the "Full Name" field')
def step_enter_name(context, name):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.enter_full_name(name), 'Error enter the Name in the field Full Name.'


@when(u'I enter "{email}" in the "Email" field')
def step_enter_email(context, email):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.enter_full_email(email), 'Error enter the Email in the field Email'


@when(u'I enter "{current_address}" in the "Current Address" field')
def step_enter_current_address(context, current_address):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.enter_full_current_address(current_address), ' Error enter the Current Address in the field Current Address'


@when(u'I enter "{permanent_address}" in the "Permanent Address" field')
def step_enter_permanent_address(context, permanent_address):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.enter_full_permanent_address(permanent_address), 'Error enter the Permanent Address in the field Permanent Address'


@when(u'I click the "Submit" button')
def step_click_submit(context):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.click_submit_button(), 'Error clicking the submit button'


@then(u'I see the information at the bottom of the form')
def step_see_information(context):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.get_output_div(), 'Error in the output div'


@when(u'I enter an invalid email format (e.g., "{invalid_email}") in the "Email" field')
def step_enter_invalid_email(context, invalid_email):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.enter_invalid_email(invalid_email), 'Error typing the invalid email'


@Then(u'I see a red color in the "Email" field')
def step_email_error(context):
    textbox_pages = TextBoxPages(context.browser)
    assert textbox_pages.get_red_color_email(), 'Error when try to get the color Red in the Email field'