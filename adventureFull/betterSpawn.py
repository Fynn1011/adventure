import random

def spawn_enemy(difficulti_multi, gegner_name_list, gegner_prefix_list, prefix_weight):
    prefix = random.choices(gegner_prefix_list, prefix_weight)[0]
    enemy_base = random.choice(gegner_name_list)
    enemy = prefix + "" + enemy_base
    health = random.randint(10, 20) * difficulti_multi
    angriff = random.randint(1, 6) * difficulti_multi

    if prefix == "Grausamer":
        angriff = angriff * 1.2
    elif prefix == "Mächtiger":
        health = health * 1.2
    elif prefix == "Uralter":
        angriff = angriff * 0.6
        health = health * 2

    enemy_stats = {
        "name": enemy,
        "leben": health,
        "angriff": angriff
    }    
    return enemy_stats

def enemy_drop(player_stats, drop_list, drop_heal, drop_buff, player_items):
    drop = random.choice(drop_list)
    print(f"Du hast einen {drop} erhalten")

    user_input = input(f"Möchtest du den {drop['name']} jetzt benutzen? (Y/N)")

    if user_input.lower() == "y":
        if drop == drop_heal:
            if player_stats["health"] + 10 >= player_stats["max_health"]:
                player_stats["health"] = player_stats["max_health"]
                print(f"Du hast einen Heiltrank erhalten und hast jetzt wieder {player_stats['health']} Trefferpunkte")
            else:
                player_stats["health"] = player_stats["health"] + 10
                print(f"Du hast einen Heiltrank erhalten und hast jetzt wieder {player_stats['health']} Trefferpunkte")        

        if drop == drop_buff:
            player_stats["attack"] = player_stats["attack"] + 2
            print(f"Du hast einen Schadensbouns erhalten und verursachst jetzt {player_stats['attack']} Schaden pro Angriff")         

    else:
        player_items = player_items.append(drop)

    return player_stats, player_items    