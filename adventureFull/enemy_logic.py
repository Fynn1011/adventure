import random

def spawn_enemy(difficulty_multi):
    prefix = random.choices(gegner_prefix_list, prefix_weight)[0]
    enemy_base = random.choice(gegner_name_list)
    enemy = prefix + " " + enemy_base
    health = random.randint(10, 20)
    health = health * difficulty_multi
    angriff = random.randint(1, 6)
    angriff = angriff * difficulty_multi

    enemy_stats = {
        "name": enemy,
        "leben": health,
        "angriff": angriff
    }
    return enemy_stats

def enemy_turn(player_stats, enemy_attack, enemy):
    player_stats["health"] = player_stats["health"] - enemy_attack 
    
    if player_stats["health"] > 0:
        print(f"{enemy} greift dich an und verursacht {enemy_attack} Schaden. Du hast noch {player_stats['health']} Trefferpunkte")
        return player_stats["health"]
    else:
        player_stats["health"] = 0
        print(f"{enemy} greift dich an und verursacht {enemy_attack} Schaden. Du hast noch {player_stats["health"]} Trefferpunkte. Du bist gestorben")
        print("Spiel beendet")

def enemy_drop(player_stats):
    drop = random.choice(drop_list)

    if drop == drop_heal:
        if player_stats["health"] + 10 >= player_stats["max_health"]:
            player_stats["health"] = player_stats["max_health"]
            print(f"Du hast einen Heiltrank erhalten und hast jetzt wieder {player_stats['max_health']} Trefferpunkte")
        else:
            player_stats["health"] = player_stats["health"] + 10
            print(f"Du hast einen Heiltrank erhalten und hast jetzt wieder {player_stats['health']} Trefferpunkte")

    if drop == drop_buff:
        player_stats["attack"] = player_stats["attack"] + 2  
        print(f"Du hast einen Schadensbonus erhalten und verursachst jetzt {player_stats['attack']} Schaden pro Angriff")      

    return player_stats        