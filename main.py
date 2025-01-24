import functions, players, fields, enmyAI

# Vytvoření hráčů
hrac = players.Hrac()
nepritel = players.Nepritel()

# Vypsání informací ke hře
functions.info()

# Hlavní cyklus hry
while True:
    functions.vypsatHraciPole()
    smer = input("Zadej svůj tah: ")
    if smer == "konec" or smer == "break":
        print("Konec hry")
        break
    elif smer == "reset-mapy":
        fields.matrix = fields.defaultMatrix
        break
    elif smer == "info":
        functions.info()
        
    if smer not in ["w", "W", "a", "A", "s", "S", "d", "D"]:
        print("Byl zadán neplatný vstup")
    else:
        hrac.pohyb(smer)