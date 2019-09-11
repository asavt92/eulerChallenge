# -*- coding: utf-8 -*-

# Числа, кратные 3 или 5
# Если выписать все натуральные числа меньше 10, кратные 3 или 5, то получим 3, 5, 6 и 9. Сумма этих чисел равна 23.
#
# Найдите сумму всех чисел меньше 1000, кратных 3 или 5.

import src.timing
from functools import reduce


def dummy_script(limit, *args):
    summ = 0

    min_val = min(args)

    for i in range(min_val, limit):
        for a in args:
            if (i % a == 0):
                print(i)
                summ += i
                break
    return summ


def script(limit, *args):
    summ = 0

    min_val = min(args)

    # допущение, что аргументы не делятся друг на друга нацело и лимит больше НОД
    mcd = reduce(lambda x, y: x * y, args)
    assert limit > mcd

    iteration_num = limit // mcd
    left = limit % mcd
    num = 0
    for i in range(min_val, mcd+1):
        for a in args:
            if (i % a == 0):
                print(i)
                summ += i
                num += 1
                break
    print(summ, num)
    r_s = 0
    for i in range(iteration_num):
        r_s += (summ + (i * num * mcd))

    for i in range(min_val, left):
        for a in args:
            if (i % a == 0):
                r_s += i + iteration_num*mcd
                break
    return r_s


if __name__ == "__main__":
    print(dummy_script(1000, 3, 5))
    print(script(1000, 3, 5))
