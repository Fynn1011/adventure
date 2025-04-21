def difficulty():
    user_input = input("Bitte gib die Schwierigkeit ein (Leicht, Mittel, Schwer): ").lower()

    if user_input == "leicht":
        return 0.5
    elif user_input == "mittel":
        return 0.7
    elif user_input == "schwer":
        return 1
    else:
        print("Bitte gib eine gültige Schwierigkeit ein")
        return difficulty()