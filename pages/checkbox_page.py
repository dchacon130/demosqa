from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckboxPage:
    def __init__(self, driver) -> None:
        self.driver = driver

    def open_web_page(self, url):
        try:
            self.driver.maximize_window()
            self.driver.get(url)
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/open_web_page_checkbox_error.png')

    def select_all_checkboxes(self):
        try:
            select_checkbox = self.driver.find_element(by=By.CLASS_NAME, value="rct-icon-uncheck")
            select_checkbox.click()
            expand_arrows = self.driver.find_element(by=By.CLASS_NAME, value="rct-icon-expand-close")
            expand_arrows.click()
            return True
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/select_all_checkboxes_error.png')

    def validate_checkboxes_selected(self):
        try:
            result = self.driver.find_element(by=By.ID, value='result')
            if result:
                self.driver.save_screenshot('../screenshots/validate_checkboxes_selected.png')
                return True
            else:
                return False
        except Exception as ex:
            print('Error was found: ', ex)
            self.driver.save_screenshot('../screenshots/validate_checkboxes_selected_error.png')
        finally:
            self.driver.quit()