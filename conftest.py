import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="function")
def driver(request):
    """
    Fixture exclusiva para pruebas de UI (Selenium).
    Si un test NO pide este argumento 'driver', el navegador NO se abrirá.
    Esto permite que los tests de API corran rápido sin abrir Chrome.
    """
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

    # 2. Iniciar el Driver
    service = ChromeService(ChromeDriverManager().install())

    driver = webdriver.Chrome(service=service, options=opciones)
    # Ya no hace falta maximize si usamos start-maximized, pero lo dejamos por seguridad
    driver.maximize_window()

    # IMPORTANTE: Adjuntamos el driver al nodo del test para el reporte
    request.node.driver = driver

    # 3. Entregar el driver al test
    yield driver

    # 4. Limpieza (Teardown)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Este hook genera el reporte HTML y adjunta capturas SOLO si es necesario.
    Funciona tanto para UI (con foto) como para API (sin foto).
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        if report.failed:
            # Intentamos obtener el driver del test
            driver = getattr(item, 'driver', None)

            if driver:
                # CASO 1: Es un test de UI (Selenium)
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
                # CASO 2: Es un test de API (Backend)
                # No hacemos nada, ni imprimimos error. Es normal que no haya driver.
                pass

        report.extra = extra