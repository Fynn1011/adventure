from player_logic import clear_screen
from shop import shop
from player_logic import show_stats
from playerItem import item_inventory
from help import help_list

def input_handling(game_data):
    item_shop = game_data["item_shop"]
    item_shop = game_data["item_shop"]

    user_input = input("Bitte Aktion eingeben oder /help: ").lower()

    try:
        if user_input == "/help":
            clear_screen()
            help_list()
            clear_screen()

        if user_input == "shop":
            clear_screen()
            player_stats = shop(player_stats, item_shop)
            clear_screen()
        elif user_input == "stats":
            clear_screen()
            show_stats(player_stats)
            clear_screen()
        elif user_input == "inventar":
            clear_screen()
            player_items, player_stats = item_inventory(player_items, player_stats)
            clear_screen()
    except ValueError:
        print("Bitte gültige Eingabe eingeben oder /help:")
        return input_handling(game_data)