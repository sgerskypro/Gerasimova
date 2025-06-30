from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class MainPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация главной страницы.

        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self._driver: WebDriver = driver
        self._driver.get("https://www.chitai-gorod.ru/")
        self._driver.implicitly_wait(5)
        self._driver.maximize_window()

    @allure.step("Открыть корзину")
    def open_cart(self) -> None:
        """
        Кликнуть на кнопку "Корзина".

        :return: None
        """
        cart_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
        )
        cart_button.click()

    @allure.step("Открыть страницу акций")
    def open_promotions(self) -> None:
        """
        Кликнуть на кнопку "Акции".

        :return: None
        """
        promotions_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/promotions"]'))
        )
        promotions_button.click()

    @allure.step("Открыть страницу распродаж")
    def open_sales(self) -> None:
        """
        Кликнуть на кнопку "Распродажа".

        :return: None
        """
        sales_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/sales"]'))
        )
        sales_button.click()

    @allure.step("Открыть страницу магазинов")
    def open_shops(self) -> None:
        """
        Кликнуть на кнопку "Магазины".

        :return: None
        """
        shops_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/shops"]'))
        )
        shops_button.click()

    @allure.step("Открыть журнал")
    def open_articles(self) -> None:
        """
        Кликнуть на кнопку "Читай журнал".

        :return: None
        """
        articles_button = WebDriverWait(self._driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/articles"]'))
        )
        articles_button.click()

    @allure.step("Найти книгу")
    def find_books(self, value: str):
        self._driver.find_element(By.CSS_SELECTOR, "input.header-search__input").send_keys(value + Keys.RETURN)


