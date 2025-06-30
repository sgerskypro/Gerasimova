# Проект по автоматизации API и UI тестирования на Python для компании веб-сервиса Читай город

***
«Читай-город» – это самая большая в России сеть книжных магазинов и интернет-магазин.

## Шаги

1. Установить зависимости
2. Запустить тесты с указанием пути к директории результатов тестирования `pytest --alluredir allure_files`
3. Сформировать отчет `allure generate allure-files -o allure_report`
4. Открыть отчет `allure open allure_report`

## Стек

- pytest<br>
- selenium<br>
- requests<br>
- allure<br>
- config<br>

## Структура

- ./test - тесты
    - \_\_init\_\_.py
    - /api_test.py - API-тесты
    - /ui_test.py - UI-тесты
- ./web_pages - описание страниц
    - /CompanyApi.py - описание API-методов
    - /MainPage.py - описание методов на главной странице
    - /ResultPage.py - описание результатов
- ./pytest.ini - файл конфигурации для pytest, который содержит настройки тестирования, такие как параметры командной
  строки и плагины.
- README.md - файл с документацией проекта, в котором описаны установка, использование, структура проекта и другие
  важные аспекты.
- requirements.txt - файл с используемыми зависимостями

## Полезные ссылки

- [Тест-план] https://sger.yonote.ru/doc/diplom-chitaj-gorod-hborpA8792
- [Веб-интерфейс сервиса Читай город ](https://www.chitai-gorod.ru/)

## Библиотеки

- pip3 install pytest
- pip3 install selenium
- pip3 install webdriver-manager
- pip3 install allure-pytest
- pip3 install requests
- pip install pytest requests python-dotenv allure-pytest -для API-тестов
- pip install selenium webdriver-manager - для UI -тестов

## Запуск тестов

- pytest tests_api.py -v
- pytest tests_ui.py  -v