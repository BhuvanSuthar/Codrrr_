import pyautogui
import time
time.sleep(8)
count=0
while count <=50:
    pyautogui.typewrite("bye Good Night")
    pyautogui.press("enter")
    count=count+1