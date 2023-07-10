from behave import *
from pages.radio_button_pages import RadioButton


@given(u'I am on the Radio Button page "{url}"')
def step_open_demoqa(context, url):
    radiobuttons = RadioButton(context.browser)
    assert radiobuttons.open_web_page(url)

@When(u'I select the Yes radio button')
def step_select_yes_radio_button(context):
    radiobuttons = RadioButton(context.browser)
    assert radiobuttons.click_yes_button('Yes')

@Then(u'the Yes radio button is selected in the text')
def step_verify_yes_text(context):
    radiobuttons = RadioButton(context.browser)
    assert radiobuttons.step_verify_text()

@When(u'I select the Impressive radio button')
def step_select_impressive_radio_button(context):
    radiobuttons = RadioButton(context.browser)
    assert radiobuttons.select_radiobutton('Impressive')

@Then(u'the Impressive radio button is selected in the text')
def step_verify_text(context):
    radiobuttons = RadioButton(context.browser)
    assert radiobuttons.step_verify_text()