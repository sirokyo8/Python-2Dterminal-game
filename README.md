# 2D Terminálová Hra

Toto je jednoduchá 2D hra založená na terminálu, kde ovládáte postavu hráče a interagujete s nepřítelem. Hra se hraje na mřížce a můžete pohybovat svou postavou, sbírat předměty a bojovat s nepřítelem.

## Jak hrát

### Ovládání

- `W` - Pohyb nahoru
- `A` - Pohyb doleva
- `S` - Pohyb dolů
- `D` - Pohyb doprava
- `WW`, `AA`, `SS`, `DD` - Pohyb dvakrát ve zvoleném směru (vyžaduje útěk)
- `info` - Zobrazit informace o hře
- `zdravi` - Zobrazit zdraví hráče a nepřítele
- `brneni` - Zobrazit brnění hráče a nepřítele
- `sila` - Zobrazit sílu hráče a nepřítele
- `pocet-uteku` - Zobrazit počet útěků hráče
- `ja` - Zobrazit statistiky hráče
- `nepritel` - Zobrazit statistiky nepřítele
- `boj` - Zahájit boj s nepřítelem (pokud je vedle)
- `konec` nebo `break` - Ukončit hru
- `reset-mapy` - Resetovat herní mapu

### Cíl

Cílem hry je porazit nepřítele snížením jeho zdraví na nulu, zatímco si udržíte své zdraví nad nulou. Můžete sbírat předměty na mapě, které zvýší vaše zdraví, sílu, brnění nebo vám poskytnou další útěky.

### Předměty

- `*` - Představuje předmět na mapě. Předměty mohou zvýšit vaše zdraví, sílu, brnění nebo vám poskytnout další útěk.

### Podmínky pro konec hry

- Pokud zdraví hráče i nepřítele klesne na nulu, hra končí remízou.
- Pokud zdraví hráče klesne na nulu, hráč prohrává.
- Pokud zdraví nepřítele klesne na nulu, hráč vyhrává.

## Spuštění hry

Pro spuštění hry spusťte soubor `main.py`:

```sh
python main.py
```

## Soubory

- `players.py` - Obsahuje třídy hráče a nepřítele a jejich logiku pohybu.
- `main.py` - Hlavní herní smyčka a zpracování uživatelského vstupu.
- `functions.py` - Herní funkce jako zobrazení herního pole, kontrola pozic a zpracování boje.
- `fields.py` - Definuje herní mapu.
- `enmyAI.py` - Obsahuje logiku AI pro pohyby nepřítele.

Užijte si hru!

---

# 2D Terminal Game

This is a simple 2D terminal-based game where you control a player character and interact with an enemy. The game is played on a grid, and you can move your character, collect items, and engage in combat with the enemy.

## How to Play

### Controls

- `W` - Move up
- `A` - Move left
- `S` - Move down
- `D` - Move right
- `WW`, `AA`, `SS`, `DD` - Move twice in the specified direction (requires an escape item)
- `info` - Display game information
- `zdravi` - Display player's and enemy's health
- `brneni` - Display player's and enemy's armor
- `sila` - Display player's and enemy's strength
- `pocet-uteku` - Display the number of escapes the player has
- `ja` - Display player's stats
- `nepritel` - Display enemy's stats
- `boj` - Engage in combat with the enemy (if adjacent)
- `konec` or `break` - End the game
- `reset-mapy` - Reset the game map

### Objective

The objective of the game is to defeat the enemy by reducing their health to zero while keeping your own health above zero. You can collect items on the map to increase your health, strength, armor, or gain additional escapes.

### Items

- `*` - Represents an item on the map. Items can increase your health, strength, armor, or give you an additional escape.

### Game Over Conditions

- If both the player and the enemy's health drop to zero, the game ends in a draw.
- If the player's health drops to zero, the player loses.
- If the enemy's health drops to zero, the player wins.

## Running the Game

To start the game, run the `main.py` file:

```sh
python main.py
```

## Files

- `players.py` - Contains the player and enemy classes and their movement logic.
- `main.py` - The main game loop and user input handling.
- `functions.py` - Game functions such as displaying the game board, checking positions, and handling combat.
- `fields.py` - Defines the game map.
- `enmyAI.py` - Contains the AI logic for the enemy's movements.

Enjoy the game!