# Urban Routes - Automatización de pruebas con Selenium

Este proyecto contiene pruebas automatizadas para la funcionalidad de **Urban Routes**, incluyendo la selección de tarifa, ingreso de dirección, número de teléfono, tarjetas de crédito, extras y la validación de información del conductor.

---

## 📂 Estructura del proyecto
rban_routes_project/
│
├─ config.py # Configuración general (URL base, headers, etc.)
├─ data.py # Datos de prueba (teléfono, dirección, tarjeta, mensajes)
├─ helpers.py # Funciones auxiliares (ejemplo: retrieve_phone_code)
├─ pages.py # Clase UrbanRoutesPage: localizadores y métodos de interacción
├─ main.py # Ejecución de pruebas completas
└─ tests/ # Carpeta que contiene las pruebas automatizadas
└─ test_taxi_flow.py

---

## 🛠️ Requisitos

- Python 3.13+
- Selenium
- WebDriver para Chrome (Chromedriver)
- Pytest (para ejecutar pruebas)

Instalación de dependencias:

```bash
pip install selenium pytest

---
🧪 Ejecución de pruebas
1️⃣ Ejecutar todas las pruebas con Pytest
pytest -v tests/
2️⃣ Ejecutar pruebas desde main.py (flujo completo)
python main.py
Esto simula todo el proceso de pedir un taxi paso a paso, mostrando mensajes en consola al completar cada acción.

🔹 Flujo de pruebas cubierto
Configurar dirección.
Seleccionar tarifa Comfort.
Rellenar número de teléfono.
Agregar tarjeta de crédito (incluye confirmación de código).
Escribir un mensaje para el conductor.
Pedir manta y pañuelos.
Pedir 2 helados.
Solicitar taxi y esperar información del conductor.
💡 Notas
La función retrieve_phone_code() se encuentra en helpers.py y ya devuelve automáticamente el código de confirmación, no es necesario modificarla.
Todas las pruebas están diseñadas para ejecutarse en un entorno real con el servicio activo.
Se recomienda tener la ventana del navegador maximizada para evitar problemas con elementos invisibles al ejecutar Selenium.




