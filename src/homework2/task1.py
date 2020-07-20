"""Напишите программу, которая считает общую цену.

   Вводится M рублей и N копеек цена, а также количество S товара Посчитайте
   общую цену в рублях и копейках за L товаров.
"""


def total_sum(m, n, s):
    """Подсчет общей суммы покупок.

    :param m: рубли
    :param n: копейки
    :param s: количество товара
    :return: строка. общая цена в рублях и копейках. формат:
        'x rubles y kopecks'
    """
    # write your code here
    try:
        rubles = int(input('рубли '))
        kopecks = int(input('копейки '))
        goods = int(input('количество товара '))
        rubles_total = rubles * goods
        kopecks_total = kopecks * goods

        return 'Общая цена товара составляет {0} рублей и {1} копеек за {2} товара'.\
            format(rubles_total, kopecks_total, goods)
    except ValueError:
        return 'Вы ввели не число!'


if __name__ == '__main__':
    # здесь можно сделать ввод из консоли и проверить работу функции
    m, n, s = '', '', ''
    print(total_sum(m, n, s))
