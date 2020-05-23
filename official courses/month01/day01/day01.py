"""
    1.在pycharm创建工程:
        file --> new project --> 设置location
    2.执行方式:交互式 文件式
    3.执行过程:
              c/c++   运行前   (运行快,不能跨平台)
              源代码   -编译->   机器码
              JavaScript 运行时   (运行慢,能跨平台)
              源代码   -解释->   机器码
              python  运行时
              源代码   -"编译"->   字节码   -解释->   机器码
                /     第一次        /
                       优化              跨平台
"""


"""
    汇率转换器
"""
#1.获取数据
usd = float(input("请输入您的美元:"))

#2.逻辑计算
rmb = usd * 7.0947

#3.显示结果 1美元=7.0947人民币
print(str(usd)+"美元="+str(rmb)+"元")


"""
总结:
1.程序自上而下执行,但是编码要以需求为导向.
2.一行代码往往是从右向左编写
3.程序写完一定报错
    仔细阅读错误提示,定位错误代码,再修改.
"""