import time

import pyautogui

# pyautogui.moveRel(-50, -50, duration=0.5)  # Move the mouse cursor up and to the left

pyautogui.moveTo(469, 746, duration=0.2)
pyautogui.click()

pyautogui.moveTo(508, 370, duration=0.6)
pyautogui.click()

pyautogui.moveTo(797, 355, duration=0.6)
pyautogui.doubleClick()

time.sleep(5)
print(pyautogui.position() )

