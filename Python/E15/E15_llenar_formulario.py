import pyautogui,time
for i in range(2):
    time.sleep(3)
    pyautogui.click(x=336, y = 442, clicks = 1)
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.typewrite("Las decisiones dificiles requieren voluntades fuertes")
    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.click(x=659, y = 458, clicks = 1)
    pyautogui.click(x=372, y = 500, clicks = 1)

    pyautogui.press('tab')
    pyautogui.press('tab')

    pyautogui.typewrite("CorreoFalse")
    pyautogui.hotkey('shift','2')
    pyautogui.typewrite("falso.com")
    time.sleep(3)
    pyautogui.click(x=422, y = 706, clicks = 1)
    input()
    time.sleep(3)
    pyautogui.click(x=85, y = 49, clicks = 1)
