import time
import pyautogui
import random
direction = 0
time.sleep(3)
while True:
    if direction == 0:
        pyautogui.mouseDown()
        pyautogui.keyDown('d')
        time.sleep(random.uniform(16.9, 17.1))
        pyautogui.keyUp('d')
        direction = 1
    elif direction == 1:
        pyautogui.mouseDown
        pyautogui.keyDown('s')
        time.sleep(random.uniform(16.9, 17.1))
        pyautogui.keyUp('s')
        direction = 0  
    
