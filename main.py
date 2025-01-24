# Hrací pole
matrix = [
    ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
    ["█", "-", "-", "@", "-", "-", "-", "-", "█", "-", "-", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "-", "#", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "█"],
    ["█", "-", "-", "-", "-", "-", "-", "-", "█", "-", "-", "-", "-", "*", "-", "-", "█"],
    ["█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█", "█"],
]

# Funkce pro vypsání pravidel a informací o hře
def info():
    print()
    print("Ahoj, vítej v mé 2D hře. Zde jsou informace:")
    print("@ jsi ty. Na začátku hry máš 100 zdraví a sílu 20. Tvá hybnost je 50 (máš 50 tahů).")
    print("Pokud se pokusíš jít do zdi (to je: █), nabouráš a ubere se ti zdraví o 1. Máš jedno brnění a jednu zbraň.")
    print("* je item, který můžeš sebrat. Je to lektvar, když ho sebereš a použiješ, tak se ti buď zvětší zdraví o 5, nebo síla o 5, nebo hybnost o 10.")
    print("# je nepřítel, který se tě snaží zneškodnit. Nemůže tě vidět, pokud jsi od něj dál než 3 políčka. Jeho síla je 20")
    print("Pokud ty zaútočíš na nepřítele, ubereš mu stejný počet zdraví, jako máš ty sílu. To stejné platí i naopak.")
    print("Hýbeš se pomocí kláves WSAD; W-nahoru, S-dolu, A-doleva, D-doprava.")
    print("Cílem hry je zneškodnit nepřítele.")
    print("""Hru můžeš ukončit buď klávesovou zkratkou Ctrl+C, nebo napiš "konec" do inputu""")
    print("UŽIJ SI HRU!")
    print()
    print()

# Funkce pro vypisování hracího pole
def vypsatHraciPole():
    for i in matrix:
        for z in i:
            print(z, end="")
        print()

# Funkce pro zkontrolování, zda na pozici můžu jít
def kontrola(pozice, hrac):
    row, col = pozice
    if matrix[row][col] == "█":
        print("Narazil jsi do zdi: Ubráno zdraví o 1!")
        hrac.zdravi -= 1
        return False
    elif matrix[row][col] == "-":
        return True
    elif matrix[row][col] == "*":
        print("Sebral jsi item! (ještě není plně funkční)") # DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT DODĚLAT !!!!!!!!!!
        return True
        

# Classes s hráči
class Player():
    def __init__(self):
        self.sila = 50
        self.zdravi = 100
        self.hybnost = 50
        self.zbran = 1
        self.brneni = 1
        self.inventar = []
        self.pozice = (0,0)

class Nepritel(Player):
    def __init__(self):
        super().__init__()
        self.pozice = (2,9)
    
class Hrac(Player):
    def __init__(self):
        super().__init__()
        self.pozice = (1,3)
        
    
    def pohyb(self, smer):
        if smer in ("w", "W"):
            pohyb = (self.pozice[0] - 1, self.pozice[1])
            if kontrola(pohyb, self):
                matrix[pohyb[0]][pohyb[1]] = "@"
                matrix[self.pozice[0]][self.pozice[1]] = "-"
                self.pozice = pohyb
                
        elif smer in ("a", "A"):
            pass
        elif smer in ("s", "S"):
            pass
        elif smer in ("d", "D"):
            pass
        else: print("Byl zadán neplatný vstup")