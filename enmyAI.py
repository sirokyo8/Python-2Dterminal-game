# AI for enmy (#)
# AI pro nepřítele (#)

# The enemy can see the player within 2 spaces (after spotting him, he moves towards him). Otherwise it moves to a random location.
# Nepřítel může hráče vidět do vzdálenosti 2 pole (po zahlédnutí se pohybuje směrem k němu). Jinak se přesouvá na náhodné místo.

import fields, random

def enmysMove(pozice, nepritel):
    
    # Kontrola zda nepřítel nemůže vidět hráče - pokud ano, posune se k němu
    row, col = pozice
    
    # Kontrola nahoře (3 políčka)
    for i in range(1, 4):
        if is_valid_position(row-i, col):
            if fields.matrix[row-i][col] == "@":
                if i == 1:
                    nepritel.pohyb("w")
                    return
                elif i == 2:
                    if not is_wall((row-1, col)):
                        nepritel.pohyb("w")
                        return
                else:
                    if not is_wall((row-1, col)) and not is_wall((row-2, col)):
                        nepritel.pohyb("w")
                        return
    
    # Kontrola dole (3 políčka)      
    for i in range(1, 4):
        if is_valid_position(row+i, col):
            if fields.matrix[row+i][col] == "@":
                if i == 1:
                    nepritel.pohyb("s")
                    return
                elif i == 2:
                    if not is_wall((row+1, col)):
                        nepritel.pohyb("s")
                        return
                else:
                    if not is_wall((row+1, col)) and not is_wall((row+2, col)):
                        nepritel.pohyb("s")
                        return
                        
    # Kontrola vpravo (3 políčka)
    for i in range(1, 4):
        if is_valid_position(row, col+i):
            if fields.matrix[row][col+i] == "@":
                if i == 1:
                    nepritel.pohyb("d")
                    return
                elif i == 2:
                    if not is_wall((row, col+1)):
                        nepritel.pohyb("d")
                        return
                else:
                    if not is_wall((row, col+1)) and not is_wall((row, col+2)):
                        nepritel.pohyb("d")
                        return
                        
    # Kontrola vlevo (3 políčka)
    for i in range(1, 4):
        if is_valid_position(row, col-i):
            if fields.matrix[row][col-i] == "@":
                if i == 1:
                    nepritel.pohyb("a")
                    return
                elif i == 2:
                    if not is_wall((row, col-1)):
                        nepritel.pohyb("a")
                        return
                else:
                    if not is_wall((row, col-1)) and not is_wall((row, col-2)):
                        nepritel.pohyb("a")
                        return
    
    # Kontrola vpravo nahoře
    if is_valid_position(row-1, col+1) and (fields.matrix[row-1][col+1] == "@"):
        if fields.helpMatrix[row-1][col] == "@":
            nepritel.pohyb("w")
            return
        elif fields.helpMatrix[row][col+1] == "@":
            nepritel.pohyb("d")
            return
        else:
            if not is_wall((row-1, col)):
                nepritel.pohyb("w")
                return
            elif not is_wall((row, col+1)):
                nepritel.pohyb("d")
                return
            
    # Kontrola vlevo nahoře     
    elif is_valid_position(row-1, col-1) and (fields.matrix[row-1][col-1] == "@"): 
        if fields.helpMatrix[row-1][col] == "@":
            nepritel.pohyb("w")
            return
        elif fields.helpMatrix[row][col-1] == "@":
            nepritel.pohyb("a")
            return
        else:
            if not is_wall((row-1, col)):
                nepritel.pohyb("w")
                return
            elif not is_wall((row, col-1)):
                nepritel.pohyb("a")
                return
    
    # Kontrola vpravo dole
    elif is_valid_position(row+1, col+1) and (fields.matrix[row+1][col+1] == "@"):
        if fields.helpMatrix[row+1][col] == "@":
            nepritel.pohyb("s")
            return
        elif fields.helpMatrix[row][col+1] == "@":
            nepritel.pohyb("d")
            return
        else:
            if not is_wall((row+1, col)):
                nepritel.pohyb("s")
                return
            elif not is_wall((row, col+1)):
                nepritel.pohyb("d")
                return
            
    # Kontrola vlevo dole
    elif is_valid_position(row+1, col-1) and (fields.matrix[row+1][col-1] == "@"):
        if fields.helpMatrix[row+1][col] == "@":
            nepritel.pohyb("s")
            return
        elif fields.helpMatrix[row][col-1] == "@":
            nepritel.pohyb("a")
            return
        else:
            if not is_wall((row+1, col)):
                nepritel.pohyb("s")
                return
            elif not is_wall((row, col-1)):
                nepritel.pohyb("a")
                return
            
    # Pokud hráče nevidí, pohybuje se náhodně
    while True:
        smer = random.choice(["W", "S", "A", "D"])
        if smer == "W":
            pohyb = (pozice[0] - 1, pozice[1])
        elif smer == "S":
            pohyb = (pozice[0] + 1, pozice[1])
        elif smer == "A":
            pohyb = (pozice[0], pozice[1] - 1)
        elif smer == "D":
            pohyb = (pozice[0], pozice[1] + 1)
        
        if not is_wall(pohyb):
            nepritel.pohyb(smer)
            break

def is_wall(pozice):
    row, col = pozice
    return fields.matrix[row][col] == "█"

def iswallbetween(fr, fc, sr, sc, tr, tc):
    return fields.matrix[fr][fc] == "█" or fields.matrix[sr][sc] == "█" or fields.matrix[tr][tc] == "█"

def is_valid_position(r, c):
    return r >= 0 and r < len(fields.matrix) and c >= 0 and c < len(fields.matrix[0])