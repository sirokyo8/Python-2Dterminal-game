import functions, fields

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
        self.pozice = self.najdiPozici()
        
    def najdiPozici(self):
        for i in fields.matrix:
            for z in i:
                if z == "#":
                    return (fields.matrix.index(i), i.index(z))
    
class Hrac(Player):
    def __init__(self):
        super().__init__()
        self.pozice = self.najdiPozici()
        
    def najdiPozici(self):
        for i in fields.matrix:
            for z in i:
                if z == "@":
                    return (fields.matrix.index(i), i.index(z))
        
    
    def pohyb(self, smer):
        # Pohyb nahoru
        if smer in ("w", "W"):
            pohyb = (self.pozice[0] - 1, self.pozice[1])
            if functions.kontrola(pohyb, self):
                fields.matrix[pohyb[0]][pohyb[1]] = "@"
                fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                self.pozice = pohyb
                print(f"Posunul jsi se na pozici {self.pozice}")
                
        # Pohyb doleva        
        elif smer in ("a", "A"):
            if smer in ("a", "A"):
                pohyb = (self.pozice[0], self.pozice[1] - 1)
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = "@"
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    print(f"Posunul jsi se na pozici {self.pozice}")
        
        # Pohyb dolů   
        elif smer in ("s", "S"):
            if smer in ("s", "S"):
                pohyb = (self.pozice[0] + 1, self.pozice[1])
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = "@"
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    print(f"Posunul jsi se na pozici {self.pozice}")
        
        # Pohyb doprava
        elif smer in ("d", "D"):
            if smer in ("d", "D"):
                pohyb = (self.pozice[0], self.pozice[1] + 1)
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = "@"
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    print(f"Posunul jsi se na pozici {self.pozice}")
        
        else: print("Byl zadán neplatný vstup")