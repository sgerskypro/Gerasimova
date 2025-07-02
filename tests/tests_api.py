# pytest tests_api.py -v
import pytest
import allure
from pages.CompanyApi import CompanyApi

API_URL = "https://web-gate.chitai-gorod.ru/api/v1"
Bearer = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTE1MzQxMTIsImlhdCI6MTc1MTM2NjExMiwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjJhZTkxNjQwMTc3ODlhOWYxMDNhN2IyZjA0ZDljYWVhMzZmMjkxNTY1NzJjMmMzZTAwMDllYjdiM2NkN2RmZWEiLCJ0eXBlIjoxMH0.ovg-DiIbwPpfx4Z5d05bAokAzlnuTWOujA7rkuLcSq4"  # Заменить на новый токен


@allure.title("Добавить продукт в корзину")
@allure.description("Тест проверяет функциональность добавления продукта в корзину")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_add_product_to_cart():
    company_api = CompanyApi(API_URL, Bearer)

    product_data = {
        "id": 3070330,
        "adData": {
            "item_list_name": "search",
            "product_shelf": ""
        }
    }

    with allure.step("Добавление продукта в корзину"):
        response = company_api.add_product_to_cart(product_data)

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка тела ответа"):
        assert response.text == "", "Ожидался пустой ответ"


@allure.title("Получить содержимое корзины")
@allure.description("Тест проверяет функциональность получения содержимого корзины")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_retrieve_cart_contents():
    company_api = CompanyApi(API_URL, Bearer)

    with allure.step("Получение содержимого корзины"):
        response = company_api.get_cart_contents()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой ответ"


@allure.title("Очистить корзину")
@allure.description("Тест проверяет функциональность очистки корзины")
@allure.feature("Управление корзиной")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_clear_cart():
    company_api = CompanyApi(API_URL, Bearer)

    with allure.step("Очистка корзины"):
        response = company_api.clear_cart()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 204, "Ожидался статус код 204 No Content"

    with allure.step("Проверка тела ответа"):
        assert response.text == '', "Ожидалось пустое тело ответа"


@allure.title("Получить список магазинов")
@allure.description("Тест проверяет функциональность получения списка магазинов")
@allure.feature("Управление магазинами")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_get_shops_list():
    company_api = CompanyApi(API_URL, Bearer)

    with allure.step("Получение списка магазинов"):
        response = company_api.get_shops()  # Нет параметров, так как тело не нужно

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой список"


@allure.title("Получить список стран, где есть магазины")
@allure.description("Тест проверяет функциональность получения списка доступных стран")
@allure.feature("Управление странами")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.api
def test_get_countries_list():
    company_api = CompanyApi(API_URL, Bearer)

    with allure.step("Получение списка стран"):
        response = company_api.get_countries()

    with allure.step("Проверка кода состояния ответа"):
        assert response.status_code == 200, "Ожидался статус код 200 OK"

    with allure.step("Проверка, что тело ответа не пустое"):
        assert response.json(), "Ожидался непустой список"
