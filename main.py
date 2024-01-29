import pyautogui
import platform
import time

import requests
# fetch from https://spammer.vercel.app/ and get the raw html
html = requests.get("https://spammer.vercel.app/").text
# find the word in the html
if html != "true":
  print("you are not allowed to use this program now.")
  time.sleep(100)
  exit()

print("whatsapp bot spammer")
word = input("enter the phrase you want to spam: ")
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

pyautogui.click()
pyautogui.typewrite(word, interval=0)
pyautogui.hotkey(cntrling_key, 'a')

pyautogui.hotkey(cntrling_key, 'c')
pyautogui.hotkey(cntrling_key, 'v')
pyautogui.press('enter')

if n != "":
  for i in range(int(n)-1):
    pyautogui.hotkey(cntrling_key, 'v')
    pyautogui.press('enter')
else: 
  while True:
    pyautogui.hotkey(cntrling_key, 'v')
    pyautogui.press('enter')
