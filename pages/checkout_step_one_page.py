from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutOnePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.title = (By.XPATH, "//span[@class='title'][contains(.,'Checkout: Your Information')]")
        self.input_first_name = (By.XPATH, "//input[contains(@id,'first-name')]")
        self.input_last_name = (By.XPATH, "//input[contains(@id,'last-name')]")
        self.input_zip = (By.XPATH, "//input[contains(@id,'postal-code')]")

    def esta_en_checkout_one(self):
        try:
            self.wait.until(EC.url_contains("checkout-step-one"))
            return True
        except:
            return False

    def write_information(self, firstname, lastname, code):
        insertfirstname = self.wait.until(EC.element_to_be_clickable(self.input_first_name))
        insertfirstname.send_keys(firstname)
        insertlastname = self.wait.until(EC.element_to_be_clickable(self.input_last_name))
        insertlastname.send_keys(lastname)
        insertzip = self.wait.until(EC.element_to_be_clickable(self.input_zip))
        insertzip.send_keys(code)


        boton = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[contains(@id,'continue')]")))
        self.driver.execute_script("arguments[0].click();", boton)