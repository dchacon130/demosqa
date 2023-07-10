from behave import *
from pages.checkbox_page import CheckboxPage

@given(u'the user opens the webpage "{url}"')
def step_open_url(context, url):
    checkbox = CheckboxPage(context.browser)
    assert checkbox.open_web_page(url)

@When(u'the user selects all checkboxes')
def step_select_all_checkboxes(context):
    checkbox = CheckboxPage(context.browser)
    assert checkbox.select_all_checkboxes()

@Then(u'all checkboxes should be selected')
def step_checkboxes_selected(context):
    checkbox = CheckboxPage(context.browser)
    assert checkbox.validate_checkboxes_selected()