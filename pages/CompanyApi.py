import requests
from requests import Response


class CompanyApi:
    def __init__(self, url: str, token: str):
        """
        Инициализация класса для работы с API компании.

        :param url: URL для доступа к API.
        :param token: Токен для аутентификации.
        """
        self.url = url        
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "user-agent": "Mozilla/5.0 "
            "(Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/137.0.0.0 Mobile Safari/537.36"
        }

    def add_product_to_cart(self, product_data: dict) -> Response:
        """
        Добавляет продукт в корзину.

        :param product_data: Данные о продукте, которые нужно добавить в корзину.
        :return: Объект Response от API с результатом операции.
        """
        resp = requests.post(self.url + '/cart/product', json=product_data,
                             headers=self.headers)
        return resp

    def get_cart_contents(self) -> Response:
        """
        Получает содержимое корзины.

        :return: Объект Response от API с содержимым корзины.
        """
        resp = requests.get(self.url + '/cart', headers=self.headers)
        return resp  # Возвращаем объект Response

    def clear_cart(self) -> Response:
        """
        Очищает корзину.

        :return: Объект Response от API с результатом операции.
        """
        resp = requests.delete(self.url + '/cart', headers=self.headers)
        return resp  # Возвращаем объект Response

    def get_shops(self, params: dict = None) -> Response:
        """
        Получает список магазинов.

        :param params: (опционально) Параметры запроса.
        :return: Объект Response от API с результатом запроса.
        """
        resp = requests.get(self.url + '/shops-cities', params=params,
                            headers=self.headers)
        return resp  # Возвращаем объект Response

    def get_countries(self) -> Response:
        """
        Получает список доступных стран.

        :return: Объект Response от API с результатом запроса.
        """
        resp = requests.get(self.url + '/countries', headers=self.headers)
        return resp  # Возвращаем объект Response
