from difficulty import difficulty
from player_logic import player_turn, show_stats, clear_screen 
from enemy_logic import spawn_enemy, enemy_turn, enemy_drop
from shop import shop
from playerItem import item_inventory
from input_handling import input_handling

input_list = ["shop", "inventar", "stats"]

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
    "effekt": "heal"
}

drop_buff = {
    "name": "Schadensboost",
    "effekt": "dmg_boost"
}

drop_list = [drop_heal, drop_buff]
    
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

    player_items = []

    game_data = {
    "input_list": input_list,
    "item_shop": item_shop,
    "player_stats": player_stats,
    "item_inventory": player_items,
    }
    
    print(f"Ok {player_name}, du spielst das Spiel mit einem Gegner Trefferpunkt Multiplikator von {difficulty_multi * 100}%")
    input("Beliebige Taste zum fortfahren drücken")
    game_active = True

    while game_active:
        clear_screen()
        enemy = spawn_enemy(player_stats["difficulty"], gegner_name_list, gegner_prefix_list, prefix_weight)
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
                player_stats, player_items = enemy_drop(player_stats, drop_list, drop_heal, drop_buff, player_items)
                player_stats["money"] = player_stats["money"] + 10

                input_handling(game_data)

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