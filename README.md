# Hybrid Test Automation Framework (UI + API)

[![Pruebas Automatizadas (CI/CD)](https://github.com/Andresocegueda/Hybrid-Test-Automation-Framework/actions/workflows/ejecucion_automatica.yml/badge.svg)](https://github.com/Andresocegueda/Hybrid-Test-Automation-Framework/actions/workflows/ejecucion_automatica.yml)

Este repositorio contiene un framework de pruebas automatizadas híbrido, diseñado para validar tanto la interfaz de usuario (Front-end) como los servicios web (Back-end) en una misma arquitectura escalable.

## 🎯 Objetivo del Proyecto
Demostrar la capacidad de construir una solución de calidad robusta que integra:
* **Pruebas UI:** Automatización de flujos "End-to-End" en *SauceDemo* (E-commerce).
* **Pruebas API:** Validación de endpoints RESTful usando *JSONPlaceholder*.
* **CI/CD:** Ejecución automática de pruebas en la nube mediante GitHub Actions.

## 🛠️ Stack Tecnológico

| Herramienta | Uso Principal |
|-------------|---------------|
| **Python** 🐍 | Lenguaje base del framework. |
| **Selenium WebDriver** | Automatización del navegador y simulacion de usuario. |
| **Requests** | Librería para peticiones HTTP rápidas y validación de API. |
| **Pytest** | Runner de pruebas, manejo de fixtures y aserciones. |
| **WebDriver Manager** | Gestión automática de drivers (Chromedriver). |
| **GitHub Actions** | Integración Continua (CI) para correr tests en cada push. |

## 📂 Estructura del Proyecto

```text
Hybrid-Test-Automation-Framework/
├── .github/workflows/  # Configuración del robot de CI/CD
├── pages/              # Page Objects (Lógica de las páginas Web - POM)
├── reportes/           # Reportes HTML generados (evidencias)
├── tests/              # Casos de prueba (Scripts)
│   ├── test_ui_login.py    # Pruebas de Interfaz (Selenium)
│   └── test_api_users.py   # Pruebas de Backend (API)
├── conftest.py         # Configuración global (Fixtures, Hooks, Drivers)
├── requirements.txt    # Dependencias del proyecto
└── README.md           # Documentación
```

## ¿Cómo ejecutar este proyecto localmente?

Si deseas correr estas pruebas en tu máquina, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone [https://github.com/Andresocegueda/Hybrid-Test-Automation-Framework.git](https://github.com/Andresocegueda/Hybrid-Test-Automation-Framework.git)
    cd Hybrid-Test-Automation-Framework
    ```

2.  **Instalar dependencias:**
    Es recomendable usar un entorno virtual.
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ejecutar las pruebas:**
    Para correr todo el set (UI + API):
    ```bash
    pytest -v
    ```

## Integración Continua (CI/CD)
Este proyecto cuenta con un pipeline configurado en **GitHub Actions**.
Cada vez que se hace un `push` a la rama principal, un servidor Ubuntu en la nube:
1.  Instala Python y las dependencias.
2.  Ejecuta todos los tests en modo **Headless** (sin interfaz gráfica).
3.  Genera un reporte de éxito o fallo.

---
**Autor:** Ramón Andrés Ocegueda Montoya
* QA Automation Engineer Student