from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
            full_name_field = self.driver.find_element(by=By.ID, value='userName')
            full_name_field.send_keys(name)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_name_error.png')
            return False
    
    def enter_full_email(self, email):
        try:
            full_email_field = self.driver.find_element(by=By.ID, value='userEmail')
            full_email_field.send_keys(email)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_email_error.png')
            return False
        
    def enter_full_current_address(self, current_address):
        try:
            full_current_address_field = self.driver.find_element(by=By.ID, value='currentAddress')
            full_current_address_field.send_keys(current_address)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_current_address_error.png')
            return False
    
    def enter_full_permanent_address(self, permanent_address):
        try:
            full_permanent_address_field = self.driver.find_element(by=By.ID, value='permanentAddress')
            full_permanent_address_field.send_keys(permanent_address)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_full_permanent_address_error.png')
            return False
        
    def click_submit_button(self):
        try:
            submit_button = self.driver.find_element(by=By.ID, value='submit')
            self.driver.save_screenshot('../screenshots/click_submit_button.png')
            submit_button.click()
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/click_submit_button_error.png')
            return False
        
    def get_output_div(self):
        try:
            output_div = self.driver.find_element(by=By.ID, value='output')
            if output_div:
                output_name = self.driver.find_element(by=By.ID, value='name').text
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
            full_email_field = self.driver.find_element(by=By.ID, value='userEmail')
            full_email_field.send_keys(email)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/enter_invalid_email_error.png')
            return False
        
    def get_red_color_email(self):
        try:
            email_field_color = self.driver.find_element(by=By.CSS_SELECTOR, value='.field-error')
            valor_border = email_field_color.value_of_css_property('border')
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