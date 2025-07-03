# Проект по автоматизации API и UI тестирования на Python для  веб-сервиса Читай город

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

- pip install -U pytest selenium webdriver-manager allure-pytest requests
- pip install pytest-repeat

## Запуск тестов

- pytest tests_api.py -v
- pytest tests_ui.py  -v    [тесты выполняются в трогом порядке один за другим]
- pytest --ignore=tests/conftest.py tests/  [запуск всех тестов одновременно]
- for ($i=1; $i -le 10; $i++) { pytest --ignore=tests/conftest.py tests/ -v }  [запуск всех тестов одновременно 10 раз подряд]