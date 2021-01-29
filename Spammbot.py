#Über einen Stern würde ich mich freuen.



import pyautogui, time ,webbrowser, colorama

from colorama import *

init(autoreset=True)

print(Fore.CYAN + 'Wenn euch der Bot gefällt teilt es mir mit Discord: Broken__TV#2004')

text = input("Welche Nachricht soll gesendet werden:")

print(Fore.RED + 'Achtung pass auf wen du vollspammst. Frage die Person vorher es ist nicht Erlaubt.')

many = int(input("Wie oft soll die Nachricht gesendet werden:"))

print(Fore.WHITE + Back.BLUE + 'Whatsapp : https://www.whatsapp.com | Discord : https://discord.com/app')

print(Fore.GREEN + 'Falls du keinen Link öffnen möchtest drücke enter.')


url = input("Welcher Link soll geöffnet werden:")

webbrowser.open(url)



print(Fore.BLUE + 'Die Nachrichen werden in 30 Sekunden gesendet.')
time.sleep(30)


for i in range(many):
    for letter in range(len(text)):
        pyautogui.press(text[letter])
    pyautogui.press("enter")
    if i == 0:
        print(Fore.RED + 'einmal gesendet.')
    else:
        print(str(i + 1) + (Fore.RED +'mal gesendet.'))
        
