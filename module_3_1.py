# Домашняя работа по уроку "Пространство имён"
# Задача "Счётчик вызовов":
calls = 0


def count_calls():
    """
    Функция подсчитывает вызовы остальных функций
    путем увеличения на единицу глобальной переменной calls

    :return: none
    """
    global calls
    calls += 1


def string_info(string):
    """
    Функция string_info принимает аргумент - строку и
    возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    :param string: строка
    :return: кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре
    """
    tuple_ = [len(string), string.upper(), string.lower()]
    count_calls()
    return tuple(tuple_)


def is_contains(string_info, is_contains):
    """
    Функция is_contains принимает два аргумента: строку и список,
    и возвращает
    True, если строка находится в этом списке,
    False - если отсутствует.
    Регистром строки при проверке пренебрегает: UrbaN ~ URBAN.
    :param string_info: String
    :param is_contains: Tuple
    :return: True, если строка находится в этом списке, False - если отсутствует.
    """
    is_contains_2 = []
    count_calls()
    for i in is_contains:
        is_contains_2.append(i.lower())
    return string_info.lower() in is_contains_2


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)

"""
Вывод на консоль:
(8, 'CAPYBARA', 'capybara')
(10, 'ARMAGEDDON', 'armageddon')
True
False
4
"""
