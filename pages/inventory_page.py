from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.titulo_pagina = (By.XPATH, "//span[@class='title'][contains(.,'Products')]")
        self.buttons = (By.XPATH, "(//button[contains(.,'Add to cart')])")
    def esta_en_inventario(self):
        try:
            self.wait.until(EC.url_contains("inventory"))
            return True
        except:
            return False

    def order(self):
        filt = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//select[contains(@class,'product_sort_container')]")))
        filt2 = Select(filt)
        filt2.select_by_visible_text("Price (high to low)")

    def add_top_products(self):
        list_buttons = self.driver.find_elements(*self.buttons)

        if len(list_buttons) >= 2:
            list_buttons[0].click()
            list_buttons[1].click()
        else:
            print("Error")

    def carrito(self):
        boton_carrito = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping_cart_link")))

        self.driver.execute_script("arguments[0].click();", boton_carrito)






