import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="function")
def driver(request):
    # 1. Configuración de Opciones
    opciones = Options()
    opciones.add_argument("--incognito")
    opciones.add_argument("--guest")
    opciones.add_argument("--start-maximized")
    opciones.add_argument("--window-size=1920,1080")
    opciones.add_argument("--headless")  # Modo fantasma (sin ventana)

    # Preferencias para evitar popups y guardar claves
    opciones.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "safebrowsing.enabled": False
    })
    opciones.add_experimental_option("excludeSwitches", ["enable-automation"])
    opciones.add_experimental_option('useAutomationExtension', False)

    # Iniciar el Driver
    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=opciones)
    driver.maximize_window()

    request.node.driver = driver

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        if report.failed:
            driver = getattr(item, 'driver', None)

            if driver:
                print("\n📸 Fallo en UI detectado. Tomando captura de pantalla...")
                screenshot = driver.get_screenshot_as_base64()
                html = (
                    f'<details style="margin-top: 10px; border: 1px solid #ccc; padding: 5px; background: #f9f9f9;">'
                    f'  <summary style="cursor: pointer; font-weight: bold; color: #0056b3;">📸 Ver Captura de Pantalla (Clic para expandir)</summary>'
                    f'  <div style="margin-top: 10px; text-align: center;">'
                    f'    <img src="data:image/png;base64,{screenshot}" alt="screenshot" '
                    f'         style="width: 90%; max-width: 1000px; border: 1px solid #ddd; box-shadow: 2px 2px 5px rgba(0,0,0,0.2);"/>'
                    f'  </div>'
                    f'</details>'
                )
                extra.append(pytest_html.extras.html(html))
            else:
                pass

        report.extra = extra