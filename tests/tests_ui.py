# pytest tests_ui.py  -v
# for ($i=1; $i -le 3; $i++) { pytest tests_ui.py  -v}
import time
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import TestData, MainPageLocators, SearchPageLocators
from locators.locators import CartPageLocators  # Импорт локаторов


class TestSearch:
    def test_search_book_1(self, wait):
        # Тест Поиск книги ПОЗИТИВНЫЙ
        wait.until(
            EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT)
        )

        search_input = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_INPUT)
        )
        
        search_input.click()
        search_input.send_keys(TestData.BOOK)

        # Клик  на нопку поиска
        search_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        search_button.click()

    def test_add_books_2(self, driver, wait):
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

        # Ограничиваем количество добавляемых книг для стабильности до 3 книг
        for card in book_cards[:3]:
            try:
                # Прокручиваем к карточке
                driver.execute_script(
                    "arguments[0].scrollIntoView({block: 'center'});", card)

                # Клик по кнопке "Купить"
                buy_button = wait.until(
                    EC.element_to_be_clickable(card.find_element(
                        *SearchPageLocators.BUY_BUTTON)),
                    message="Кнопка 'Купить' не кликабельна"
                )
                buy_button.click()

                wait.until(
                    EC.element_to_be_clickable(card.find_element(
                        *SearchPageLocators. WAIT_IN_SEARCH))
                )

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

    def test_clean_cart_3(self, driver, wait):
        """ ТЕСТ очистка корзины и переход обратно в каталог. ПОЗИТИВНЫЙ"""
        # ожидание появления кнопки корзины
        wait.until(
            EC.presence_of_element_located(CartPageLocators.MAKE_ORDER_BUTTON))
        
        wait.until(
            EC.visibility_of_element_located(SearchPageLocators.CART_BUTTON))

        cart_button = wait.until(
            EC.element_to_be_clickable(SearchPageLocators.CART_BUTTON)
        )
        cart_button.click()

        wait.until(
            EC.visibility_of_element_located(CartPageLocators.CLEAR_CART)
        )

        clear_button = wait.until(
            EC.element_to_be_clickable(CartPageLocators.CLEAR_CART)
        )
        clear_button.click()

        #  Клик на кнопку возврата в каталог
        back_to_catalogue = wait.until(
            EC.element_to_be_clickable(CartPageLocators.BACK_TO_CATALOGUE)
        )
        back_to_catalogue.click()

    def test_add__one_book_4(self, driver, wait):
        # Тест Поиск второй книги ПОЗИТИВНЫЙ
        search_input = wait.until(
            EC.visibility_of_element_located(MainPageLocators.SEARCH_INPUT)
        )

        search_input = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_INPUT)
        )

        search_input.click()
        search_input.send_keys(TestData.BOOK2)

        # Клик на нопку поиска
        search_button = wait.until(
            EC.element_to_be_clickable(MainPageLocators.SEARCH_BUTTON)
        )
        search_button.click()

        """Добавление первой книги """
        wait.until(EC.visibility_of_element_located
                   (SearchPageLocators.BOOK_CARD2))
        
        first_book = wait.until(
            EC.element_to_be_clickable(SearchPageLocators.BOOK_CARD2)
        )
        first_book.find_element(*SearchPageLocators.BUY_BUTTON).click()

        # Переход в корзину
        wait.until(
            EC.presence_of_element_located(SearchPageLocators.CART_BUTTON)
        )

        cart_button = wait.until(
            EC.element_to_be_clickable(SearchPageLocators.CART_BUTTON)
        )
        cart_button.click()

        # Проверка перехода в корзину
        wait.until(
            EC.url_contains("/cart")
        )

    def test_clean_cart_and_restore_5(self, driver, wait):
        """ ТЕСТ очистка корзины и обратное восстановление. ПОЗИТИВНЫЙ"""
        # cart_button = wait.until(
        #     EC.element_to_be_clickable(SearchPageLocators.CART_BUTTON)
        # )
        # cart_button.click()

        wait.until(
            EC.presence_of_element_located(CartPageLocators.MAKE_ORDER_BUTTON))

        wait.until(
            EC.presence_of_element_located(CartPageLocators.CLEAR_CART)
        )

        clear_button = wait.until(
            EC.element_to_be_clickable(CartPageLocators.CLEAR_CART)
        )
        clear_button.click()

        #  Клик на кнопку восстановить корзину
        wait.until(
            EC.presence_of_element_located(CartPageLocators.RESTORE_CART)
        )

        restore_cart = wait.until(
            EC.element_to_be_clickable(CartPageLocators.RESTORE_CART)
        )
        restore_cart.click()

        logo_button = wait.until(
            EC.element_to_be_clickable(CartPageLocators.LOGO_BUTTON)
        )
        logo_button.click()

        time.sleep(3)
