"""
PyAutoGUI——做职场高手让所有GUI自动化击败无聊的办公室重复性操作
GUI:图形用户界面(Graphical User Interface)
例如 办公软件音乐播放器...
作用：自动控制鼠标和键盘。
文档：https://pyautogui.readthedocs.io/en/latest/install.html
安装：pip3 install pyautogui

盘点机械化：文档、发邮件、电商摘抄商品价格
公司系统、登微信、QQ、
"""
# 准备工具
import pyautogui

# 只能运行在命令行中
# pyautogui.displayMousePosition()

# # 工具.移动(x轴y轴持续时间)
pyautogui.moveTo(325,407,1)# 移动到酷狗音乐
# # 工具.双击()
pyautogui.doubleClick()# 打开酷狗
# # pyautogui.moveTo(962,881,1)# 移动到播放

# 1. 工具.截屏(region=(x轴y轴宽高))
# img = pyautogui.screenshot(region=(604,851,70,70))
# # 工具.保存("图片名称")
# img.save("play.png")

# 工具.睡眠(秒)
pyautogui.sleep(3)# 等等3秒

# 2. 工具.定位("需要定位的图片名称")
position = pyautogui.locateOnScreen("play.png")
# 工具.中心点()
position = pyautogui.center(position)
# 3. 移动
pyautogui.moveTo(position.x,position.y,1) # 移动到播放


# 工具.睡眠(秒)
pyautogui.sleep(3)# 等等3秒
# 工具.单击()
pyautogui.click()# 单击播放