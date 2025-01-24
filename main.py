# RUN THIS FILE TO PLAY THE GAME!
# SPUSŤ TENTO SOUBOR PRO ZAČÁTEK HRY!

import others.players as players
import others.defaultField as defaultField

# Hrací pole
matrix = [
    ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "█", "-", "-", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "@", "-", "-", "-", "-", "-", "#", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "█", "-", "-", "-", "-", "*", "-", "-", "█"],
    ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
]

# Funkce pro vypisování hracího pole
def vypsatHraciPole():
    for i in matrix:
        for z in i:
            print(z, end="")
        print()