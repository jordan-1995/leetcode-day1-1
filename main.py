def swapNums(list):
    last_position = len(list) - 1

    last = list.pop(last_position)
    first = list.pop(0)

    list.insert(last_position-1, first)
    list.insert(0, last)

    print(list)

swapNums([1, 2, 3, 4, 5])