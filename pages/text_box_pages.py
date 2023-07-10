from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.textbox_locators import TextBoxLocators

class TextBoxPages:
    def __init__(self,driver) -> None:
        self.driver = driver
              

    def open_web_page(self, url):
        try:
            self.driver.maximize_window() 
            self.driver.get(url)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/open_web_page_error.png')
            return False

    def enter_full_name(self, name):
        try:
            tbl = TextBoxLocators()
            full_name_field = self.driver.find_element(by=By.ID, value=tbl.locator_full_name_field)
            full_name_field.send_keys(name)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_name_error.png')
            return False
    
    def enter_full_email(self, email):
        try:
            tbl = TextBoxLocators()
            full_email_field = self.driver.find_element(by=By.ID, value=tbl.locator_full_email_field)
            full_email_field.send_keys(email)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_email_error.png')
            return False
        
    def enter_full_current_address(self, current_address):
        try:
            tbl = TextBoxLocators()
            full_current_address_field = self.driver.find_element(by=By.ID, value=tbl.locator_full_current_address_field)
            full_current_address_field.send_keys(current_address)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_current_address_error.png')
            return False
    
    def enter_full_permanent_address(self, permanent_address):
        try:
            tbl = TextBoxLocators()
            full_permanent_address_field = self.driver.find_element(by=By.ID, value=tbl.locator_full_permanent_address_field)
            full_permanent_address_field.send_keys(permanent_address)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_permanent_address_error.png')
            return False
        
    def click_submit_button(self):
        try:
            tbl = TextBoxLocators()
            submit_button = self.driver.find_element(by=By.ID, value=tbl.locator_submit_button)
            self.driver.save_screenshot('../screenshots/click_submit_button.png')
            submit_button.click()
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/click_submit_button_error.png')
            return False
        
    def get_output_div(self):
        try:
            tbl = TextBoxLocators()
            output_div = self.driver.find_element(by=By.ID, value=tbl.locator_output_div)
            if output_div:
                output_name = self.driver.find_element(by=By.ID, value=tbl.locator_output_name).text
                print('output_name: ', output_name)
                self.driver.save_screenshot('../screenshots/get_output_div.png')
                return True
            else:
                return False
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/get_output_div_error.png')
            return False
        
    def enter_invalid_email(self, email):
        try:
            tbl = TextBoxLocators()
            full_email_field = self.driver.find_element(by=By.ID, value=tbl.locator_full_email_field)
            full_email_field.send_keys(email)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_invalid_email_error.png')
            return False
        
    def get_red_color_email(self):
        try:
            tbl = TextBoxLocators()
            email_field_color = self.driver.find_element(by=By.CSS_SELECTOR, value=tbl.locator_email_field_color)
            valor_border = email_field_color.value_of_css_property(tbl.locator_valor_border)
            print('valor_border: ', valor_border)
            if '1px solid rgb(255, 0, 0)' == valor_border:
                self.driver.save_screenshot('../screenshots/get_red_color_email.png')
                return True
            else:
                return False
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/get_red_color_email_error.png')
            return False
        finally:
            self.driver.quit()