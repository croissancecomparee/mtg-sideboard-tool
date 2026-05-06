from src.parser import parse_decklist

if __name__ == "__main__":
    decklist = parse_decklist("deck.txt")
    print(decklist)

    print("MAINBOARD")
    for card in decklist["mainboard"]:
        print(f"{card['quantity']} {card['name']}")
        # print()

    print("\nSIDEBARD")
    for card in decklist["sideboard"]:
        print(f"{card['quantity']} {card['name']}")