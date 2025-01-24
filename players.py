import main
import checking

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
            if checking.kontrola(pohyb, self):
                main.matrix[pohyb[0]][pohyb[1]] = "@"
                main.matrix[self.pozice[0]][self.pozice[1]] = "-"
                self.pozice = pohyb
                print(f"Posunul jsi se na pozici {self.pozice}")
                
        elif smer in ("a", "A"):
            pass
        elif smer in ("s", "S"):
            pass
        elif smer in ("d", "D"):
            pass
        else: print("Byl zadán neplatný vstup")