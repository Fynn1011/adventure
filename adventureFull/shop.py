import os
from player_logic import clear_screen

def shop(player_stats, item_shop):
    print("="*80)
    print(f"Willkommen im Shop {player_stats['name']}")
    print(f"Du hast {player_stats['money']} Münzen")
    print("Folgende Items stehen zum Verkauf:")
    print(f"0. Shop verlassen")

    for i in range(len(item_shop)):
        print(f"{i+1}. {item_shop[i]['name']} - {item_shop[i]['preis']} Münzen")
    
    choice = int(input("Welches Item möchtest du kaufen? (Gib die Nummer ein): "))

    try:
        if choice == 0:
            print("Auf Wiedersehen")
            return player_stats
        
        if choice >= 1 and choice <= len(item_shop):
            selected_item = item_shop[choice-1]

            if player_stats["money"] >= selected_item['preis']:
                player_stats["money"] = player_stats["money"] - selected_item['preis']

                if selected_item['effekt'] == "health_max":
                    player_stats["max_health"] = player_stats["max_health"] + 10
                    print(f"Deine Maximale Gesundheit ist auf {player_stats['max_health']} gestiegen")
                    return player_stats
                elif selected_item['effekt'] == "attack_up":
                    player_stats["attack"] = player_stats["attack"] + 3
                    print(f"Dein Schadenswert ist auf {player_stats['attack']} gestiegen")
                    return player_stats
                elif selected_item['effekt'] == "player_heal":
                    player_stats["health"] = player_stats["health"] + 5
                    print(f"Dein Gesunheit ist auf {player_stats['health']} gestiegen")
                    return player_stats

            print(f"Du hast noch {player_stats['money']} Münzen")
            return shop(player_stats)
        else:
            print("Du hast nicht genug Münzen")
            return shop(player_stats)
    except ValueError:
        print("Bitte gib eine Zahl ein")
        return shop(player_stats)    