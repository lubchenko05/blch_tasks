"""
Дано масив цілих чисел, знайти найбільший добуток, який можна отримати з трьох чисел цього масиву.
Вхідний масив має містити хоча б три цілих числа.
"""


def get_max_mult(l):
    if type(l) != list or len(l) < 3:
        print('lt must be a list that contains at least 3 items')
        return
    data = sorted(l)
    return data[-1]*data[-2]*data[-3]


if __name__ == "__main__":
    print(get_max_mult([4, 3, 5, 2, 6]))