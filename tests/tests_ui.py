# pytest tests_ui.py  -v
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from locators.locators import TestData, MainPageLocators, SearchPageLocators, CartPageLocators # Импорт локаторов


class TestSearch:
    def test_search_book(self, driver, wait):
        # Тест Поиск книги ПОЗИТИВНЫЙ
        search_input = wait.until(
            EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT)
        )
        search_input.click()
        search_input.send_keys(TestData.BOOK)

        # Клик  на нопку поиска
        search_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        search_button.click()
        
    def test_add_books(self, driver, wait):
        """Тест добавления книг в корзину с проверками. ПОЗИТИВНЫЙ"""
        # Ожидаем загрузки карточек товаров
        book_cards = wait.until(
            EC.presence_of_all_elements_located(SearchPageLocators.BOOK_CARD),
            message="Карточки товаров не найдены"
        )
        search_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        search_button.click()
        # time.sleep(1)
        # Ограничиваем количество добавляемых книг для стабильности до 3 книг
        for card in book_cards[:3]:
            try:
                # Прокручиваем к карточке
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", card)
                time.sleep(0.5)

                # Клик по кнопке "Купить"
                buy_button = wait.until(
                    EC.element_to_be_clickable(card.find_element(*SearchPageLocators.BUY_BUTTON)),
                    message="Кнопка 'Купить' не кликабельна"
                )
                buy_button.click()

                # Ожидание подтверждения добавления
                wait.until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-notification")),
                    message="Уведомление о добавлении не появилось"
                )
                time.sleep(1)  # Пауза между добавлениями

            except Exception as e:
                print(f"Ошибка при добавлении книги: {str(e)}")
                continue

        # Переход в корзину
        cart_button = wait.until(
            EC.element_to_be_clickable(SearchPageLocators.CART_BUTTON),
            message="Кнопка корзины не кликабельна"
        )
        cart_button.click()

        # Проверка перехода в корзину
        wait.until(
            EC.url_contains("/cart"),
            message="Не удалось перейти в корзину"
        )
        time.sleep(10)  # Пауза для загрузки корзины

    def test_clean_cart(self, driver, wait):
        """ ТЕСТ очистка корзины и переход обратно в каталог. ПОЗИТИВНЫЙ"""
        clear_button = wait.until(
            EC.element_to_be_clickable(CartPageLocators.CLEAR_CART)
        )
        clear_button.click()
        time.sleep(0.5)

        #  Клик на кнопку возврата в каталог
        back_to_catalogue = wait.until(
            EC.element_to_be_clickable(CartPageLocators.BACK_TO_CATALOGUE)
        )
        back_to_catalogue.click()
        time.sleep(5)

    def test_add__one_book(self, driver, wait):
        # Тест Поиск книги ПОЗИТИВНЫЙ
        search_input = wait.until(
            EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT)
        )
        search_input.click()
        search_input.send_keys(TestData.BOOK2)

        # Клик на нопку поиска
        search_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        search_button.click()

        """Добавление первой книги """
        first_book = wait.until(EC.visibility_of_element_located(SearchPageLocators.BOOK_CARD2))
        first_book.find_element(*SearchPageLocators.BUY_BUTTON).click()

        # Переход в корзину
        cart_button = wait.until(
            EC.element_to_be_clickable(SearchPageLocators.CART_BUTTON),
            message="Кнопка корзины не кликабельна"
        )
        cart_button.click()

        # Проверка перехода в корзину
        wait.until(
            EC.url_contains("/cart"),
            message="Не удалось перейти в корзину"
        )
        time.sleep(10)  # Пауза для загрузки корзины

    def test_clean_cart_and_restore(self, driver, wait):
        """ ТЕСТ очистка корзины и обратное восстановление. ПОЗИТИВНЫЙ"""
        clear_button = wait.until(
            EC.element_to_be_clickable(CartPageLocators.CLEAR_CART)
        )
        clear_button.click()
        time.sleep(0.5)

        #  Клик на кнопку восстановить корзину
        back_to_cart = wait.until(
            EC.element_to_be_clickable(CartPageLocators.BACK_TO_CART)
        )
        back_to_cart.click()
        time.sleep(5)
