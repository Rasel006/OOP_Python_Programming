import pyautogui 
from time import sleepH
sleep(5)
for i in range(0,7):
    pyautogui.write('Hello, Are you Okay?', interval=0.25)
    pyautogui.press('enter')