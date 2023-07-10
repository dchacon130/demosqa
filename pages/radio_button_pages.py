from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class RadioButton:
    def __init__(self, driver):
        self.driver = driver
        self.radio_buttons_section = (By.XPATH, "//body/div[@id='app']/div[@class='body-height']/div[@class='container playgound-body']/div[@class='row']/div[@class='col-12 mt-4 col-md-6']/div[2]")

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
        wait = WebDriverWait(self.driver, 10)
        yes_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Yes')]/preceding-sibling::input")))
        yes_button.click()

    def select_radiobutton(self, text):
        try:
            print('Value: ', text)
            if text == 'Yes':
                wait = WebDriverWait(self.driver, 10)
                yes_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Yes')]/preceding-sibling::input")))
                yes_click.click()
                return True
            elif text == 'Impressive':
                wait = WebDriverWait(self.driver, 10)
                impressive_click = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Impressive')]/preceding-sibling::input")))
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
            self.driver.switch_to.default_content()
            yes_text = self.driver.find_element(by=By.CLASS_NAME, value='text-success')
            print('Text Value: ', yes_text.text)
            if yes_text.text == 'Yes':
                self.driver.save_screenshot('../screenshots/step_verify_text_yes.png')
                return True
            elif yes_text.text == 'Impressive':
                self.driver.save_screenshot('../screenshots/step_verify_text_impressive.png')
                return True
            else:
                return False
        except Exception as ex:
            print('Error: ', ex)
            self.driver.save_screenshot('../screenshots/step_verify_text_error.png')
            return False
        finally:
            self.driver.quit()