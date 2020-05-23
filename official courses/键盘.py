import pyautogui
pyautogui.moveTo(30,766,1)
pyautogui.click()
pyautogui.hotkey('ctrl', 'space')
for i in range(3):
    pyautogui.write('kankan1', interval=0.25)
pyautogui.hotkey('ctrl', 'space')
