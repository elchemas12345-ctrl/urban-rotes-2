# Urban Routes - Pruebas Automatizadas 

Este proyecto automatiza el flujo completo de pedir un taxi en **Urban Routes**.

---

## 📂 Estructura del proyecto

urban_routes_project/
│
├─ config/ # Configuración de URLs y headers
│ └─ settings.py
│
├─ data/ # Datos de prueba
│ └─ data.py
│
├─ pages/ # Clases de página (UrbanRoutesPage)
│ └─ urban_routes_page.py
│
├─ tests/ # Pruebas automatizadas
│ └─ test_order_taxi.py
│
└─ README.md

---

## 🔹 Requisitos

- Python 3.10+  
- [Selenium](https://pypi.org/project/selenium/) (`pip install selenium`)  
- Navegador Chrome o Firefox y su correspondiente driver (`chromedriver` o `geckodriver`)  
- pytest (`pip install pytest`)  

Opcional:
- Función `retrieve_phone_code()` incluida en el repositorio para interceptar el código de confirmación de la tarjeta.

---

## 🔹 Cómo ejecutar la prueba

1. Clona el repositorio:

```bash
git clone <URL_REPOSITORIO>
cd urban_routes_project
pip install selenium pytest
pytest tests/test_order_taxi.py -s
🔹 Flujo de prueba automatizado
Configura la dirección de recogida.
Selecciona la tarifa Comfort.
Ingresa el número de teléfono del usuario.
Agrega una tarjeta de crédito:
Ingresa número, fecha de expiración y CVV.
Simula cambio de enfoque para habilitar el botón de agregar tarjeta.
Confirma el código de teléfono usando retrieve_phone_code().
Envía un mensaje para el conductor.
Solicita extras: manta, pañuelos y 2 helados.
Pide un taxi.
Espera a que aparezca el modal con información del conductor.
🔹 Notas importantes
El botón de agregar tarjeta se habilita después de desenfocar el campo CVV.
La función retrieve_phone_code() se usa para obtener el código de confirmación de la tarjeta automáticamente.
Se utilizan esperas explícitas (WebDriverWait) para garantizar que los elementos estén visibles y clicables antes de interactuar.
🔹 Extensiones futuras
Validar que el modal del conductor muestre datos correctos (nombre, placa, modelo del taxi).
Manejar diferentes tipos de tarifas y extras.
Integrar reportes automáticos de ejecución de pruebas.
Este README sirve como guía completa de cómo funciona la prueba automatizada de Urban Routes y cómo ejecutarla.
