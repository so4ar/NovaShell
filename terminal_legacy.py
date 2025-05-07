import sys
import pyautogui
import os

power = True

color = "color 0F"

while power:

    command = input(">>> ")

    if command.startswith("/"):

        if command == "/exit" or command == "/e":
            power = False
        
        elif command == "/fullscreen" or command == "/full":
            pyautogui.press("f11")

        elif command == "/color/info":
            print("""
    | Kod | Kolor          |
    | --- | -------------- |
    | 0   | Czarny         |
    | 1   | Niebieski      |
    | 2   | Zielony        |
    | 3   | Turkusowy      |
    | 4   | Czerwony       |
    | 5   | Fioletowy      |
    | 6   | Złoty          |
    | 7   | Szary          |
    | 8   | Jasnoszary     |
    | 9   | Jasnoniebieski |
    | A   | Jasnozielony   |
    | B   | Jasnoturkusowy |
    | C   | Jasnoczerwony  |
    | D   | Jasnofioletowy |
    | E   | Jasnozłoty     |
    | F   | Biały          |
    """)
        
        elif command.startswith("/color/set"):
            color = command.replace("/color/set ", "color ")
            os.system(color)

        elif command == "/clear" or command == "/cls":
            os.system("cls")

        elif command.startswith("/open"):
            path = command.replace("/open ", "")
            if os.path.exists(path):
                os.startfile(path)
            else:
                print("Path does not exist")

        else:
            print("Unknown command")
        
    else:
        print(command)

    