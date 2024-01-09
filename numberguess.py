import random

while True:
    zahl = random.randint(1,1000000)

    print("Willkommen zu Number-Guess XTREME!!!")

    show = input("Willst du die Zahl wissen aus irgendeinem Grund (y/n): ")

    if show == "y":
        print(zahl)
    elif show == "n":
        print("Okey jetzt geht es weiter")

    tip = int(input("Eine Zahl von 1-1MIO: "))

    if tip == zahl:
        print("Richtig")
        break
    elif tip > zahl:
        print("Zu hoch")
    elif tip < zahl:
        print("Zu niedrig")