# EN: Function for checking if I can go to the position
# CZ: Funkce pro zkontrolování, zda na pozici můžu jít

import main

def kontrola(pozice, hrac):
    row, col = pozice
    if main.matrix[row][col] == "█":
        print("Narazil jsi do zdi: Ubráno zdraví o 1!")
        hrac.zdravi -= 1
        return False
    elif main.matrix[row][col] == "-":
        return True
    elif main.matrix[row][col] == "*":
        print("Sebral jsi item! (ještě není plně funkční)") # DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT !!!!!!!!!!
        return True