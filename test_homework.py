from datetime import time


def test_dark_theme_by_time():
    """
    Протестируйте правильность переключения темной темы на сайте в зависимости от времени
    """
    current_time = time(hour=23)

    if time(hour=22) <= current_time <= time(hour=23) or time(hour=0) <= current_time <= time(hour=6):
        is_dark_theme = True
    else:
        is_dark_theme = False

    assert is_dark_theme is True


def test_dark_theme_by_time_and_user_choice():
    """
    Протестируйте правильность переключения темной темы на сайте
    в зависимости от времени и выбора пользователя
    dark_theme_enabled_by_user = True - Темная тема включена
    dark_theme_enabled_by_user = False - Темная тема выключена
    dark_theme_enabled_by_user = None - Пользователь не сделал выбор (используется переключение по времени системы)
    """
    current_time = time(hour=16)
    dark_theme_enabled_by_user = True

    if dark_theme_enabled_by_user:
        is_dark_theme = True
    elif dark_theme_enabled_by_user == False:
        is_dark_theme = False
    elif dark_theme_enabled_by_user is None:
        if time(hour=22) <= current_time <= time(hour=23) or time(hour=0) <= current_time <= time(hour=6):
            is_dark_theme = True
        else:
            is_dark_theme = False

    assert is_dark_theme is True


def test_find_suitable_user():
    """
    Найдите нужного пользователя по условиям в списке пользователей
    """
    users = [
        {"name": "Oleg", "age": 32},
        {"name": "Sergey", "age": 24},
        {"name": "Stanislav", "age": 15},
        {"name": "Olga", "age": 45},
        {"name": "Maria", "age": 18},
    ]

    suitable_users = None
    for user in users:
        if user["name"] == "Olga" and user["age"] == 45:
            suitable_users = {"name": user["name"], "age": user["age"]}
            break
    assert suitable_users == {"name": "Olga", "age": 45}

    suitable_users = []
    for user in users:
        if user["age"] < 20:
            suitable_users.append(user)
    assert suitable_users == [
        {"name": "Stanislav", "age": 15},
        {"name": "Maria", "age": 18},
    ]


# Сделайте функцию, которая будет печатать
# читаемое имя переданной ей функции и значений аргументов.
# Вызовите ее внутри функций, описанных ниже
# Подсказка: Имя функции можно получить с помощью func.__name__
# Например, вызов следующей функции должен преобразовать имя функции
# в более читаемый вариант (заменить символ подчеркивания на пробел,
# сделать буквы заглавными (или первую букву), затем вывести значения всех аргументов этой функции:
# >>> open_browser(browser_name="Chrome")
# "Open Browser [Chrome]"


def test_readable_function():
    print()
    open_browser(browser_name="Chrome")
    go_to_companyname_homepage(page_url="https://companyname.com")
    find_registration_button_on_login_page(page_url="https://companyname.com/login", button_text="Register")


def open_browser(browser_name):
    str_open_browser = open_browser.__name__
    actual_result = " ".join(str_open_browser.split("_")).title() + f" [{browser_name}]"
    print(actual_result)
    assert actual_result == "Open Browser [Chrome]"


def go_to_companyname_homepage(page_url):
    str_go_to_companyname_homepage = go_to_companyname_homepage.__name__
    actual_result = " ".join(str_go_to_companyname_homepage.split("_")).title() + f" [{page_url}]"
    print(actual_result)
    assert actual_result == "Go To Companyname Homepage [https://companyname.com]"


def find_registration_button_on_login_page(page_url, button_text):
    str_find_registration_button_on_login_page = find_registration_button_on_login_page.__name__
    actual_result = " ".join(str_find_registration_button_on_login_page.split("_")).title() + f" [{page_url}, {button_text}]"
    print(actual_result)
    assert actual_result == "Find Registration Button On Login Page [https://companyname.com/login, Register]"