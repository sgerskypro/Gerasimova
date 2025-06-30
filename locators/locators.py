from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestData:
    BOOK = "Ониксовый шторм"  # Общая переменная для всех тестов
    BOOK2 = "Граф Монте-Кристо"  # Общая переменная для всех тестов


class MainPageLocators:
    SEARCH_INPUT = (By.NAME, "search")  # поле ввода поиска
    SEARCH_BUTTON = (By.CSS_SELECTOR, ".search-form__icon-search")  # кнопка найти


class SearchPageLocators:
    # Локатор для карточек нужных книг (по локатору Book)
    BOOK_CARD = (By.CSS_SELECTOR, f"article.product-card:has(a[title*='{TestData.BOOK}'])")
    BOOK_CARD2 = (By.CSS_SELECTOR, f"article.product-card:has(a[title*='{TestData.BOOK2}'])")

    # Локатор  кнопки "Купить" в карточке
    BUY_BUTTON = (By.XPATH, ".//button[contains(., 'Купить')]")

    # кнока корзины
    CART_BUTTON = (By.XPATH, "//span[contains(text(),'Корзина')]/..")

    CART_NOTIFICATION = (By.CSS_SELECTOR, ".cart-notification")


class CartPageLocators:
    CLEAR_CART = (By.XPATH, "//span[@class='cart-page__clear-cart-title']")
    BACK_TO_CATALOGUE = (By.XPATH, "//div[contains(text(),'Перейти в каталог')]")
    BACK_TO_CART = (By.XPATH, "//div[@class='chg-app-button__content'][normalize-space()='']")
