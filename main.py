import functions, players, fields, enmyAI
import copy

# Vytvoření hráčů
hrac = players.Hrac()
nepritel = players.Nepritel()

# Hlavní cyklus hry
while True:
    functions.vypsatHraciPole()
    fields.helpMatrix = copy.deepcopy(fields.matrix)
    smer = input("Zadej svůj tah: ")
    if smer == "konec" or smer == "break":
        print("Konec hry")
        break
    elif smer == "reset-mapy":
        fields.matrix = fields.defaultMatrix
        break
    elif smer == "info":
        print("Veškeré informace o hře najdeš v souboru README.md")
    elif smer == "zdravi":
        print(f"Zdraví hráče (ty): {hrac.zdravi}")
        print(f"Zdraví nepřítele: {nepritel.zdravi}")
    elif smer == "brneni":
        print(f"Brnění hráče (ty): {hrac.brneni}")
        print(f"Brnění nepřítele: {nepritel.brneni}")
    elif smer == "sila":
        print(f"Síla hráče (ty): {hrac.sila}")
        print(f"Síla nepřítele: {nepritel.sila}") 
    elif smer in ["w", "W", "a", "A", "s", "S", "d", "D"]:
        hrac.pohyb(smer)
        enmyAI.enmysMove(nepritel.pozice, nepritel)
        functions.zkotrolovatAPridatItem()
    else:
        print("Žádný tah nebyl proveden. Špatný vstup!")