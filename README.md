 Proyecto Urban Routes - Automatización QA con Selenium

## 📌 Descripción

Este proyecto automatiza el flujo completo de solicitar un taxi en la plataforma **Urban Routes**, utilizando **Selenium** y el patrón **Page Object Model (POM)**.  
Incluye la interacción con los elementos principales de la interfaz: dirección, tarifa, número de teléfono, tarjeta de crédito, mensaje al conductor, extras y modal del conductor.

---

## 📂 Estructura del proyecto
urban_routes_project/
├── helpers.py # Funciones auxiliares (ej. retrieve_phone_code)
├── pages.py # Clase principal con localizadores y métodos de interacción
├── main.py # Ejecuta el flujo completo de pruebas
├── data.py # Datos de prueba (teléfono, dirección, tarjeta, mensaje)
├── config.py # Configuración del proyecto (https://cnt-ebf51b5b-10be-4720-9274-f52763742f1c.containerhub.tripleten-services.com?lng=es")

---

## ⚙️ Requisitos

- Python 3.13+
- Selenium 4+
- ChromeDriver (compatible con la versión de Chrome instalada)
- Pytest (opcional si se desea correr pruebas en modo unitario)

Instalación de dependencias:

```bash
pip install selenium pytest

📝 Configuración
Definir la URL del servicio en config.py:
URL_SERVICE = "https://cnt-ebf51b5b-10be-4720-9274-f52763742f1c.containerhub.tripleten-services.com?lng=es"
Definir datos de prueba en data.py:
user_phone = "+5215551234567"
user_address = "Av. Reforma 100, Ciudad de México"
card_number = "4111111111111111"
card_expiry = "12/25"
card_cvv = "123"
driver_message = "Por favor, toca el claxon al llegar"
🧩 Flujo de pruebas automatizado
El flujo completo cubre los siguientes pasos:
Configurar la dirección.
Seleccionar la tarifa Comfort.
Ingresar el número de teléfono.
Agregar una tarjeta de crédito.
Confirmar el código de teléfono mediante retrieve_phone_code().
Escribir un mensaje para el conductor.
Solicitar manta y pañuelos.
Pedir 2 helados.
Solicitar el taxi y esperar a que aparezca la información del conductor en el modal.
🚀 Cómo ejecutar
Activar tu entorno virtual (si tienes uno):
source .venv/bin/activate   # macOS/Linux
# o
.venv\Scripts\activate      # Windows
Ejecutar el flujo de pruebas con Python:
python main.py
Salida esperada (ejemplo):
Dirección configurada ✅
Tarifa Comfort seleccionada ✅
Número de teléfono ingresado ✅
Tarjeta agregada ✅
Código de confirmación ingresado ✅
Mensaje al conductor enviado ✅
Manta y pañuelos solicitados ✅
2 helados solicitados ✅
Información del conductor visible ✅
✅ Buenas prácticas
Todos los datos de prueba están centralizados en data.py para fácil mantenimiento.
La URL del servicio se gestiona desde config.py.
La función retrieve_phone_code() permite simular la confirmación de tarjeta sin depender de SMS reales.
La validación del modal del conductor garantiza que el flujo completo se haya ejecutado correctamente.
⚠️ Nota
El proyecto utiliza Selenium para interactuar con un servidor web. Si la URL del servicio no está disponible o cambia la estructura de la página, las pruebas pueden fallar.
Es recomendable ejecutar los tests en un entorno de pruebas controlado.
