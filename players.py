import functions, fields

# Classes s hráči
class Player():
    def __init__(self):
        self.sila = 10
        self.zdravi = 100
        self.brneni = 5
        self.pozice = (0,0)
        
    def pohyb(self, smer):
        # Zjištění symbolu hráče
        if self.typ == "hrac":
            symbol = "@"
        else: symbol = "#"
        
        # Pohyb nahoru
        if smer in ("w", "W"):
            pohyb = (self.pozice[0] - 1, self.pozice[1])
            if functions.kontrola(pohyb, self):
                fields.matrix[pohyb[0]][pohyb[1]] = symbol
                fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                self.pozice = pohyb
                if self.typ == "hrac":
                    print(f"Posunul jsi se na pozici {self.pozice}")
                
        # Pohyb doleva        
        elif smer in ("a", "A"):
            if smer in ("a", "A"):
                pohyb = (self.pozice[0], self.pozice[1] - 1)
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = symbol
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    if self.typ == "hrac":
                        print(f"Posunul jsi se na pozici {self.pozice}")
        
        # Pohyb dolů   
        elif smer in ("s", "S"):
            if smer in ("s", "S"):
                pohyb = (self.pozice[0] + 1, self.pozice[1])
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = symbol
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    if self.typ == "hrac":
                        print(f"Posunul jsi se na pozici {self.pozice}")
        
        # Pohyb doprava
        elif smer in ("d", "D"):
            if smer in ("d", "D"):
                pohyb = (self.pozice[0], self.pozice[1] + 1)
                if functions.kontrola(pohyb, self):
                    fields.matrix[pohyb[0]][pohyb[1]] = symbol
                    fields.matrix[self.pozice[0]][self.pozice[1]] = "-"
                    self.pozice = pohyb
                    if self.typ == "hrac":
                        print(f"Posunul jsi se na pozici {self.pozice}")
        
        else: print("Byl zadán neplatný vstup")

class Nepritel(Player):
    def __init__(self):
        super().__init__()
        self.pozice = self.najdiPozici()
        self.typ = "nepritel"
        
    def najdiPozici(self):
        for i in fields.matrix:
            for z in i:
                if z == "#":
                    return (fields.matrix.index(i), i.index(z))
    
class Hrac(Player):
    def __init__(self):
        super().__init__()
        self.pozice = self.najdiPozici()
        self.typ = "hrac"
        self.utek = 1
        
    def najdiPozici(self):
        for i in fields.matrix:
            for z in i:
                if z == "@":
                    return (fields.matrix.index(i), i.index(z))