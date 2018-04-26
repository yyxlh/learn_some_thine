#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width, height = pyautogui.size()
print(width, height)

pyautogui.moveTo(500, 500, duration=0.25)
pyautogui.moveRel(100, 0, duration=0.25)

cur_pos_x, cur_pos_y = pyautogui.position();
print(cur_pos_x, cur_pos_y)

# 点击鼠标
pyautogui.click(600, 400, button='left')
pyautogui.doubleClick(600, 400, button='left')
# 拖动鼠标
pyautogui.dragTo(600, 300, duration=0.25)
pyautogui.dragRel(0, -100, duration=0.25)
# 滚动鼠标
pyautogui.scroll(-200)
# 屏幕快照，进行分析判断
im = pyautogui.screenshot()
# 图像识别
left, top, right, bottom = pyautogui.locateOnScreen('button.png')
x, y = pyautogui.center(left, top, right, bottom)
pyautogui.click(x, y)

# 模拟键盘输入
print(pyautogui.KEYBOARD_KEYS)
pyautogui.typewrite('Hello every body!')
pyautogui.press('enter')

# 模拟输入 $
pyautogui.keyDown('shift')  # 按下某键
pyautogui.press('4')  # 输入某个字符，调用了keyDown和keyUp
pyautogui.keyUp('shift')  # 抬起某键
# 热键，也可以通过keyDown和keyUp组合进行实现，但是比较麻烦
pyautogui.hotkey('ctrl', 'v')
