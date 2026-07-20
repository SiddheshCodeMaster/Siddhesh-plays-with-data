# Print how many time an element of "m" is present in "n"?

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# solution-1: BRUTE FORCE


def brute_solution():
    count = {}
    for x in m:
        for num in n:
            if x == num:
                count[x] = count.get(num, 0) + 1
    return count


# print(brute_solution())


# Solution-2: OPTIMIZED:


def optimized_solution():
    hash_list = [0] * len(n)

    for num in n:
        hash_list[num] += 1

    for num in m:
        if num < 1 or num > 10:
            print(0)
        else:
            print(hash_list[num])


print(optimized_solution())


# Solution-3: Ultra Optimized:
def ultra_optimized():
    freq_map = {}
    for num in n:
        freq_map[num] = freq_map.get(num, 0) + 1
        for num in m:
            print(freq_map.get(num, 0))
