# main.py
from pages import UrbanRoutesPage
from data import user_phone, user_address, card_number, card_expiry, card_cvv, driver_message
from helpers import retrieve_phone_code
from selenium import webdriver

from config import BASE_URL

def run_tests():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://cnt-ebf51b5b-10be-4720-9274-f52763742f1c.containerhub.tripleten-services.com?lng=es")
    page = UrbanRoutesPage(driver)

    # 1️⃣ Configurar dirección
    page.set_address(user_address)
    print("Dirección configurada ✅")

    # 2️⃣ Seleccionar tarifa Comfort
    page.select_comfort_tariff()
    print("Tarifa Comfort seleccionada ✅")

    # 3️⃣ Rellenar teléfono
    page.enter_phone_number(user_phone)
    print("Número de teléfono ingresado ✅")

    # 4️⃣ Agregar tarjeta
    page.add_credit_card(card_number, card_expiry, card_cvv)
    print("Tarjeta agregada ✅")

    # 5️⃣ Confirmar código de teléfono
    code = retrieve_phone_code()
    page.confirm_phone_code(code)
    print("Código de confirmación ingresado ✅")

    # 6️⃣ Escribir mensaje al conductor
    page.write_message(driver_message)
    print("Mensaje al conductor enviado ✅")

    # 7️⃣ Pedir manta y pañuelos
    page.request_extras(blanket=True, tissues=True)
    print("Manta y pañuelos solicitados ✅")

    # 8️⃣ Pedir 2 helados
    page.request_extras(ice_cream_qty=2)
    print("2 helados solicitados ✅")

    # 9️⃣ Solicitar taxi
    page.request_taxi()
    page.wait_for_driver_info()
    print("Información del conductor visible ✅")

    driver.quit()

if __name__ == "__main__":
    run_tests()
