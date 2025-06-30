from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class ResultPage:
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы результатов.

        :param driver: Объект WebDriver для взаимодействия с браузером.
        """
        self._driver: WebDriver = driver

    @allure.step("Получить текст корзины")
    def get_cart_text(self) -> str:
        """
        Получить текст заголовка страницы корзины.

        :return: Текст заголовка корзины.
        """
        cart_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return cart_text.text

    @allure.step("Получить текст акций")
    def get_promotions_text(self) -> str:
        """
        Получить текст заголовка страницы акций.

        :return: Текст заголовка акций.
        """
        promotions_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return promotions_text.text

    @allure.step("Получить текст распродажи")
    def get_sales_text(self) -> str:
        """
        Получить текст заголовка страницы распродаж.

        :return: Текст заголовка распродаж.
        """
        sales_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return sales_text.text

    @allure.step("Получить текст магазинов")
    def get_shops_text(self) -> str:
        """
        Получить текст заголовка страницы магазинов.

        :return: Текст заголовка магазинов.
        """
        shops_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return shops_text.text

    @allure.step("Получить текст журнала")
    def get_articles_text(self) -> str:
        """
        Получить текст заголовка страницы журнала.

        :return: Текст заголовка журнала.
        """
        articles_text = WebDriverWait(self._driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "h1"))
        )
        return articles_text.text

    @allure.step("Получить заголовок первой книги")
    def get_book_title(self) -> str:
        """
        Получить заголовок книги по заданному href и title.

        :return: Текст заголовка книги.
        """
        book_element = WebDriverWait(self._driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH,
                 '//*[@id="__layout"]/div/div[3]/div[1]/div/div/div[1]/section/section/div/article[1]/div[2]/a/div/div[1]')
            )
        )
        return book_element.text
