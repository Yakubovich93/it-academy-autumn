"""Вводится строка. Требуется удалить из нее повторяющиеся символы и все
    пробелы. Например, если было введено "abc cde def", то должно быть
    выведено "abcdef".

   Подсказка: оператор in проверяет, входит ли подстрока в строку или нет.
"""


def sub_string(str_):
    """Конструирование подстроки.

    :param str_: входная строка
    :return: строка. Получившееся выражение
    """

    # write your code here
    string_ = "abcd bcd bdef ef"
    new_str = ''.join(string_.split())
    list_ = []
    for elem in new_str:
        if elem not in list_:
            list_.append(elem)
            result = ''.join(list_)
    return 'Получившееся выражение: ' + result


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    str_ = ''
    print(sub_string(str_))
