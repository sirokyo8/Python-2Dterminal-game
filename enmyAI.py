# AI for enmy (#)
# AI pro nepřítele (#)

# The enemy can see the player within 2 spaces (after spotting him, he moves towards him). Otherwise it moves to a random location.
# Nepřítel může hráče vidět do vzdálenosti 2 pole (po zahlédnutí se pohybuje směrem k němu). Jinak se přesouvá na náhodné místo.

import fields

def enmysMove(pozice, nepritel):
    
    # Kontrola zda nepřítel nemůže vidět hráče - pokud ano, posune se k němu
    row, col = pozice
    if fields.matrix[row-1][col] == "@" or fields.matrix[row-2][col] == "@" and not iswallbetween(row-1,col,row-2,col):     # 1. kontrola je 2 pole nahoře
        nepritel.pohyb(nepritel, "W")
    elif fields.matrix[row+1][col] == "@" or fields.matrix[row+2][col] == "@" and not iswallbetween(row+1,col,row+2,col):   # 2. kontrola je 2 pole dole
        nepritel.pohyb(nepritel, "S")
    elif fields.matrix[row][col+1] == "@" or fields.matrix[row][col-2] == "@" and not iswallbetween(row,col+1,row,col+2):   # 3. kontrola je 2 pole vpravo
        nepritel.pohyb(nepritel, "D")
    elif fields.matrix[row][col-1] == "@" or fields.matrix[row][col-2] == "@" and not iswallbetween(row,col-1,row,col-2):   # 4. kontrola je 2 pole vlevo
        nepritel.pohyb(nepritel, "A")
        
def iswallbetween(fr,fc,sr,sc): # fr = first row, sc = second column etc.
    if fields.matrix[fr][fc] != "█" and fields.matrix[sr][sc] != "█":
        return True
    else: return False