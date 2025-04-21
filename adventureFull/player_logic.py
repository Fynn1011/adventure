def player_turn(player_stats, enemy_health):
    user_input = input("Was möchtest du tun? Angreifen oder Fliehen?: ").lower()
    clear_screen()

    if user_input == "angreifen" or user_input == "a":
        enemy_health = enemy_health - player_stats["attack"]
        return enemy_health
    elif user_input == "fliehen" or user_input == "f":
        ergebnis = random.choices(["erfolg", "fehlschlag"], [0.7, 0.3])[0]
        if ergebnis == "erfolg":
            print("Du konntest erfolgreich fliehen")
            return -69
        else:
            print("Du konntest nicht fliehen")
            return enemy_health
    else:
        print("Bitte gib eine gültige Eingabe ein")
        return player_turn(enemy_health)
    
def show_stats(player_stats):
clear_screen()
print(f"{player_stats['health']} Trefferpunkte von {player_stats['max_health']} maximalen Trefferpunkten")
print(f"{player_stats['attack']} Schaden pro Angriff")
print(f"{player_stats['money']} Münzen")
print(f"{player_stats['difficulty']} Schwierigkeitsgrad") 

 input("Beliebige Taste drücken um Seite zu verlassen: ")