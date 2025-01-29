# AI for enmy (#)
# AI pro nepřítele (#)

# The enemy can see the player within 2 spaces (after spotting him, he moves towards him). Otherwise it moves to a random location.
# Nepřítel může hráče vidět do vzdálenosti 2 pole (po zahlédnutí se pohybuje směrem k němu). Jinak se přesouvá na náhodné místo.

import fields, random

def enmysMove(pozice, nepritel):
    
    # Kontrola zda nepřítel nemůže vidět hráče - pokud ano, posune se k němu
    row, col = pozice
    if (fields.matrix[row-1][col] == "@" or fields.matrix[row-2][col] == "@") and not iswallbetween(row-1, col, row-2, col):     # 1. kontrola je 2 pole nahoře
        nepritel.pohyb("w")
    elif (fields.matrix[row+1][col] == "@" or fields.matrix[row+2][col] == "@") and not iswallbetween(row+1, col, row+2, col):   # 2. kontrola je 2 pole dole
        nepritel.pohyb("s")
    elif (fields.matrix[row][col+1] == "@" or fields.matrix[row][col+2] == "@") and not iswallbetween(row, col+1, row, col+2):   # 3. kontrola je 2 pole vpravo
        nepritel.pohyb("d")
    elif (fields.matrix[row][col-1] == "@" or fields.matrix[row][col-2] == "@") and not iswallbetween(row, col-1, row, col-2):   # 4. kontrola je 2 pole vlevo
        nepritel.pohyb("a")
    elif (fields.matrix[row-1][col+1] == "@"): # 5. kontrola je vpravo nahoře
        if not is_wall((row, col+1)):
            nepritel.pohyb("d")
        elif not is_wall((row-1, col)):  # Jakou cestu má nepřítel zvolit?
            nepritel.pohyb("w")
    elif (fields.matrix[row-1][col-1] == "@"): # 6. kontrola je vlevo nahoře
        if not is_wall((row, col-1)):
            nepritel.pohyb("a")
        elif not is_wall((row-1, col)):  # Jakou cestu má nepřítel zvolit?
            nepritel.pohyb("w")
    elif (fields.matrix[row+1][col+1] == "@"): # 7. kontrola je vpravo dole
        if not is_wall((row, col+1)):
            nepritel.pohyb("d") 
        elif not is_wall((row+1, col)):  # Jakou cestu má nepřítel zvolit?
            nepritel.pohyb("s")
    elif (fields.matrix[row+1][col-1] == "@"): # 8. kontrola je vlevo dole
        if not is_wall((row, col-1)):
            nepritel.pohyb("a")
        elif not is_wall((row+1, col)):  # Jakou cestu má nepřítel zvolit?
            nepritel.pohyb("s")
            
            
    # Pokud hráče nevidí, pohybuje se náhodně
    else:
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

def iswallbetween(fr, fc, sr, sc):
    return fields.matrix[fr][fc] == "█" or fields.matrix[sr][sc] == "█"