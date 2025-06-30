import pytest
import configparser
import os
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import requests

def pytest_configure(config):
    """Регистрация кастомных маркеров"""
    config.addinivalue_line(
        "markers",
        "api: mark test as API test (will not use browser)"
    )

def pytest_addoption(parser):
    """Добавляем возможность отключения браузера через командную строку"""
    parser.addoption("--no-browser", action="store_true", help="Disable browser for API tests")

def pytest_collection_modifyitems(items):
    """Сортировка тестов в порядке их объявления"""
    items.sort(key=lambda x: x.fspath)

# ------------------------- Config Fixtures -------------------------
@pytest.fixture(scope="session")
def config():
    config = configparser.ConfigParser()
    config_path = os.path.join(os.path.dirname(__file__), 'test_config.ini')
    config.read(config_path)
    return config

# ------------------------- UI Fixtures -------------------------
@pytest.fixture(scope="session") 
def browser(config, pytestconfig):
    """Фикстура браузера, которая создается только при необходимости"""
    if pytestconfig.getoption("--no-browser"):
        yield None
        return
    
    base_url = config.get('ui', 'base_url', fallback='https://www.chitai-gorod.ru/')
    browser_name = config.get('ui', 'browser_name', fallback='firefox').lower()

    options = Options()
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    
    driver.maximize_window()
    driver.get(base_url)
    
    yield driver
    if driver:
        driver.quit()

@pytest.fixture
def driver(browser, request):
    """Основная фикстура драйвера с проверкой маркера"""
    if 'api' in request.keywords:
        pytest.skip("Browser not needed for API tests")
    if browser is None:
        pytest.skip("Browser disabled by command line")
    return browser

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, timeout=10)

@pytest.fixture(autouse=True)
def soft_clear_cache(request):
    """Мягкая очистка, не сбрасывающая критичное состояние (только для UI)"""
    if 'api' in request.keywords:
        yield
        return
        
    # Получаем driver из request если он нужен
    if 'driver' in request.fixturenames:
        driver = request.getfixturevalue('driver')
        yield
        driver.execute_script("window.localStorage.clear();")
        driver.execute_script("window.sessionStorage.clear();")
    else:
        yield

# ------------------------- API Fixtures -------------------------
@pytest.fixture(scope="session")
def api_config(config):
    return {
        'base_url': config.get('api', 'base_url', fallback='https://api.chitai-gorod.ru/v1'),
        'token': config.get('api', 'token', fallback='')
    }

@pytest.fixture
def api_client(api_config):
    class APIClient:
        def __init__(self, base_url, token):
            self.base_url = base_url
            self.headers = {
                'Authorization': f'Bearer {token}',
                'Content-Type': 'application/json'
            }
        
        def get(self, endpoint, params=None):
            return requests.get(
                f"{self.base_url}{endpoint}",
                headers=self.headers,
                params=params
            )
            
        def post(self, endpoint, json=None):
            return requests.post(
                f"{self.base_url}{endpoint}",
                json=json,
                headers=self.headers
            )
    
    return APIClient(api_config['base_url'], api_config['token'])