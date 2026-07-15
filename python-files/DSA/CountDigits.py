n = 5873

from math import *  # For second solutions

# Solution - 1:


def count_digits(num: int):
    count = 0
    while num > 0:
        count += 1
        num = num // 10

    return count


print(count_digits(n))


# Solution - 2:


def count_digits_log(num: int):
    return int(log10(num) + 1)


print(count_digits_log(n))
