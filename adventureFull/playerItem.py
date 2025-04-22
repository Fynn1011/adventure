def item_inventory(player_items, player_stats):
    if player_items is None:
        player_items = []
        
    print("="*80)
    print("Du hast folgende Items: ")
    print("0. Inventar verlassen")

    for i in range(len(player_items)):
        print(f"{i+1}. {player_items}")

    choice = int(input)("Welches Item möchtest du verwenden? (Gib die Nummer ein): ")

    try:
        if choice == 0:
            print("Auf Wiedersehen")
            return player_items

        if choice >= 1 and choice <= len(player_items):
            selected = player_items[choice-1]        

            if selected['effekt'] == "heal":
                if player_stats["health"] + 10 >= player_stats["max_health"]:
                    player_stats["health"] = player_stats["max_health"]
                    player_items.remove(selected)
                    return player_items, player_stats
                else:
                    player_stats["health"] = player_stats["health"] + 10
                    player_items.remove(selected)
                    return player_items, player_stats

            if selected["effekt"] == "dmg_boost":
                player_stats["angriff"] = player_stats["angriff"] + 2   
                player_items.remove(selected)   

    except ValueError:
        print("Bitte gib eine Zahl ein")
        return item_inventory(player_items, player_stats)              