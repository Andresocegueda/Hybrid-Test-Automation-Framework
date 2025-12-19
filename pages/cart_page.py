from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.title = (By.XPATH, "//span[@class='title'][contains(.,'Your Cart')]")

    def esta_en_carrito(self):
        try:
            self.wait.until(EC.url_contains("cart"))
            return True
        except:
            return False

    def ir_a_checkout(self):
        button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@id,'checkout')]")))
        self.driver.execute_script("arguments[0].click();", button)

