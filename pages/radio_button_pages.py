from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.radiobutton_locators import RadioButtonLocators

class RadioButton:
    def __init__(self, driver):
        self.driver = driver
        rbl = RadioButtonLocators()
        self.radio_buttons_section = (By.XPATH, rbl.locator_rb_section)

    def open_web_page(self, url):
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            return True
        except Exception as ex:
            print('Error: ', ex)
            self.driver.save_screenshot('../screenshots/open_web_page_error.png')
            return False
        
    def click_yes_button(self):
        rbl = RadioButtonLocators()
        wait = WebDriverWait(self.driver, 10)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, rbl.locator_yes_button)))
        yes_button.click()

    def select_radiobutton(self, text):
        try:
            print('Value: ', text)
            rbl = RadioButtonLocators()
            if text == 'Yes':
                wait = WebDriverWait(self.driver, 10)
                yes_click = wait.until(EC.element_to_be_clickable((By.XPATH, rbl.locator_yes_click)))
                yes_click.click()
                return True
            elif text == 'Impressive':
                wait = WebDriverWait(self.driver, 10)
                impressive_click = wait.until(EC.element_to_be_clickable((By.XPATH, rbl.locator_impressive_click)))
                impressive_click.click()
                return True
            else:
                return False
        except Exception as ex:
            print('Error: ', ex)
            self.driver.save_screenshot('../screenshots/select_radiobutton_error.png')
            return False
        
    def step_verify_text(self):
        try:
            rbl = RadioButtonLocators()
            self.driver.switch_to.default_content()
            yes_text = self.driver.find_element(by=By.CLASS_NAME, value=rbl.locator_yes_text)
            print('Text Value: ', yes_text.text)
            if yes_text.text == 'Yes':
                self.driver.save_screenshot('../screenshots/step_verify_text_yes.png')
                return True
            elif yes_text.text == 'Impressive':
                self.driver.save_screenshot('../screenshots/step_verify_text_impressive.png')
                return True
        except Exception as ex:
            print('Error: ', ex)
            self.driver.save_screenshot('../screenshots/step_verify_text_error.png')
            return False
        finally:
            self.driver.quit()