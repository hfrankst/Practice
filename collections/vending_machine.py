sodas = ["Root Beer", "Sprite", "Mountain Dew"]
chips = ["Doritos", "Miss Vicki's"]
candy = ["Reese's", "M&M's", "Twizzlers"]

while True:
    choice = input("Would you like a SODA, some CHIPS, or a CANDY? ").lower()
    if choice == 'soda':
        snack = sodas.pop()
    elif choice == 'chips':
        snack = chips.pop()
    elif choice == 'candy':
        snack = candy.pop()
    else:
        print("Sorry, I didn't understand that.")
        continue
    print("Here's your {}: {}".format(choice, snack))
    