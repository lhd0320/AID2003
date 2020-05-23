"""
(选做)面向对象
    参照学生管理系统,制作游戏2048.
    只需要实现上下左右移动
    控制与显示分离
"""
class GameController():
    def __init__(self):
        self.__list_merge = None #type:lis
        self.__map = [
            [2, 0, 0, 2],
            [4, 2, 2, 4],
            [2, 4, 2, 4],
            [0, 4, 0, 4],
        ]

    @property
    def list_merge(self):
        return self.__list_merge

    @property
    def map(self):
        return self.__map

    def zero_to_end(self,list_merge):
        for item in range(len(list_merge) - 1, -1, -1):
            if list_merge[item] == 0:
                del list_merge[item]
                list_merge.append(0)

    def merge(self,list_merge):
        for r in range(len(list_merge) - 1):
            c = r + 1
            self.zero_to_end(list_merge)
            if list_merge[r] == list_merge[c]:
                list_merge[r] += list_merge[c]
                list_merge[c] = 0

    def move_left(self):
        for item in self.__map:
            self.zero_to_end(item)
            self.merge(item)

    def move_right(self):
        for item in range(len(self.__map)):
            self.__list_merge=self.__map[item][::-1]
            self.zero_to_end(self.__list_merge)
            self.merge(self.__list_merge)
            self.__map[item] = self.__list_merge[::-1]

    def move_up(self):
        list_merge = [[r1[c1] for r1 in self.__map] for c1 in range(4)]
        for item in list_merge:
            self.zero_to_end(item)
            self.merge(item)
        self.__map = [[r2[c2] for r2 in list_merge] for c2 in range(4)]

    def move_down(self):
        list_conversion = [[r3[c3] for r3 in self.__map] for c3 in range(4)]
        for item in range(len(list_conversion)):
            self.__list_merge= list_conversion[item][::-1]
            self.zero_to_end(self.__list_merge)
            self.merge(self.__list_merge)
            list_conversion[item] = self.__list_merge[::-1]
        self.__map = [[r4[c4] for r4 in list_conversion] for c4 in range(4)]

class GameView:
    def __init__(self):
        self.__controller=GameController()

    def __draw_map(self):
        for line in self.__controller.map:
            print(line)

    def __display_menu(self):
        print("8键向上移动")
        print("2键向下移动")
        print("4键向左移动")
        print("6键向右移动")

    def __move_menu(self):
        item = input("请输入您的选项：")
        if item == "8":
            self.__controller.move_up()
        elif item == "2":
            self.__controller.move_down()
        elif item == "4":
            self.__controller.move_left()
        elif item == "6":
            self.__controller.move_right()

    def main(self):
        while True:
            self.__draw_map()
            self.__display_menu()
            self.__move_menu()

g=GameView()
g.main()