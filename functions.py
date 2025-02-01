# RUN THIS FILE TO PLAY THE GAME!
# SPUSŤ TENTO SOUBOR PRO ZAČÁTEK HRY!

import fields, players, random
    
# Funkce pro vypisování hracího pole
def vypsatHraciPole():
    for i in fields.matrix:
        for z in i:
            print(z, end="")
        print()

# Funkce pro kontrolu, zda můžu jít na pozici
def kontrola(pozice, hrac):
    row, col = pozice
    if fields.matrix[row][col] == "█":
        print("Narazil jsi do zdi: Ubráno zdraví o 1!")
        hrac.zdravi -= 1
        return False
    elif fields.matrix[row][col] == "-":
        return True
    elif fields.matrix[row][col] == "*":
        if hrac.typ=="hrac":
            vec = item("h")
            if vec[0] == "zdravi":
                hrac.zdravi += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} zdraví")
            elif vec[0] == "sila":
                hrac.sila += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} síly")
            elif vec[0] == "utek":
                hrac.utek += vec[1]
                print(f"Získal jsi 1 útěk navíc")
            else:
                hrac.brneni += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} brnění")
        elif hrac.typ=="nepritel":
            vec = item("n")
            if vec[0] == "zdravi":
                hrac.zdravi += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} zdraví")
            elif vec[0] == "sila":
                hrac.sila += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} síly")
            else:
                hrac.brneni += vec[1]
                print(f"Sebral jsi lektvar a získal jsi {vec[1]} brnění")
                
        return True
    
def item(typHrace):
    if typHrace == "h":
        typItemu = random.choice(["zdravi", "sila", "brneni", "utek"])
    else:
        typItemu = random.choice(["zdravi", "sila", "brneni"])
        
    if typItemu == "zdravi":
        return ["zdravi", random.randint(5, 50)]
    elif typItemu == "sila":
        return ["sila", random.randint(5, 50)]
    elif typItemu == "utek":
        return ["utek", 1]
    else:
        return ["brneni", random.randint(1, 10)]
    
def zkotrolovatAPridatItem():
    
    # Zkontrolování, zda item náhodou už v hracím poli není
    for i in fields.matrix:
        for z in i:
            if z == "*":
                return
    
    # Pokud ne, přidáme ho
    while True:
        row = random.randint(0, len(fields.matrix)-1)
        col = random.randint(0, len(fields.matrix[0])-1)
        if fields.matrix[row][col] == "-":
            fields.matrix[row][col] = "*"
            return
        
def zije(postava):
    if postava.zdravi <= 0:
        return False
    return True

def jsouVedle(hrac, nepritel):
    pr, pc = hrac.pozice
    er, ec = nepritel.pozice
    
    if (pr + 1) == er and pc == ec:
        return True
    elif (pr - 1) == er and pc == ec:
        return True
    elif (pc + 1) == ec and pr == er:
        return True
    elif (pc - 1) == ec and pr == er:
        return True
    else: return False

def boj(hrac, nepritel):
    print("Bojuješ s nepřítelem!")

    # Útok hráče
    nepritel.zdravi -= (hrac.sila - nepritel.brneni)
    print(f"Zdraví nepřítele: {nepritel.zdravi}")
        
    # Útok nepřítele
    hrac.zdravi -= (nepritel.sila - hrac.brneni)
    print(f"Zdraví hráče: {hrac.zdravi}")
    
    return