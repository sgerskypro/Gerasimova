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

-!!!!!!!!!!!!!!!!!!!!!!! [Проект Читай город: тест план + отчет о тестировании ](https://juniper-ranunculus-9dd.notion.site/09e79800396f4c2ca5a6651d5bbfe692?pvs=4)
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

- `pytest | python3 -m pytest` (запуск тестов)
- `python3 -m pytest -s` (вывод в консоль print)
- `python3 -m pytest -v` (запуск тестов с подробным выводом в консоль)
- `python3 pytest -m ui_test.py` (запуск только UI тестов)
- `python3 pytest -m api_test.py` (запуск только API тестов)
- `python3 -m pytest --alluredir allure-result` (запуск тестов и сохранение отчета о результатах тестирования)
- `python3 allure serve allure-result/` (формирование отчета о тестировании)
pytest  -v