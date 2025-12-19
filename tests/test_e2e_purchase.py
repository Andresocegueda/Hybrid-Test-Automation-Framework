import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart
from pages.checkout_step_one_page import CheckoutOnePage
from pages.checkout_step_two_page import CheckoutTwoPage
from pages.purchase_complete_page import PurchaseCompletePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

users = [
    ("standard_user", "secret_sauce", True),  # Caso Positivo
    ("locked_out_user", "secret_sauce", False),  # Caso Negativo (Debe ser bloqueado)
    ("usuario_falso", "password_falso", False)  # Caso Negativo (No existe)
]

@pytest.mark.parametrize("user, password, debe_entrar", users)
def test_compra_completa(driver, user, password, debe_entrar):
    enter = LoginPage(driver)
    enter.navegar()
    enter.login(user, password)
    inventory = InventoryPage(driver)
    if debe_entrar:
        # ESCENARIO POSITIVO: Esperamos ver el carrito o productos
        # Validamos que REALMENTE entramos al sistema
        try:
            WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.ID, "inventory_container"))
            )
            assert "inventory.html" in driver.current_url
        except:
            pytest.fail(f"El usuario '{user}' debía entrar, pero el login falló.")

    else:
        # ESCENARIO NEGATIVO: Esperamos ver un mensaje de error
        # Validamos que el sistema nos detuvo
        try:
            mensaje_error = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".error-message-container"))
            )
            assert mensaje_error.is_displayed()
            assert "inventory.html" not in driver.current_url
            return
        except:
            pytest.fail(f"El usuario '{user}' debía ser bloqueado, pero entró o no salió error.")

    inventory.order()
    inventory.add_top_products()
    inventory.carrito()

    cart = Cart(driver)

    assert cart.esta_en_carrito() == True, f"Error: No está en el carrito..."

    cart.ir_a_checkout()

    checkout = CheckoutOnePage(driver)
    assert checkout.esta_en_checkout_one() == True, f"Error: No está en el checkout..."
    checkout.write_information("Andres", "Ocegueda", "12345")

    checkout2 = CheckoutTwoPage(driver)
    assert checkout2.esta_en_checkout_two() == True, f"Error: No está en el checkout 2..."
    checkout2.accept_purchase()

    complete = PurchaseCompletePage(driver)
    assert complete.is_fihish() == True, f"Error: No entró a la página final..."













