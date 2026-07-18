nums = [5, 6, 7, 7, 1, 9, 1, 1, 5, 1, 1, 111]

## Method-1:


def count_items(ns: list):
    countDict = {}

    for i in range(0, len(ns)):
        if ns[i] in countDict:
            countDict[ns[i]] += 1
        else:
            countDict[ns[i]] = 1

    return countDict


print(count_items(nums))


## Method-2:


def countItems(ns: list):
    hashMap = dict()

    n = len(ns)

    for i in range(0, n):
        hashMap[ns[i]] = hashMap.get(ns[i], 0) + 1

    return hashMap


print(countItems(nums))
