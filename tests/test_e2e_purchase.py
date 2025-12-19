import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import Cart
from pages.checkout_step_one_page import CheckoutOnePage
from pages.checkout_step_two_page import CheckoutTwoPage
from pages.purchase_complete_page import PurchaseCompletePage

users = [
    ("standard_user", "secret_sauce"),
    ("visual_user", "secret_sauce")
]

@pytest.mark.parametrize("user, password", users)
def test_compra_completa(driver, user, password):
    enter = LoginPage(driver)
    enter.navegar()
    enter.login(user, password)

    inventory = InventoryPage(driver)

    assert inventory.esta_en_inventario() == True, f"Error: No se logró iniciar sesión"

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













