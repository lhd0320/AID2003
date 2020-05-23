list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]
list02 = [
    [1, 2, 3, 4, 9],
    [5, 6, 7, 8, 9],
]

def print_double_list(list_target):
    for r in list_target:
        for c in r:
            print(c, end=" ")
        print()


print_double_list(list01)
print_double_list(list02)




