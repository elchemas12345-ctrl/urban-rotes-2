Proyecto Urban Routes

Proyecto 8 – Creación de un kit personal

Este proyecto automatiza pruebas para la creación de un kit personal dentro de la API de Urban Grocers.
El objetivo es verificar que el sistema acepte correctamente nombres de kit con diferentes características y devuelva los códigos de respuesta esperados.

⚙️ Qué hace el proyecto

Crea un usuario nuevo y obtiene su token de autenticación (authToken).
Crea un kit personal asociado a ese usuario, enviando el token en el encabezado Authorization.
Ejecuta pruebas automatizadas con Pytest para validar:
Límites de longitud del nombre (1, 511, 0, 512 caracteres)
Caracteres especiales, espacios y números
Casos donde falta el parámetro o se pasa con un tipo incorrecto
Comprueba que los códigos de respuesta sean correctos:
201 → creación exitosa
400 → error por datos inválidos
🚀 Requisitos previos

Python 3.9+
PyCharm o cualquier editor
Acceso a la API (URL de servicio)
🛠️ Instalación y configuración

Clona el repositorio:
git clone https://github.com//Users/charlo.00/qa-project-Urban-Grocers-app-es
cd proyecto_7_kit
Crea un entorno virtual

python3 -m venv .venv source .venv/bin/activate # macOS / Linux

Instala dependencias

pytest -v

Ejecutar pruebas

pytest -v tests/create_kit_name_kit_test.py

pytest -v

Estructura del proyecto

/Users/charlo.00/qa-project-Urban-Grocers-app-es ├─ configuration.py # Configuración: URLs y headers ├─ data.py # Datos de prueba (cuerpos de las requests) ├─ sender_stand_request.py # Funciones para enviar requests ├─ tests/ │ └─ create_kit_name_kit_test.py # Pruebas con pytest

Lista de comprobación

Nombre con 1 carácter → ✅ 201 Nombre con 511 caracteres → ✅ 201 Nombre vacío → ❌ 400 Nombre con 512 caracteres → ❌ 400 Caracteres especiales permitidos → ✅ 201 Nombre con espacios → ✅ 201 Nombre con números → ✅ 201 Parámetro name faltante → ❌ 400 name con tipo numérico → ❌ 400
