"""
(选做)自学：身份运算符 is
    语法:
        x is y
        x is not y
    作用：
        is 用于判断两个对象是否是同一个对象,是时返回True,否则返回False。
        is not 的作用与is相反
"""
# a = "悟空" is "悟空"
# print(a)
# b = "悟空" is "孙悟空"
# print(b)
# c = ["悟空"] is not "悟空"
# print(c)
# d = ["悟空", "八戒", "唐僧"] is ["悟空", "八戒", "唐僧"]
# print(d)
# e = {"name": "悟空", "height": 180} is {"name": "悟空", "height": 180}
# print(e)

list01=[1,2,3]
list02=[1,2,3]
print(list01 == list02)
print(list01 is list02)
