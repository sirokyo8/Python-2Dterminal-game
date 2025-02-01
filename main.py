import functions, players, fields, enmyAI
import copy

# Vytvoření hráčů
hrac = players.Hrac()
nepritel = players.Nepritel()

# Hlavní cyklus hry
while True:
    zivotHrace = functions.zije(hrac)
    zivotNepritele = functions.zije(nepritel)
    
    if not zivotHrace and not zivotNepritele:
        print("REMÍZA! Oba jste ztratili veškeré zdraví!")
        break
    elif not zivotHrace:
        print("PROHRÁL JSI! Tvé zdraví kleslo na 0!")
        break
    elif not zivotNepritele:
        print("VYHRÁL JSI! Nepřítel ztratil veškeré zdraví!")
        break
    
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
    elif smer == "pocet-uteku":
        print(f"Hráč (ty) má {hrac.utek} útěků")
    elif smer == "ja":
        print(f"Tvoje zdraví: {hrac.zdravi}")
        print(f"Tvoje síla: {hrac.sila}")
        print(f"Tvoje brnění: {hrac.brneni}")
        print(f"Tvoje útěky: {hrac.utek}")
    elif smer == "nepritel":
        print(f"Zdraví nepřítele: {nepritel.zdravi}")
        print(f"Síla nepřítele: {nepritel.sila}")
        print(f"Brnění nepřítele: {nepritel.brneni}")
    elif smer == "boj":
        if functions.jsouVedle(hrac, nepritel):
            functions.boj(hrac, nepritel)
        else: print("Nemůžeš zaútočit, protože nejsi vedle nepřítele!")
    
    # Útěky hráče
    elif len(smer) >= 2 and smer[0] in ["w", "W", "a", "A", "s", "S", "d", "D"] and smer[1] in ["w", "W", "a", "A", "s", "S", "d", "D"] and (len(smer) == 2 or (len(smer) == 3 and smer[2] in ["w", "W", "a", "A", "s", "S", "d", "D"])):
        if hrac.utek < 1:
            print("Nemáš možnost útěku (musíš nejdříve získat útěk z itemu)!")
        else:
            if len(smer) == 2:
                hrac.pohyb(smer[0])
                hrac.pohyb(smer[1])
                hrac.utek -= 1
                enmyAI.enmysMove(nepritel.pozice, nepritel)
                functions.zkotrolovatAPridatItem()
            elif len(smer) == 3:
                hrac.pohyb(smer[0])
                hrac.pohyb(smer[1])
                hrac.pohyb(smer[2])
                hrac.utek -= 1
                enmyAI.enmysMove(nepritel.pozice, nepritel)
                functions.zkotrolovatAPridatItem()
        
    # Pohyby hráče
    elif smer in ["w", "W", "a", "A", "s", "S", "d", "D"]:
        hrac.pohyb(smer)
        enmyAI.enmysMove(nepritel.pozice, nepritel)
        if functions.jsouVedle(hrac, nepritel):
            hrac.zdravi -= (functions.myRound(nepritel.sila / 2) - hrac.brneni)
            print("Nepřítel na tebe zaútočil poloviční silou!")
            print(f"Zdraví hráče (ty): {hrac.zdravi}")
        functions.zkotrolovatAPridatItem()
    else:
        print("Žádný tah nebyl proveden. Špatný vstup!")