#! python3
# -*- coding: utf-8 -*-
# @date: 2018/6/12 20:37
# @name: ch
# @author：Go361
import pyautogui
import pyperclip

pyautogui.PAUSE = 1.5

fileName = 'TIMsearch.png'	## TIM 搜索框
message = u'学而时习之'
im = pyautogui.screenshot()
def messageSend(richText='Hello!'):
	try:
		position = pyautogui.locateOnScreen(fileName)
		print(position)
	except Exception as err:
		print("Can't find dst area" + str(err))
	centerX, centerY = pyautogui.center(position)
	pyautogui.click(centerX, centerY)	## 获得搜索框
	pyautogui.typewrite('1046554514')	## 输入要查找的人
	pyautogui.press('enter')	## 打开聊天界面
	pyperclip.copy(richText)
	pyautogui.hotkey('ctrl', 'v')	## 输入要发送的消息
	pyautogui.press('enter')	## 发送

# messageSend(message)
with open("OurLove.txt",encoding='utf-8') as f:
	print(f)
	record = []
	for line in f.readlines():
		# line = line.split("/n")
		record.append(line)
		# break
# print(len(record))
for i in range(0, 2000):
	messageSend(record[i])