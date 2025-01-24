# AI for enmy (#)
# AI pro nepřítele (#)

# The enemy can see the player within 2 spaces (after spotting him, he moves towards him). Otherwise it moves to a random location.
# Nepřítel může hráče vidět do vzdálenosti 2 pole (po zahlédnutí se pohybuje směrem k němu). Jinak se přesouvá na náhodné místo.

import fields, players

def enmysMove(pozice, nepritel):
    # Kontrola zda nepřítel nemůže vidět hráče
    row, col = pozice
    if fields.matrix[row-1][col] == "@" or fields.matrix[row-2][col] == "@": # 1. kontrola je 2 pole nahoře
        players.pohyb(nepritel, "W")