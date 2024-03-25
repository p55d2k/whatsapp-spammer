import time
import platform
import pyperclip
import pyautogui
import os
os.system("pip install pyautogui requests")
print("\033c")

print("whatsapp bot spammer")
word = input(
    "enter the phrase you want to spam (press space to use the text you already copied): ")
n = input("enter the number of times you want to spam, leave blank for infinite: ")
print("open whatsapp web in a browser and select the chat you want to spam")
time.sleep(1)
print("if u select infinite it wont stop until u close the program")
time.sleep(1)
print("you have 5 seconds before the program starts")
time.sleep(5)

if platform.system() == 'Windows':
    cntrling_key = 'ctrl'
else:
    cntrling_key = 'command'

if word != " ":
    pyperclip.copy(word)

pyautogui.click()
pyautogui.hotkey(cntrling_key, 'v')
pyautogui.press('enter')

if n != "":
    for i in range(int(n)):
        pyautogui.hotkey(cntrling_key, 'v')
        pyautogui.press('enter')
else:
    while True:
        pyautogui.hotkey(cntrling_key, 'v')
        pyautogui.press('enter')
