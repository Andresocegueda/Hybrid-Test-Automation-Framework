from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTwoPage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.title = (By.XPATH, "//span[@class='title'][contains(.,'Checkout: Overview')]")

    def esta_en_checkout_two(self):
        try:
            self.wait.until(EC.url_contains("checkout-step-two"))
            return True
        except:
            return False

    def accept_purchase(self):
        boton_finish = self.wait.until(EC.presence_of_element_located((By.ID, "finish")))

        self.driver.execute_script("arguments[0].click();", boton_finish)

