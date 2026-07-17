# To check if a number is a Armstrong Number or not?

n = 153


def checkArmstrong(num: int):

    result = 0
    nod = len(str(n))
    num = n
    while num > 0:
        last_digit = num % 10
        result = result + last_digit**nod
        num = num // 10

    return result == n


print(checkArmstrong(n))
