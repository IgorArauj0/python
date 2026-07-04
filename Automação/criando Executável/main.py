import time

import pyautogui

# pyautogui.moveRel(-50, -50, duration=0.5)  # Move the mouse cursor up and to the left

time.sleep(3)
print(pyautogui.position()  )

pyautogui.moveTo(469, 746, duration=0.2)
pyautogui.click()