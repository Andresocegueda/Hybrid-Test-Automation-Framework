import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutOnePage
from pages.checkout_step_two_page import CheckoutTwoPage
from pages.purchase_complete_page import PurchaseCompletePage
from utils.csv_reader import get_csv_data
@pytest.mark.parametrize("user, password, debe_entrar", get_csv_data("data/users.csv"))
def test_compra_completa(driver, user, password, debe_entrar):
    enter = LoginPage(driver)
    enter.navegar()
    enter.login(user, password)
    inventory = InventoryPage(driver)
    if debe_entrar:
       assert inventory.esta_en_inventario() == True, f"No está en inventario... Hubo un error"
    else:
        assert enter.obtener_mensaje_error() == True, f"No se encuentra el mensaje... ¿Realmente inició sesión?"
        return

    inventory.order()
    inventory.add_top_products()
    inventory.carrito()

    cart_page = CartPage(driver)

    assert cart_page.esta_en_carrito() == True, f"Error: No está en el carrito..."

    cart_page.ir_a_checkout()

    checkout = CheckoutOnePage(driver)
    assert checkout.esta_en_checkout_one() == True, f"Error: No está en el checkout..."
    checkout.write_information("Andres", "Ocegueda", "12345")

    checkout2 = CheckoutTwoPage(driver)
    assert checkout2.esta_en_checkout_two() == True, f"Error: No está en el checkout 2..."
    checkout2.accept_purchase()

    complete = PurchaseCompletePage(driver)
    assert complete.is_finish() == True, f"Error: No entró a la página final..."













