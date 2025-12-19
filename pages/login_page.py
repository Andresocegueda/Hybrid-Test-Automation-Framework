from pygments.lexers import q
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.url = "https://www.saucedemo.com/"

        self.input_user = (By.ID, "user-name")
        self.input_pass = (By.ID, "password")
        self.btn_login = (By.ID, "login-button")

    def navegar(self):
        self.driver.get(self.url)

    def login(self, username, password):
        self.wait.until(EC.visibility_of_element_located(self.input_user)).send_keys(username)
        self.driver.find_element(*self.input_pass).send_keys(password)
        self.driver.find_element(*self.btn_login).click()


