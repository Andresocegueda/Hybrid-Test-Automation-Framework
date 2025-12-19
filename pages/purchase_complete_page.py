from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PurchaseCompletePage:
    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(driver,10)
        self.message = (By.XPATH, "//h2[@class='complete-header'][contains(.,'Thank you for your order!')]")

    def is_fihish(self):
        try:
            self.wait.until(EC.url_contains("checkout-complete"))
            return True
        except:
            return False

