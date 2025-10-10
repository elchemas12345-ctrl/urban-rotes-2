# tests/test_taxi_flow.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pages import UrbanRoutesPage
from helpers import retrieve_phone_code
from data import user_phone, user_address, card_number, card_expiry, card_cvv, driver_message
from selenium import webdriver
from config import BASE_URL



class TestUrbanRoutes:

    def setup_method(self):
        # Inicializa el driver de Chrome
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://cnt-ebf51b5b-10be-4720-9274-f52763742f1c.containerhub.tripleten-services.com?lng=es")
        # Instancia la clase de la página
        self.page = UrbanRoutesPage(self.driver)

    def teardown_method(self):
        # Cierra el navegador al final de cada test
        self.driver.quit()

    # 1️⃣ Configurar la dirección
    def test_set_address(self):
        self.page.set_address(user_address)
        assert self.page.is_route_set(), "❌ La dirección no se estableció correctamente."

    # 2️⃣ Seleccionar la tarifa Comfort
    def test_select_comfort(self):
        self.page.select_comfort_tariff()
        assert self.page.is_comfort_selected(), "❌ La tarifa Comfort no se seleccionó correctamente."

    # 3️⃣ Rellenar el número de teléfono
    def test_fill_phone(self):
        self.page.enter_phone_number(user_phone)
        assert self.page.is_phone_entered(), "❌ El número de teléfono no se ingresó correctamente."

    # 4️⃣ Agregar tarjeta de crédito
    def test_add_card(self):
        self.page.add_credit_card(card_number, card_expiry, card_cvv)
        assert self.page.is_card_added(), "❌ La tarjeta no se agregó correctamente."

    # 5️⃣ Confirmar código de teléfono (retrieve_phone_code)
    def test_confirm_code(self):
        code = retrieve_phone_code()
        self.page.confirm_phone_code(code)
        assert code == "0000", "❌ El código de confirmación no es válido."

    # 6️⃣ Escribir mensaje para el conductor
    def test_message_driver(self):
        self.page.write_message(driver_message)
        assert self.page.is_message_sent(), "❌ El mensaje para el conductor no se envió correctamente."

    # 7️⃣ Pedir manta y pañuelos
    def test_extras_blanket_tissues(self):
        self.page.request_extras(blanket=True, tissues=True)
        assert self.page.are_extras_selected(blanket=True, tissues=True), "❌ Los extras no se seleccionaron correctamente."

    # 8️⃣ Pedir 2 helados
    def test_extras_ice_cream(self):
        self.page.request_extras(ice_cream_qty=2)
        assert self.page.are_ice_creams_added(2), "❌ No se agregaron correctamente los helados."

    # 9️⃣ Modal del conductor
    def test_driver_modal(self):
        self.page.request_taxi()
        self.page.wait_for_driver_info()
        assert self.page.is_driver_info_visible(), "❌ No aparece la información del conductor en pantalla."
