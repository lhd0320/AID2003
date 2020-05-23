"""
    -- 全局变量
      list_merge = [2, 0, 2, 0]
      1). 定义函数,零元素移动到末尾.
        def zero_to_end():

                思想：从后向前判断，如果是0则删除,在末尾追加.
                [2, 0, 4, 2]  -->  [2, 4, 2, 0]

            pass
"""
"""
2).定义函数, 合并相邻相同数据
# [2,0,2,0]  -->[2,2,0,0]  -->  [4,0,0,0]
# [2,0,0,2]  -->[2,2,0,0]  -->  [4,0,0,0]
# [4,4,4,4]  -->  [8,8,0,0]
# [2,0,4,2]  -->  [2,4,2,0]


def merge():

          核心思想：零元素后移，判断是否相邻相同。如果是则合并.

    pass
"""
"""
     3). 向左移动
        map = [
            [2, 0, 0, 2],
            [4, 2, 0, 2],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]
        def move_left():

                向左移动map
                思想：获取每行，交给list_merge，在通知merge()进行合并
            :return:

            pass
"""
"""
4).向右移动
move_right


def move_right():

        思想：从二维列表中获取每行,反向切片,交给list_merge在通知merge()进行合并,还原给二维列表

    pass
"""
list_merge = []
list_conversion = []
map = [
    [2, 0, 0, 2],
    [4, 2, 2, 4],
    [2, 4, 2, 4],
    [0, 4, 0, 4],
]


def zero_to_end():
    for item in range(len(list_merge) - 1, -1, -1):
        if list_merge[item] == 0:
            del list_merge[item]
            list_merge.append(0)


def merge():
    for r in range(len(list_merge) - 1):
        c = r + 1
        zero_to_end()
        if list_merge[r] == list_merge[c]:
            list_merge[r] += list_merge[c]
            list_merge[c] = 0


def move_left():
    global list_merge
    global map
    for item in map:
        list_merge = item
        zero_to_end()
        merge()
    return map


def move_right():
    global list_merge
    global map
    for item in range(len(map)):
        list_merge = map[item][::-1]
        zero_to_end()
        merge()
        map[item] = list_merge[::-1]
    return map


def move_up():
    global list_merge
    global map
    global list_conversion
    list_conversion = [[r1[c1] for r1 in map] for c1 in range(4)]
    for item in list_conversion:
        list_merge = item
        zero_to_end()
        merge()
    map = [[r2[c2] for r2 in list_conversion] for c2 in range(4)]
    return map


def move_down():
    global list_merge
    global map
    global list_conversion
    list_conversion = [[r3[c3] for r3 in map] for c3 in range(4)]
    for item in range(len(list_conversion)):
        list_merge = list_conversion[item][::-1]
        zero_to_end()
        merge()
        list_conversion[item] = list_merge[::-1]
    map = [[r4[c4] for r4 in list_conversion] for c4 in range(4)]
    return map


print(move_left())
print(move_right())
print(move_up())
print(move_down())
