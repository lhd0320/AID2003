# list01 = [4, 56, 6, 76, 87, 8, 1]

# for r in range(len(list01) - 1):
#     for c in range(r + 1, len(list01)):
#         if list01[r] < list01[c]:
#             list01[r], list01[c] = list01[c], list01[r]
# print(list01)

def descending_sort(list_num):
    for r in range(len(list_num) - 1):
        for c in range(r + 1, len(list_num)):
            if list_num[r] < list_num[c]:
                list_num[r], list_num[c] = list_num[c], list_num[r]
list01 = [4, 56, 6, 76, 87, 8, 1]
descending_sort(list01)
print(list01)