import time
import pyautogui
import os
os.system("pip install pyautogui requests")
print("\033c")

if not os.path.exists('n.txt'):
    with open('n.txt', 'w') as f:
        f.write('0')

print("whatsapp bot spammer")
time.sleep(5)

cntrling_key = 'command'

n = 0
with open('n.txt', 'r') as f:
    n = int(f.read())

pyautogui.click()
pyautogui.typewrite(str(n))
pyautogui.press('enter')

while True:
    n += 1
    with open('n.txt', 'w') as f:
        f.write(str(n))
    pyautogui.typewrite(str(n))
    pyautogui.press('enter')
