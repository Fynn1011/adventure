import os

def clear_screen():
    if os.name =='nt':
        os.system('cls')

gegner_name_list = ["Troll", "Gnome", "Golem", "Ork"]
gegner_prefix_list = ["", "Grausamer", "Mächtiger", "Uralter"]
prefix_weight = [0.4, 0.2, 0.2, 0.2]

max_health_up = {
    "name": "Maximale Gesundheit Upgrade",
    "preis": 15,
    "effekt": "health_max"
}

player_attack_up = {
    "name": "Schadensupgrade",
    "preis": 20,
    "effekt": "attack_up"
}

player_health_potion = {
    "name": "Heiltrank",
    "preis": 8,
    "effekt": "player_heal"
}

item_shop = [max_health_up, player_attack_up, player_health_potion]

drop_heal = {
    "name": "Heiltrank",
}

drop_buff = {
    "name": "Schadensboost",
}

drop_list = [drop_heal, drop_buff]

def shop(player_stats):
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
    
def main():
    clear_screen()
    print("Willkommen Abenteurer!")
    player_name = input("Bitte verrat mir deinen namen: ")
    difficulty_multi = difficulty()

    player_stats = {
        "name": player_name,
        "health": 20,
        "max_health": 20,
        "attack": 3,
        "money": 0,
        "difficulty": difficulty_multi
    }
    
    print(f"Ok {player_name}, du spielst das Spiel mit einem Gegner Trefferpunkt Multiplikator von {difficulty_multi * 100}%")
    input("Beliebige Taste zum fortfahren drücken")
    game_active = True

    while game_active:
        clear_screen()
        enemy = spawn_enemy(player_stats["difficulty"])
        print(f"Ein wildes {enemy['name']} erscheint. Der Gegner hat {enemy['leben']} Leben und verursacht {enemy['angriff']} Schaden pro Angriff")
        battle_active = True

        while battle_active:
            enemy['leben'] = player_turn(player_stats, enemy['leben'])

            if enemy['leben'] == -69:
                print("Du bist entkommen")
                battle_active = False
                continue

            if enemy['leben'] <= 0:
                print(f"Du hast {enemy['name']} besiegt")
                battle_active = False
                player_stats = enemy_drop(player_stats)
                player_stats["money"] = player_stats["money"] + 10

                if input("Möchtest du dir deine aktuellen Werte anschauen? (Y/N): ").lower() == "y":
                    clear_screen()
                    show_stats(player_stats)
                    clear_screen()

                if input("Möchtest du den Shop besuchen? (Y/N): ").lower() == "y":
                    clear_screen()
                    player_stats = shop(player_stats)
                    clear_screen()

                continue   

            print(f"Der Gegner {enemy['name']} hat noch {enemy['leben']} Trefferpunkte")
            player_stats["health"] = enemy_turn(player_stats, enemy['angriff'], enemy['name'])

            if player_stats["health"] <= 0:
                game_active = False
                break

        if player_stats["health"] > 0:
            continue_game = input("Möchtest du weiterspielen (Y/N): ").lower()    
            if continue_game == "n":
                print(f"Danke fürs Spielen, {player_stats['name']}. Auf Wiedersehen")
                game_active = False
        else:
            game_active = False                

if __name__ == "__main__":
    main()