import functions, players, fields

# Vytvoření hráčů
hrac = players.Hrac()
nepritel = players.Nepritel()

# Vypsání informací ke hře
functions.info()

# Hlavní cyklus hry
while True:
    functions.vypsatHraciPole()
    smer = input("Zadej směr: ")
    if smer == "konec" or smer == "break":
        print("Konec hry")
        break
    if smer not in ["w", "W", "a", "A", "s", "S", "d", "D"]:
        print("Byl zadán neplatný vstup")
    else:
        hrac.pohyb(smer)