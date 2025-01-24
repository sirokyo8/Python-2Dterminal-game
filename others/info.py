# EN: Function for printing rules and information about the game
# CZ: Funkce pro vypsání pravidel a informací o hře

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